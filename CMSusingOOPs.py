import pickle
class Customer:
    cuslist=[]
    def __init__(self):
        self.id=0
        self.age=0
        self.name=""

    def addcust(self):
        Customer.cuslist.append(self)

    def searchcust(self):
        for cus in Customer.cuslist:
            if(cus.id==self.id):
                self.age=cus.age
                self.name=cus.name
    def modifycust(self):
        for cus in Customer.cuslist:
            if(cus.id==self.id):
                cus.age=self.age
                cus.name=self.name

    def delcust(self):

        for e in Customer.cuslist:
            if(e.id==self.id):
                Customer.cuslist.remove(e)
                return
    def savetoPickle():
        f=open("D://rishav//picklefile.txt","wb")
        pickle.dump(Customer.cuslist,f)
        f.close()
    def loadfromPickle():
        f = open("D://rishav//picklefile.txt", "rb")
        Customer.cuslist=pickle.load(f)
        f.close()


#Presentation Layer
if(__name__=="__main__"):
    def displayall():
        for cus in Customer.cuslist:
            print("Customer ID:",cus.id, "Customer Age:",cus.age, "Customer Name:",cus.name)


    while(1):
        print("Press 1 to Add Customer")
        print("Press 2 to Delete Customer")
        print("Press 3 to Search Customer")
        print("Press 4 to Display All")
        print("Press 5 to Exit")
        print("Press 6 Save to Pickle")
        print("Press 7 Load from Pickle")
        c=int(input("Please Enter Your Choice : "))
        if(c==1): #Add Customer
            cus=Customer()
            cus.id=int(input("Enter Customer ID"))
            cus.age=int(input("Enter Customer Age"))
            cus.name=input("Enter Customer Name")
            cus.addcust()
        elif(c==2): #Delete Customer
            cus=Customer()
            cus.id=int(input("Enter Customer ID"))
            cus.delcust()
            print("Customer Deleted Successfully")
        elif(c==3): #Search Customer
            cus=Customer()
            cus.id=int(input("Enter Customer ID"))
            cus.searchcust()
            print("Cust ID:",cus.id,"Cust Name:",cus.name, "Cust Age:",cus.age)
        elif(c==4):
            displayall()
        elif(c==5):
            exit()
        elif (c == 6):
            Customer.savetoPickle()
        elif (c == 7):
            Customer.loadfromPickle()

