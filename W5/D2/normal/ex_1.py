class Family():
    def __init__(self, family_name, Members):
        self.family_name = family_name
        self.Members = Members

    def print_Family(self):
        for member in range(len(self.Members)):
            print(repr(self.Members[member]))

    def __repr__(self):
        repr_str = ""
        for key, value in Family.Members.items():
            repr_str += f"{key}: {value},"
        repr_str += "/n"
    

class Member(Family):
    def __init__(self, family_name, name, Members):
        super().__init__(family_name , Members)
        self.name = name

    def born(self, **kwargs):
        self.child = {}
        for key, value in kwargs.items():
            self.child.update({key: value})
        self.child.update({"age": 0})
        self.child.update({"is_child": True})
        
        print(
            f"Congrats to your new child! {self.child.get('name')} is a {self.child.get('gender')} !!!")
        return self.child

    def is_18(self, name):
        for k, v in self.Members.items():
            if k == "age" and v > 18:
                for k, v in self.Members.items():
                    if k == "name" and v == name:
                        return True
        return False
            

def main():
    Cohen = Family("Cohen", [])
    Michael = Member("Cohen","Michael", {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False}, )
    Cohen.Members.append(Michael)
    
    Sarah = Member("Cohen", "Sarah", {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False})
    Cohen.Members.append(Sarah)
    new_Child = Member("Cohen", "Julien", {'name': 'Julien', 'gender': 'male',})
    new_Child.born(name="Julien", gender="male")
    Cohen.Members.append(new_Child)
    Michael.is_18("Michael")
    # print(Cohen)
    


if __name__ == '__main__':
    main()
