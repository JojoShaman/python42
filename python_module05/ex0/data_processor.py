from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list = []
        self._rank = 0

    def output(self) -> tuple[int, str]:
        data_tuple = tuple([self._rank, self._data[0]])
        self._data.pop(0)
        self._rank += 1
        return data_tuple

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):
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
                self._data.extend([str(element) for element in data])
            elif isinstance(data, (int, float)):
                self._data.append(str(data))
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
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
                self._data.extend([element for element in data])
            elif isinstance(data, str):
                self._data.append(data)
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
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
                self._data.extend(
                    [f"{element['log_level']}: {element['log_message']}"
                     for element in data])
            elif isinstance(data, dict):
                self._data.append(str(data))
        else:
            raise ValueError("Improper log data")


if __name__ == "__main__":
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': {numeric.validate(42)}")
    print(f" Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    # try:
    #     numeric.ingest('foo')
    # except Exception as e:
    #     print(f" Got exception: {e}")
    numeric.ingest([1, 2, 3, 4, 5])
    print(" Processing data: [1, 2, 3, 4, 5]")
    print(" Extracting 3 values...")
    for x in range(3):
        rank, value = numeric.output()
        print(f" Numeric value {rank}: {value}")
    print("\nTesting Text Processor...")
    print(f" Trying to validate input '42': {text.validate(42)}")
    text.ingest(['Hello', 'Nexus', 'World'])
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    print(" Extracting 1 value...")
    rank, value = text.output()
    print(f" Text value {rank}: {value}")
    print("\nTesting Log Processor...")
    print(f" Trying to validate input '42': {log.validate({42, 'wesh'})}")
    log.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    print(" Processing data: "
          "[{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, "
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    print(" Extracting 2 value...")
    for x in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")
