class Employee:
    def __init__(self,empid,name,age,salary):
        self.empid=empid
        self.name=name
        self.age=age
        self.salary=salary

class commands:
    def __init__(self):
        self.emp=[]
    
    def add(self,x):
        self.emp.append(x)
    
    def search(self,choice):
        res=[]
        if choice==1:
            in_age=int(input("Enter Age: "))
            for i in self.emp:
                if i.age==in_age:
                    res.append(i)
            return res
        elif choice==2:
            in_name=input("Enter Name: ").lower()
            for i in self.emp:
                if (i.name).lower()==in_name:
                    res.append(i)
            return res

        elif choice==3:
            in_op=input("Enter Operator (<,>,<=,>=): ")
            salary=float(input("Enter Salary: "))
            for i in self.emp:
                if in_op=="<" and i.salary<salary:
                    res.append(i)
                elif in_op==">" and i.salary>salary:
                    res.append(i)
                elif in_op=="<=" and i.salary<=salary:
                    res.append(i)
                elif in_op==">=" and i.salary>=salary:
                    res.append(i)
            return res
        
    def display(self,res):
        if res:
            for i in res:
                print(f"Employee ID: {i.empid}    Name: {i.name}    Age: {i.age}    Salary: {i.salary}")
        else:
            print("No records exist")

        
def main():
    cmd=commands()
    cmd.add(Employee("161E90", "Raman", 41, 56000))
    cmd.add(Employee("161F91", "Himadri", 38, 67500))
    cmd.add(Employee("161F99", "Jaya", 51, 82100))
    cmd.add(Employee("171E20", "Tejas", 30, 55000))
    cmd.add(Employee("171G30", "Ajay", 45, 44000))


    print("Select option:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    ch=int(input("Enter Choice:"))
    if ch not in [1,2,3]:
        print("Wrong Choice!!!!")
    else:
        res=cmd.search(ch)
        cmd.display(res)

if __name__=="__main__":
    main()