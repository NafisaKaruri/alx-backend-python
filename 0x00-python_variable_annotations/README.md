# 0x00. Python - Variable Annotations

This project focuses on understanding and implementing variable annotations in Python. The solutions for the tasks are organized in this directory. 

## Learning Objectives

- Explain type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Understand duck typing.
- Validate your code with `mypy`.

## Resources

- [Python 3 Typing Documentation](https://docs.python.org/3/library/typing.html)
- [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Tasks Overview

1. **Basic Annotations - `add`**  
   - **File:** `0-add.py`  
   - **Description:** Implements a type-annotated function `add` that takes two floats and returns their sum.

2. **Basic Annotations - `concat`**  
   - **File:** `1-concat.py`  
   - **Description:** Implements a type-annotated function `concat` that takes two strings and returns their concatenated value.

3. **Basic Annotations - `floor`**  
   - **File:** `2-floor.py`  
   - **Description:** Implements a type-annotated function `floor` that takes a float and returns its floor value.

4. **Basic Annotations - `to_str`**  
   - **File:** `3-to_str.py`  
   - **Description:** Implements a type-annotated function `to_str` that converts a float to its string representation.

5. **Define Variables**  
   - **File:** `4-define_variables.py`  
   - **Description:** Defines and annotates several variables with specific types and values.

6. **Complex Types - List of Floats**  
   - **File:** `5-sum_list.py`  
   - **Description:** Implements a type-annotated function `sum_list` that takes a list of floats and returns their sum.

7. **Complex Types - Mixed List**  
   - **File:** `6-sum_mixed_list.py`  
   - **Description:** Implements a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum.

8. **Complex Types - String and Int/Float to Tuple**  
   - **File:** `7-to_kv.py`  
   - **Description:** Implements a type-annotated function `to_kv` that takes a string and an int/float and returns a tuple.

9. **Complex Types - Functions**  
   - **File:** `8-make_multiplier.py`  
   - **Description:** Implements a type-annotated function `make_multiplier` that returns a function multiplying a float by a given multiplier.

10. **Let's Duck Type an Iterable Object**  
    - **File:** `9-element_length.py`  
    - **Description:** Annotates the `element_length` function with appropriate types.

11. **Duck Typing - First Element of a Sequence**  
    - **File:** `100-safe_first_element.py`  
    - **Description:** Annotates the `safe_first_element` function with duck-typed annotations.

12. **More Involved Type Annotations**  
    - **File:** `101-safely_get_value.py`  
    - **Description:** Adds type annotations to the `safely_get_value` function using `TypeVar`.

13. **Type Checking**  
    - **File:** `102-type_checking.py`  
    - **Description:** Validates and modifies the `zoom_array` function for type checking using `mypy`.

## Running Tests

Each task comes with a corresponding main file that can be used to test the implementations. Use the following command to run a specific main file:

```bash
./[filename]
```

Replace `[filename]` with the name of the main file. For example, to test the add function, you would run:

```bash
./0-main.py
```

## Conclusion

This project provides a comprehensive overview of variable annotations in Python, emphasizing type safety and code clarity. Each task builds on the previous one, helping you to solidify your understanding of advanced Python concepts.

