import time
from typing import Union, Dict

def flclass(class_name: str=None,
            return_dict: bool=True,
            save_path: str=None,
            print_output: bool=False,
            options: Dict[str, Union[bool, str]]=None):
    """
    This is a decorator function that logs the execution time of a function and the class name.
    It takes a class name as an argument and returns a decorator.
    The decorator wraps the function, logs the start and end time, calculates the execution time,
    and returns the execution time and class name.
    
    Parameters:
    class_name (str): The name of the class.
    return_dict (bool): If true, return dict with data. Else, return variables: class_name, exec_time
    save_path (str): If provided, save the execution time and class name to this file path.
    options (dict): You can load options immeadiatly through dict by format presented below.

    Dict format:
    ```python
    options = {
        'class_name': 'Test'
        'save_path': 'test.log',
        'print_output': True
        'return_dict': True
    }
    ```

    Returns:
    Dict or str, depends on return_dict bool variable.

    Usage example:
    ```python
    @flclass("Greeting to the world")
    def world():
        print("Hello World!")

    world()
    ```
    """
    if options:
        class_name = options.get('class_name', class_name)
        return_dict = options.get('return_dict', return_dict)
        save_path = options.get('save_path', save_path)
        print_output = options.get('print_output', print_output)
    if class_name is None:
        raise ValueError('Class name is missing.')

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            exec_time = end_time - start_time
            time_unit = "seconds"
            if exec_time < 1e-6:
                exec_time *= 1e6
                time_unit = "microseconds"
            elif exec_time < 1e-3:
                exec_time *= 1e3
                time_unit = "milliseconds"
            if print_output:
                print(f"Execution time of part {class_name}: {exec_time:.2f} {time_unit}")
            if return_dict:
                data = {"class_name": class_name, "execution_time": exec_time, "time_unit": time_unit}
            else:
                data = class_name, exec_time, time_unit
            if save_path:
                saver(save_path, class_name, exec_time, time_unit)
            return data
        return wrapper
    return decorator

def saver(location: str, class_name: str, exec_time: float or int, time_unit: str):
    with open(location, 'a+') as f:
        f.write(f"{class_name}: {exec_time:.2f} {time_unit}\n")

