"""task_1.py"""

import time
import threading


class FileCreator:
    """File create class"""

    def __init__(self, filename, encoding="utf-8"):
        """initial method"""
        self.filename = filename
        self.encoding = encoding

    def create_file(self):
        """create file method"""
        time.sleep(1)
        with open(self.filename, "w", encoding=self.encoding):
            pass


def main():
    """main method"""
    # однопоточный процесс
    start_time = time.time()
    for i in range(100):
        file_creator = FileCreator(f"file_{i+1}.txt")
        file_creator.create_file()
    end_time = time.time()
    print(f"Время выполнения цикла: {end_time - start_time}")

    # многопоточный процесс
    start_time = time.time()
    threads = []
    for i in range(100):
        file_creator = FileCreator(f"file_{i+1}.txt")
        thread = threading.Thread(target=file_creator.create_file)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Время выполнения многопоточности: {end_time - start_time}")


if __name__ == "__main__":
    main()
