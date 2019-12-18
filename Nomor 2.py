with open('data.txt','r') as f:
    data = f.read()
    employee = {}
    data = data.replace('\n', ',')
    data = data.split(',')
    
  
        



    
    
    
    
    
# def Menu():
#     program_menu = input('1. New Staff\n2. Delete Staff\n3. View Summary Data\n4. Save & exit \n')
#     while True:
#         if program_menu == 1:

#         elif program_menu == 2:
        
#         elif program_menu == 3:
#             viewSummaryData()
#             Menu()


#         elif program_menu == 4:

#         else:
#             warning = input('error, do you want to exit?(y/n) ')
#             if warning == y:
#                 exit()
#             else:
#                 Menu()

    class staff :
        def __init__(self,id,name,position,salary):
            self.id = id
            self.name = name
            self.position = position
            self.salary = salary
        def addStaff(self,id,name,position,salary):
            add_id = input('Input ID: ')
            if id[0] == 'S':
                if add_id not in employee:
                    add_name = input('Input Name:')
                    add_position = input('Input Position: ')
                    add_salary = input('Input Salary: ')
                    if add_position == 'staff':
                        if add_salary < 3500000 or salary > 7000000:
                            print(error)
                            Menu()
                    if add_position == 'Officer':
                        if add_salary < 7000001 or add_salary > 10000000:
                            print(error)
                            Menu()
                    if add_position == 'Manager':
                        if add_salary < 10000000:
                            print(error)
                            Menu()
            


        
    #     def deleteStaff(self,id,name,position,salary):
    #         if id in employee:
    #             del employee[id]
    #             print('Data has been sucessfully deleted')
def viewSummaryData():
    print('1. Staff\nMinimum Salary: 4500000\nMaximum Salary: 5000000\nAverage Salary: 4750000)
    print('\n2. Officer\nMinimum Salary: 8500000\nMaximum Salary: 8500000\nAverage Salary: 8500000)
    print('\n3. Manager\nMinimum Salary: 10700000\nMaximum Salary: 10700000\nAverage Salary: 10700000)



            