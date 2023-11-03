import GPUtil
import psutil

class RAM_Info():
    """
    This class is used to get the RAM and GPU VRAM information.
    """

    @staticmethod
    def get_gpu_vram_info(info_type='all', 
                          data_type='gb'):
        """
        This function returns the GPU VRAM information.
        
        Parameters:
        info_type (str or list): The type of information to return. If 'all', returns all information. If a list, returns only the information specified in the list.
        data_type (str): The type of data computations. Two types: 'gb' - gigabytes, 'mb' - megabytes.
        
        Returns:
        list: A list of dictionaries containing the GPU VRAM information.
        """
        gpus = GPUtil.getGPUs()
        gpu_info = []

        if data_type == 'gb':
            count_data = 3
        else:
            count_data = 2

        for gpu in gpus:
            gpu_data = {
                'gpuid': gpu.id,
                'name': gpu.name,
                'total': gpu.memoryTotal / (1024 ** count_data),  # Convert to GB
                'used': gpu.memoryUsed / (1024 ** count_data),  # Convert to GB
                'free': gpu.memoryFree / (1024 ** count_data)  # Convert to GB
            }
            if info_type != 'all':
                if isinstance(info_type, list):
                    gpu_data = {key: gpu_data.get(key) for key in info_type if key in gpu_data}
                elif info_type in gpu_data:
                    gpu_data = {info_type: gpu_data.get(info_type)}
                else:
                     print(ValueError(f"Invalid info_type: {info_type}. Valid options are 'all', 'gpuid', 'name', 'total', 'used', 'free'.\nInitialization will continue, but output of data about RAM wont be."))
            gpu_info.append(gpu_data)

        if not gpu_info or all(not info.strip() for info in gpu_info):
            return None

        return gpu_info
    
    @staticmethod
    def get_ram_info(info_type='all', data_type='gb'):
        """
        This function returns the RAM information.
        
        Parameters:
        info_type (str or list): The type of information to return. If 'all', returns all information. If a list, returns only the information specified in the list.
        data_type (str): The type of data computations. Two types: 'gb' - gigabytes, 'mb' - megabytes.

        Returns:
        dict: A dictionary containing the RAM information.
        """
        if data_type == 'gb':
            count_data = 3
        else:
            count_data = 2
        ram = psutil.virtual_memory()
        ram_info = {
            'total': ram.total / (1024 ** count_data),  # Convert to GB
            'used': ram.used / (1024 ** count_data),  # Convert to GB
            'free': ram.free / (1024 ** count_data)  # Convert to GB
        }
        if info_type != 'all':
            if isinstance(info_type, list):
                ram_info = {key: ram_info.get(key) for key in info_type if key in ram_info}
            elif info_type in ram_info:
                ram_info = {info_type: ram_info.get(info_type)}
            else:
                print(ValueError(f"Invalid info_type: {info_type}. Valid options are 'all', 'total', 'used', 'free'.\nInitialization will continue, but output of data about VRAM wont be."))
                return None
        return ram_info
    
print(RAM_Info.get_gpu_vram_info(['total', 'used'], data_type='mb'))