from lookup import lookup

class logicizer:
    'Handles the business logic of comparing inputs and deciding on the output.'
    def __init__(self):
        self.output = "Welcome to Jorts's Bomb Defusal Tool"
        self.table = lookup()

    def get_output(self):
        return self.output

    def evaluate(self, input_str):
        self.output = self.table.lookup(input_str)
