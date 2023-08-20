def decorate_me(func):
    def inner_func(*args,**kwargs):
        print("i am the extra functionality")
        return func(*args,**kwargs)
    return inner_func

@decorate_me
def message(txt):
    return txt
print(message("hello world"))

@decorate_me
def message2(txt1,txt2,txt3="dafault"):
    return txt1+txt2+txt3
print(message2("hy","orld",txt3="im learning"))