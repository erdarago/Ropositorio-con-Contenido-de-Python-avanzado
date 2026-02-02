from typing import Dict

class Wallet:
    def __init__(self, input_data: Dict):
        self.data = input_data

    def compound(self, time: int, instrument: str) -> float:
        finaData = self.data["finData"]
        s = finaData["savings"]
        i = finaData["investingInstruments"][instrument]
        return s * (1 + i) ** time