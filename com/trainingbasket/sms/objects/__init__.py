class Runner(object):
    def printMenu(self):
        print("MAIN MENU")
        print("1. To add a student")
        print("2. To show all students")
        print("3. To exit")
    def add(self):
        print("calling add")
    def show(self):
        print("calling show")
    def asdf(self):
        pass
    switcher = {
        1: add,
        2: show,
        4: asdf
    }
    def execute(self):
        option = 100;
        while option != 3:
            self.printMenu()
            option = int(input("Please Enter Your Choice"))
            ref =self.switcher.get(option, lambda: "Invalid option")
            ref()

if __name__ == '__main__':
    ref=Runner()
    ref.execute()