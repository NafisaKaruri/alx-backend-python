# 0x01. Python - Async Function

This project focuses on understanding and implementing asynchronous programming in Python using the `asyncio` library. The solutions for the tasks are organized in this directory.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without assistance:

- The `async` and `await` syntax.
- How to execute an async program using `asyncio`.
- How to run concurrent coroutines.
- How to create `asyncio` tasks.
- How to utilize the `random` module.

## Resources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Tasks Overview

1. **The Basics of Async - `wait_random`**  
   - **File:** `0-basic_async_syntax.py`  
   - **Description:** Implements an asynchronous coroutine `wait_random` that waits for a random delay between 0 and `max_delay` (default 10) seconds and returns the delay.

2. **Concurrent Coroutines - `wait_n`**  
   - **File:** `1-concurrent_coroutines.py`  
   - **Description:** Implements `wait_n`, which spawns `wait_random` `n` times with a specified `max_delay`, returning the list of delays in ascending order.

3. **Measure Runtime - `measure_time`**  
   - **File:** `2-measure_runtime.py`  
   - **Description:** Measures the total execution time for `wait_n(n, max_delay)` and returns the average time per coroutine.

4. **Create Async Tasks - `task_wait_random`**  
   - **File:** `3-tasks.py`  
   - **Description:** Implements `task_wait_random`, which creates an `asyncio.Task` for a given `max_delay`.

5. **Concurrent Tasks - `task_wait_n`**  
   - **File:** `4-tasks.py`  
   - **Description:** Similar to `wait_n`, but uses `task_wait_random` to spawn tasks instead.

## Running Tests

Each task includes a corresponding main file that can be used to test the implementations. Use the following command to run a specific main file:

```bash
./[filename]
```

Replace `[filename]` with the name of the main file. For example, to test the `wait_random` function, you would run:

```bash
./0-main.py
```

## Conclusion
This project provides a solid foundation in asynchronous programming in Python, highlighting the capabilities of the `asyncio` library. Each task builds upon the previous one, reinforcing your understanding of concurrent execution and coroutine management.
