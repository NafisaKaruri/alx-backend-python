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
   Write a type-annotated function `add` that takes two floats and returns their sum.  
   - **File**: `0-add.py`

2. **Basic Annotations - `concat`**  
   Write a type-annotated function `concat` that takes two strings and returns their concatenated value.  
   - **File**: `1-concat.py`

3. **Basic Annotations - `floor`**  
   Write a type-annotated function `floor` that takes a float and returns its floor value.  
   - **File**: `2-floor.py`

4. **Basic Annotations - `to_str`**  
   Write a type-annotated function `to_str` that converts a float to its string representation.  
   - **File**: `3-to_str.py`

5. **Define Variables**  
   Define and annotate several variables with specific types and values.  
   - **File**: `4-define_variables.py`

6. **Complex Types - List of Floats**  
   Write a type-annotated function `sum_list` that takes a list of floats and returns their sum.  
   - **File**: `5-sum_list.py`

7. **Complex Types - Mixed List**  
   Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum.  
   - **File**: `6-sum_mixed_list.py`

8. **Complex Types - String and Int/Float to Tuple**  
   Write a type-annotated function `to_kv` that takes a string and an int/float and returns a tuple.  
   - **File**: `7-to_kv.py`

9. **Complex Types - Functions**  
   Write a type-annotated function `make_multiplier` that returns a function multiplying a float by a given multiplier.  
   - **File**: `8-make_multiplier.py`

10. **Let's Duck Type an Iterable Object**  
    Annotate the `element_length` function with the appropriate types.  
    - **File**: `9-element_length.py`

11. **Duck Typing - First Element of a Sequence**  
    Annotate the `safe_first_element` function with duck-typed annotations.  
    - **File**: `100-safe_first_element.py`

12. **More Involved Type Annotations**  
    Add type annotations to the `safely_get_value` function using `TypeVar`.  
    - **File**: `101-safely_get_value.py`

13. **Type Checking**  
    Use `mypy` to validate and modify the `zoom_array` function for type checking.  
    - **File**: `102-type_checking.py`

## Conclusion

This project provides a comprehensive overview of variable annotations in Python, emphasizing type safety and code clarity. Each task builds on the previous one, helping you to solidify your understanding of advanced Python concepts.
