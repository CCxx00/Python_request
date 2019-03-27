import threading

class f(object):
    def __init__(self):
        self.a=1

    def change_a(self,a):
        self.a=a

    def print_a(self):
        print(self.a)

def main():
    fun=f()
    t=threading.Thread(target=fun.change_a,args=(22222,))
    fun.print_a()
    t.start()
    fun.print_a()
    t=threading.Thread(target=fun.change_a,args=(22,))
    t.start()
    fun.print_a()

if __name__=='__main__':
    main()
