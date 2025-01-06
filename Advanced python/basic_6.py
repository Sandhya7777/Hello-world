a = [1,2,3,4,5,6]
b = {"name":"Aritra", "title":"chakraborty"}

def fun_list(**kwargc):   #argc kwargc
    for k,v in kwargc.items():
        print(f"key and values are -> {k}  {v}")


# fun_list(name="Aritra", title="Chakraborty", pin=100101)


# decorator
def welcome(function):
    def display(name):
        return(f"Welcome to decorator {name} from {function.__name__}")
    return display


@welcome
def welcome_message(name):
    if name != 0:
        if type(name) == str():
            print("Working")
    return name

# print(welcome_message("Aritra"))

def add_data(fun):
    fun.data = 3
    return fun

@add_data
def add(x,y):
    return x+y - add.data

# print(add(3,5))
# print(add.data)


fun = lambda x,y: x+y
# print(fun(2, 4))

a = [1,2,3,4,5,6,7,8]
b = [2,4,6,8]

def short_list(lst):
    new_lst = []
    for i in lst:
        if i%2 == 0:
            new_lst.append(i)
    return new_lst

# print(short_list(a))

c = list(filter(lambda i: (i%2==0), a))
print(c)

d = {"name":"Aritra", "title":"chakraborty", "pin": 700102}

e = list(d.keys())
# f = [lambda k: k, a.keys()]
# print(f)

