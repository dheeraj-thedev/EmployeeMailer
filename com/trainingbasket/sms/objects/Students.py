import datetime
class Student(object):
    sIdCtr = 0
    name = ""
    age = 0
    contactnumber = ""
    studetid = ""

    """This is student class basically to handle student data"""
    def __init__(self,name, age, contactnumber="3094932402"):
        if (str.strip(name) != "") & (age > 10) &(contactnumber != ""):
            self.name=name
            self.age=age
            self.contactnumber=contactnumber
            Student.sIdCtr=Student.sIdCtr+1
            self._studetid="{}/{}/{}/{}".format("TB",datetime.datetime.now().month,datetime.datetime.now().year,Student.sIdCtr)


    def __str__(self):
        return "The Student ID is {3}\n" \
               "The Name is{0}\n" \
               "The Age is {1}\n" \
               "The Contact Number is {2}\n" \
               "".format(self.name,self.age,self.contactnumber,self.studetid)
