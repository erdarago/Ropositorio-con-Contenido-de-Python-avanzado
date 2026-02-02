from app.scripts.functions import greeting, getName
from app.models.objects import Wallet

if __name__ == "__main__":
    name = getName()
    greeting(name)

data ={
    'name': name,
    'finData': {
        "savings": 10000,
        "investingInstruments": {
            "BOND": 0.08
        }
    }
}

w = Wallet(input_data = data)

print(w.data)
print(w.compound(10, "BOND"))