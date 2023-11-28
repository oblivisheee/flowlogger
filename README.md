# flowlogger
flowlogger currently is small lib in pre-alpha version for helping with ML training logging.
# What is this?

flowlogger is a lib for ML training logging, currently is very few functions, in future will be improved.
*Currently in pre alpha*
# Installing
Via pip:
```python
pip install flowlogger
```
# Usage
**Calculating the function execution time**:

Using dict:
```python
import flowlogger as fl
options = {
        'class_name': 'Test'
        'save_path': 'test.log',
        'print_output': True
        'return_dict': True
    }
@fl.flclass(options=options)
def print_world():
    print('Hello World!')

print_world()
```
Using vars:
```python
import flowlogger as fl
@fl.flclass(class_name='Test', save_path='hello.log')
def five_plus_five():
    solution = 5 + 5
    print(solution)

five_plus_five()
```
