class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                stop_val = input('Input value ')
                if stop_val == "stop":
                    print(f'Final list: {self.my_list}')
                    quit()
                val = int(stop_val)
                self.my_list.append(val)
                print(f'Current list: {self.my_list} \n ')
            except ValueError:
                print(f"Invalid value! Try again \n ")


try_except = Error()
print(try_except.my_input())
