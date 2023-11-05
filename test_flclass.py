import flowlogger as fl
import time
options = {
    'class_name': 'Test 1',
    'save_path': 'test.log',
}
@fl.flclass(options=options)
def test():
    ram_info = fl.getram(info_type='used', return_dict=False)
    print(ram_info)

test()