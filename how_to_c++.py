# import subprocess
#
#
# # exe_output = subprocess.Popen('hello_world.exe', stdout=subprocess.PIPE)
# exe_output = subprocess.Popen(r'C:\Users\tosun\Desktop\hello_c\hello_fromBerk.exe', stdout=subprocess.PIPE)
# std_out, _ = exe_output.communicate()
# std_out = std_out.decode('utf-8')
# print(std_out)
#
# print('done.')


from ctypes import cdll

lib = cdll.LoadLibrary(r'C:\Users\tosun\Desktop\hello_c\testclass.so')

class Greeter:
    def __init__(self):
        self.obj = lib.Greeter_new()

    def greet(self):
        lib.Greeter_greet(self.obj)

    def show_num(self, num):
        lib.Greeter_show_num(self.obj, num)

    def show_nums(self, num1, num2):
        lib.Greeter_show_nums(self.obj, num1, num2)

    def sum(self, num1, num2):
        lib.Greeter_sum(self.obj, num1, num2)


    # def sum_r(self, num1, num2):
    #     return lib.Greeter_sum_r(self.obj, num1, num2)

G = Greeter()
G.greet()
G.show_num(152)
G.show_nums(15, 1232)
G.sum(6, 4)
# k = G.sum_r(3,4)
# print(k)

