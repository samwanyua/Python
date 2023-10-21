#**kwargs

def hello(**kwargs):
    print("Hello ", end=" ")
    for key, value in kwargs.items():\
        print(value, end=" ")

hello(title="Mr.", first="Bro", middle="Code", last="Dude")
