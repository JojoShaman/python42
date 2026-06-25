from typing import Any
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
        print("== DataStream statistics ==")
        if self.proc_list:
            for x in self.proc_list:
                print(f"{x.name}: total {x.processed} items processed, ",
                      f"remaining {len(x._data)} on processor")
        else:
            print("No processor found, no data")


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.name = "Numeric Processor"

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
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    process = DataStream()
    process.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO',
          'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    process.register_processor(NumericProcessor())
    process.process_stream(data)
    process.print_processors_stats()
    print("\nRegistering other data processors\n" +
          "Send the same batch again")
    process.register_processor(TextProcessor())
    process.register_processor(LogProcessor())
    process.process_stream(data)
    process.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        process.proc_list[0].output()
    for _ in range(2):
        process.proc_list[1].output()
    for _ in range(1):
        process.proc_list[2].output()
    process.print_processors_stats()
