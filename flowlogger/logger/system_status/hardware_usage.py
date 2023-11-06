import psutil
import time
from threading import Thread

class RealTimeCPUUsage:
    def __init__(self, interval: int=1, 
                 print_output: bool=True,
                 save_path: str=''):
        """
        Initialize the RealTimeCPUUsage class.

        Parameters:
        interval(int): The interval in which the average appearance will be evaluated.
        print_output(bool): If True, the CPU usage will be printed to the console.
        save_path(str): If not empty, the CPU usage will be saved to the specified file.
        """
        self.interval = interval
        self.print_output = print_output
        self.save_path = save_path
        self.running = False
        self.thread = None

    def start(self):
        """
        Start the real-time CPU usage monitoring.
        """
        self.running = True
        self.thread = Thread(target=self._monitor_cpu_usage)
        self.thread.start()

    def _monitor_cpu_usage(self):
        """
        Monitor the CPU usage in real-time.
        """
        while self.running:
            cpu_usage = psutil.cpu_percent(interval=self.interval)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            if self.print_output:
                print(f'CPU Usage: {cpu_usage} % at {current_time}')
            if self.save_path:
                with open(self.save_path, 'a') as f:
                    f.write(f'CPU Usage: {cpu_usage} % at {current_time}\n')
            time.sleep(self.interval)

    def stop(self):
        """
        Stop the real-time CPU usage monitoring.
        """
        self.running = False
        if self.thread is not None:
            self.thread.join()
    
    @staticmethod
    def current(interval: int=1):
        """
        Get the current CPU usage.

        Parameters:
        interval(int): The interval in which the average appearance will be evaluated.
        
        Returns:
        float: The current CPU usage in percent.

        Usage:
        ```python
        usage = RealTimeCPUUsage()
        usage.current(interval=1)
        ```
        """
        return psutil.cpu_percent(interval=interval)
