from flowlogger.logger.training.length_time.length_time_class import flclass
from flowlogger.logger.inference.system_status.hardware_usage import RealTimeCPUUsage
from flowlogger.logger.inference.system_status.ram_status import RAM_Info

def get_gpu_vram_info(info_type: str='all', 
                          data_type: str='gb'):
    RAM_Info.get_gpu_vram_info(info_type=info_type, data_type=data_type)

def get_ram_info(info_type: str='all',
                    data_type: str='gb'):
    return RAM_Info.get_ram_info(info_type=info_type, data_type=data_type)
