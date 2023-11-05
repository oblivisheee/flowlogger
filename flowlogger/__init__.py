from flowlogger.logger.length_time.length_time_class import flclass
from flowlogger.logger.system_status.hardware_usage import RealTimeCPUUsage
from flowlogger.logger.system_status.ram_status import RAM_Info

def getvram(info_type: str='all', 
                          data_type: str='gb',
                          return_dict: bool=True):
    RAM_Info.get_gpu_vram_info(info_type=info_type, data_type=data_type, return_dict=return_dict)

def getram(info_type: str='all',
                    data_type: str='gb',
                    return_dict: bool=True):
    return RAM_Info.get_ram_info(info_type=info_type, data_type=data_type, return_dict=return_dict)
