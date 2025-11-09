# Python - Test-driven development

This directory contains Python scripts demonstrating test-driven development (TDD) practices.

## Tasks

### Mandatory Tasks

0. **Integers addition** - `0-add_integer.py`
   - Adds 2 integers or floats
   - Raises TypeError for invalid inputs

1. **Divide a matrix** - `2-matrix_divided.py`
   - Divides all elements of a matrix by a number
   - Handles various edge cases

2. **Say my name** - `3-say_my_name.py`
   - Prints formatted name string
   - Validates string inputs

3. **Print square** - `4-print_square.py`
   - Prints a square with the character #
   - Validates size parameter

4. **Text indentation** - `5-text_indentation.py`
   - Prints text with 2 new lines after ., ? and :
   - Handles string formatting

5. **Max integer - Unittest** - `6-max_integer.py`
   - Finds the maximum integer in a list
   - Includes unittest test cases

## Requirements

- All files must be executable
- All files must end with a new line
- Code should use pycodestyle (version 2.7.*)
- All modules and functions must have documentation
- Tests should be written before implementation (TDD approach)
- Test files should be in `tests/` directory with `.txt` extension for doctest
- Unittest files should be in `tests/` directory with `.py` extension

## Testing

Run doctest:
```bash
python3 -m doctest -v ./tests/*.txt
```

Run unittest:
```bash
python3 -m unittest tests.6-max_integer_test
```

