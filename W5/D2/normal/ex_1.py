class Family():
    def __init__(self, family_name, Members):
        self.family_name = family_name
        self.Members = Members

    def print_Family(self):
        for member in range(len(self.Members)):
            print(repr(self.Members[member]))


class Member(Family):
    def __init__(self, family_name, name, Members):
        super().__init__(family_name , Members)
        self.name = name

        # for key, value in kwargs.items():
        #     if key == "name":
        #             self.name = value
        #     if key == "age":
        #         self.age = value
        #     if key == "gender":
        #         self.gender = value
        #     if key == "is_child":
        #         self.is_child = value

    def born(self, **kwargs):
        self.child = {}
        for key, value in kwargs.items():
            self.child.update({key: value})
        self.child.update({"age": 0})
        self.child.update({"is_child": True})
        self.Members.append(self.child)
        print(
            f"Congrats to your new child! {self.child.get('name')} is a {self.child.get('gender')} !!!")
        return self.child

    def is_18(self, name):
        for k, v in self.Members.items():
            if k == "age" and v > 18:
                print(v)
                if k == "name" and v == name:
                    print(f"{k} is an adult")
            

def main():
    Cohen = Family("Cohen", [])
    Michael = Member("Cohen","Michael", {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False}, )
    Cohen.Members.append(Michael)
    # Members = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False}, {
    #     'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}]
    # new_Child = Member("Cohen", "Julien", Members)
    # new_Child.born(name="Julien", gender="male")
    # Cohen.Members.append(new_Child)
    # Cohen.print_Family()
    # print(Cohen.Members)
    Michael.is_18("Michael")
    # print(new_Child.name)
    


if __name__ == '__main__':
    main()
