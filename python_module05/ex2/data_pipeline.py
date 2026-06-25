from typing import Any
from typing import Protocol
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list = []
        self.name = "Default processor"
        self.processed = 0

    def output(self) -> tuple[int, str]:
        data_tuple = tuple([(self.processed - len(self._data)), self._data[0]])
        self._data.pop(0)
        return data_tuple

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_output: str = ','.join(item[1] for item in data)
        print("CSV Output:\n" + csv_output)


class JsonPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_output: str = ', '.join(f'"item_{item[0]}": "{item[1]}"'
                                     for item in data)
        print("JSON Output:\n" +
              '{' + json_output + '}')


class DataStream():
    def __init__(self) -> None:
        self.proc_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.proc_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        if self.proc_list:
            error = False
            for element in stream:
                for x in self.proc_list:
                    if x.validate(element):
                        x.ingest(element)
                        error = False
                        break
                    else:
                        error = True
                if error:
                    print("DataStream error - ",
                          f"Can't process element in stream: {element}")
        else:
            print("No processor found, no processing")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if self.proc_list:
            for x in self.proc_list:
                print(f"{x.name}: total {x.processed} items processed, ",
                      f"remaining {len(x._data)} on processor")
        else:
            print("No processor found, no data")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.proc_list:
            outputs = []
            for _ in range(nb):
                if processor._data:
                    outputs.append(processor.output())
            plugin.process_output(outputs)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.name = "Numeric Processor"
        self.processed = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return (all(isinstance(element, (int, float)) for element in data))
        elif isinstance(data, (int, float)):
            return True
        else:
            return False

    def ingest(self, data: int | float | list) -> None:
        if self.validate(data):
            if isinstance(data, list):
                self.processed += len(data)
                self._data.extend([str(element) for element in data])
            elif isinstance(data, (int, float)):
                self.processed += 1
                self._data.append(str(data))
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return (all(isinstance(element, str) for element in data))
        elif isinstance(data, str):
            return True
        else:
            return False

    def ingest(self, data: str | list) -> None:
        if self.validate(data):
            if isinstance(data, list):
                self.processed += len(data)
                self._data.extend([element for element in data])
            elif isinstance(data, str):
                self.processed += 1
                self._data.append(data)
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return (all(isinstance(element, dict) for element in data))
        elif isinstance(data, dict):
            return True
        else:
            return False

    def ingest(self, data):
        if self.validate(data):
            if isinstance(data, list):
                self.processed += len(data)
                self._data.extend(
                    [f"{element['log_level']}: {element['log_message']}"
                     for element in data])
            elif isinstance(data, dict):
                self.processed += 1
                self._data.append(str(data))
        else:
            raise ValueError("Improper log data")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    process = DataStream()
    process.print_processors_stats()
    print("\nRegistering Processor\n")
    process.register_processor(NumericProcessor())
    process.register_processor(TextProcessor())
    process.register_processor(LogProcessor())
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO',
          'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']]
    data_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR',
          'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello']
    print(f"Send first batch of data on stream: {data}")
    process.process_stream(data)
    process.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    process.output_pipeline(3, CsvPlugin())
    process.print_processors_stats()
    print(f"Send another batch of data : {data_2}")
    process.process_stream(data_2)
    process.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    process.output_pipeline(5, JsonPlugin())
    process.print_processors_stats()
