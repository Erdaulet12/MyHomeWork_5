"""task_2.py"""

import random
import time
from threading import Thread


def generate_random_number(filename):
    """
    Функция генерирует случайное число и записывает его в файл.

    Args:
      filename: Имя файла для записи.
    """
    with open(filename, "w", encoding="utf-8") as f:
        time.sleep(0.1)
        f.write(str(random.randint(1, 1000)))


def main():
    """main method"""
    # Запуск функции без многопоточности

    for i in range(1000):
        generate_random_number(f"random_number_{i}.txt")

    # Замер времени выполнения без многопоточности

    start_time = time.time()
    for i in range(1000):
        generate_random_number(f"random_number_{i}.txt")
    end_time = time.time()

    print(f"Время выполнения без многопоточности: {end_time - start_time}")

    # Функция для многопоточного выполнения

    def multithreaded_generate_random_number(filenames):
        """
        Функция для многопоточного генерирования случайных чисел.

        Args:
          filenames: Список имен файлов для записи.
        """
        threads = []
        for filename in filenames:
            thread = Thread(target=generate_random_number, args=(filename,))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    # Запуск функции с многопоточностью

    filenames = [f"random_number_{i}.txt" for i in range(1000)]

    start_time = time.time()
    multithreaded_generate_random_number(filenames)
    end_time = time.time()

    print(f"Время выполнения с многопоточностью: {end_time - start_time}")


if __name__ == "__main__":
    main()
