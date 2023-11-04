import time
from typing import Union, Dict

def flclass(class_name: str,
            return_dict: bool=True,
            save_path: str=None):
    """
    This is a decorator function that logs the execution time of a function and the class name.
    It takes a class name as an argument and returns a decorator.
    The decorator wraps the function, logs the start and end time, calculates the execution time,
    and returns the execution time and class name.
    
    Parameters:
    class_name (str): The name of the class.
    return_dict (bool): If true, return dict with data. Else, return variables: class_name, exec_time
    save_path (str): If provided, save the execution time and class name to this file path.

    Returns:
    Union[Dict[str, Union[str, float]], Tuple[str, float]]: Execution time and class name.

    Usage example:
    ```python
    @flclass("Greeting to the world")
    def world():
        print("Hello World!")

    world()
    ```
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            exec_time = end_time - start_time
            print(f"Execution time of part {class_name}: {exec_time} seconds")
            if return_dict:
                data = {"class_name": class_name, "execution_time": exec_time}
            else:
                data = class_name, exec_time
            if save_path:
                saver(save_path, class_name, exec_time)
            return data
        return wrapper
    return decorator

def saver(location: str, class_name: str, exec_time: float or int):
    with open(location, 'w') as f:
        f.write(f"{class_name}: {exec_time} seconds\n")

