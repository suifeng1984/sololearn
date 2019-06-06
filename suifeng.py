

# def m1():
#     print('this is from Suifeng module')
#
#
# if __name__ =='__main__':
#     m1()


""" *args  **kwargs的用法"""

def m1(*args):
    print(sum(args))

m1(2+3)
m1(1+6+9+8+8+65+5+5+5+5+98)

def someone(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)

someone(name='xiao hong',age=20)

someone(name = 'xiao hong',age=20,height=165)

