# 0x02. Python - Async Comprehension

This project focuses on understanding and implementing asynchronous comprehensions in Python. The solutions for the tasks are organized in this directory.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without assistance:

- The use of asynchronous comprehensions in Python.
- How to combine `async` functions with list comprehensions.
- How to effectively work with `asyncio` and asynchronous iterators.
- The benefits of using async comprehensions for concurrent execution.

## Resources

- [Python Official Documentation on Asynchronous Comprehensions](https://docs.python.org/3/whatsnew/3.8.html#async-comprehensions)
- [Real Python: Asynchronous Comprehensions](https://realpython.com/python-async-comprehension/)

## Tasks Overview

1. **Basic Async Comprehension - `async_comprehension`**  
   - **File:** `0-async_comprehension.py`  
   - **Description:** Implements an asynchronous comprehension to gather a list of random delays using an async function.

2. **Async Generator - `async_generator`**  
   - **File:** `1-async_generator.py`  
   - **Description:** Creates an asynchronous generator that yields random delays.

3. **Using Async Comprehension with Generator - `wait_n`**  
   - **File:** `2-wait_n.py`  
   - **Description:** Utilizes the asynchronous generator with an async comprehension to return a list of delays.

4. **Measure Execution Time - `measure_time`**  
   - **File:** `3-measure_time.py`  
   - **Description:** Measures the execution time for the async comprehension tasks.

## Running Tests

Each task includes a corresponding main file that can be used to test the implementations. Use the following command to run a specific main file:

```bash
./[filename]
```

Replace `[filename]` with the name of the main file. For example, to test the async comprehension, you run

```bash
./0-main.py
```

## Conclusion

This project provides a comprehensive overview of asynchronous comprehensions in Python, demonstrating how to effectively leverage async programming to achieve concurrent execution. Each task builds on the previous one, enhancing your understanding of this powerful feature in Python.
