import sys 
import psutil
import platform
import cpuinfo


cName =  cpuinfo.get_cpu_info()['brand_raw']
cores = psutil.cpu_count(logical=False)
logical_cores= psutil.cpu_count()

class system_info():
    
    def __init__(self):
        super().__init__()
        
    def cpu(self,name):
        if name == 'usage':
            usage = int(psutil.cpu_percent(interval=0.2))
            return usage
        else:
            return None
        

system = system_info()
"""
while True:

    print("CPU cores: ",system.cpu('cpu_core'))
    print("CPU Logical Cores: ", system.cpu('logical_cores'))
    print("Cpu Usage: ", system.cpu('usage'),"%")
""" 
    