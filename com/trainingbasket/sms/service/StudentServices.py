class StudentService():
    listOfStudents=[]

    def addStudent(self, student):
        self.listOfStudents.append(student)

    def printAllStudents(self):
        if self.listOfStudents.count()!=0:
            for d in self.listOfStudents:
                print(d)
        else:
            print("There no data in stream")

    def printAllStudentsToFile(self, filepath):
        with open(filepath+".csv","w") as file:
            for student in self.listOfStudents:
                file.writelines(student.__str__())
                #print(student)




