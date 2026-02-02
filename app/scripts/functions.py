#recive un nombre
def greeting(name : str) -> str:
    if name == None:
        pass
    else:
        print(f"Hello {name}")

def getName() -> str:
    name = input("Enter your name: ")
    if len(name) == 0:
        print("Name cannot be empty")
        return None
    return name