from MarksheetBean import Marksheet
from MarksheetDAO import MarksheetDao

class TestMarksheetDao:
    def TestAdd():
        # create the bean object
        m=Marksheet()
        # set all the values Directly:-
        # m.setRoll_no(7)
        # m.setName("Pavan")
        # m.setPhysics(50)
        # m.setChemistry(51)
        # m.setMaths(52)

        #set all the values from user input:-
        # m.setRoll_no(input("Enter Roll No :\n"))
        m.setName(input("Enter Name :\n"))
        m.setPhysics(input("Enter Physics Score :\n"))
        m.setChemistry(input("Enter Chemistry Score :\n"))
        m.setMaths(input("Enter Maths Score :\n"))  

        # DAO object
        model=MarksheetDao()
        # call the Add method
        model.Add(m)

# calling the Add
# TestMarksheetDao.TestAdd()

    def TestUpdate():
        m=Marksheet()
        m.setRoll_no(input("Enter Roll No whose Update Value : "))
        m.setName(input("Enter Name to Update : "))
        
        model=MarksheetDao()
        model.Update(m)

# TestMarksheetDao.TestUpdate()

    def TestDelete():
        m=Marksheet()
        m.setRoll_no(input("Enter Roll No to Delete : "))

        model=MarksheetDao()
        model.Delete(m)
# TestMarksheetDao.TestDelete()

    def TestGet():
        m=Marksheet()
        m.setRoll_no(input("Enter Roll No to Get Data : "))

        model=MarksheetDao()
        model.Get(m)
# TestMarksheetDao.TestGet()

    def TestMeritList():
        model=MarksheetDao()
        model.getMeritList()
# TestMarksheetDao.TestMeritList()

    def TestSearch():
        model=MarksheetDao()
        model.Search()
TestMarksheetDao.TestSearch()