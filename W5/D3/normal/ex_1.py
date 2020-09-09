class Currency():
    def __init__(self, C_label, value):
        self.C_label = C_label
        self.value = float(value)
    
    def __add__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value + other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value = self.value + other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self

    def __iadd__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value += other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value += other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self

    def __sub__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value - other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value = self.value - other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self

    def __isub__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value -= other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value -= other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self
    
    def __mul__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value * other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value = self.value * other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self

    def __imul__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value *= other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value *= other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self

    def __truediv__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value / other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value = self.value / other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self

    def __itruediv__(self, other):
        try:
            if isinstance(other, (int, float)):
                self.value /= other
            elif isinstance(other, Currency):
                if self.C_label == other.C_label:
                    self.value /= other.value
                else:
                    print("OOPS the currencies are not the same")
        except ValueError:
            raise ValueError
        return self
        

 # Write a program that prints the list of methods for any type of objects.
def get_methods(object):
    object_methods = [method_name for method_name in dir(object)
        if callable(getattr(object, method_name))]
    return object_methods


def main():
    euro = Currency("euro", 25)
    euro2 = Currency("euro", 20)
    dollar = Currency("dollar", 25)
    euro = euro + dollar
    # print(euro.value)
    # print(euro+euro2)
    # euro = euro + 5
    # print(dollar.C_label ==  euro.C_label)
    # euro += euro2
    print(euro.value)
    euro *= euro2
    print(euro.value)
    # euro = euro * euro2
    # print(euro.value)
    # euro = euro / euro2
    # print(euro.value)
    # euro /= euro2
    # print(euro.value)
    # print(get_methods(Currency))



if __name__ == '__main__':
    main()
