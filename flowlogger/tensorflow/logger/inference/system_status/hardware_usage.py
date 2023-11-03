import psutil
import time
from threading import Thread

class RealTimeCPUUsage:
    """
    This class is used to get the real-time CPU usage.
    """
    def __init__(self, interval=1, print_output=True):
        self.interval = interval
        self.print_output = print_output
        self.running = False
        self.thread = None

    def start(self):
        """
        This function starts the real-time CPU usage monitoring.
        """
        self.running = True
        self.thread = Thread(target=self._monitor_cpu_usage)
        self.thread.start()

    def _monitor_cpu_usage(self):
        while self.running:
            cpu_usage = psutil.cpu_percent(interval=self.interval)
            if self.print_output:
                print(f'CPU Usage: {cpu_usage} %')
            time.sleep(self.interval)

    def stop(self):
        """
        This function stops the real-time CPU usage monitoring.
        """
        self.running = False
        if self.thread is not None:
            self.thread.join()
    
    @staticmethod
    def current(interval: int):
        """
        This function returns the current CPU usage.

        Parameters:
        interval(int): The interval in which the average appearance will be evaluated.
        
        Returns:
        float: The current CPU usage in percent.
        """
        return psutil.cpu_percent(interval=interval)

# Example usage:
cpu_usage_monitor = RealTimeCPUUsage(interval=2, print_output=True)
cpu_usage_monitor.start()
time.sleep(10)
cpu_usage_monitor.stop()
# To stop the monitoring, call the stop method.
# cpu_usage_monitor.stop()
# To get the current CPU usage, call the current method.
# current_cpu_usage = cpu_usage_monitor.current(interval=1)

