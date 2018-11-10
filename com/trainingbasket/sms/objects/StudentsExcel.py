from com.trainingbasket.sms.objects.Students import Student

class ExcelStudents(Student):

    def __init__(self,name, age, contactnumber,emailaddress):
        super(ExcelStudents, self).__init__(name=name,age=age,contactnumber=contactnumber)
        self.emailaddress=emailaddress

    def __str__(self):
        return "{},{},{},{},{}\n".format(self._name,self._age,self._contactnumber,self._studetid,self.emailaddress)
