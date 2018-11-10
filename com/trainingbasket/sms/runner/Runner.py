from com.trainingbasket.sms.objects.Students import Student
from com.trainingbasket.sms.service.StudentServices import StudentService
from  com.trainingbasket.sms.objects.StudentsExcel import ExcelStudents
from com.trainingbasket.sms.service.EmailService.GmailMailer import GmailMailer
class Runner(object):
    def printMenu(self):
        print("MAIN MENU\n1. To add a student\n2. To show all students\n3. To print all students\n4. To exit")


    def add(self):
        self.serv=StudentService()
        obj=ExcelStudents(name=input('Please Enter The student Name'),
            age=int(input('please enter the age')),
            contactnumber=input("please enter the contact number "),
            emailaddress=input("please enter the email address")
        )
        mailer=GmailMailer()
        mailer.sendMail(obj.emailaddress,"Employee Resitration ","Welcome {} you are welcomed on board we are very excited as you joined us in the peaktime of years\n"
                                         "Your Employee iD is {}".format(obj.name,obj.sIdCtr))
        self.serv.addStudent(obj)


    def show(self):
        self.serv.printAllStudents()
    def asdf(self):
        self.serv.printAllStudentsToFile('d:\\bhaskar')
    switcher = {
        1: add,
        2: show,
        3: asdf
    }
    def execute(self):
        option = 100;
        while option != 4:
            self.printMenu()
            option = int(input("Please Enter Your Choice"))
            ref =self.switcher.get(option, lambda: "Invalid option")
            ref(self)

if __name__ == '__main__':
    ref= Runner()
    ref.execute()
