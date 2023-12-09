class Params:
    def __init__(self,model) -> None:
        self.model = model

    def get(self):
        return self.model.get()

    def set(self,value):
        return self.model.set(value)