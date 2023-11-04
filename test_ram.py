from flowlogger import get_ram_info, flclass
@flclass("Test", save_path='test.log')
def test():
    ram_info = get_ram_info(info_type='used', return_dict=False)
    print(ram_info)

test()