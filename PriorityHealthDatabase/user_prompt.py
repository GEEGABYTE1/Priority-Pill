from rankings import prompt
from heap import MaxHeap
import time 



class Prompt:
    big_data_base = {}
    patient_database = {}
    queue = {}
    
    def intro(self):
        
        
        health_database = MaxHeap()

        running = True
        while running:
            time.sleep(0.3)
            print('-'*6)
            time.sleep(0.2)
            print("You have two options: \n")
            print('1: Insert a new medical condition you would like to sort by \n')
            print('2: View all of your patients based on priority \n')
            print('3: Add a patient to your database and queue')
            print('4: To remove the patient from your queue')
            print('/quit : to exit the database')
            print('/view_database: to see your medical issues registered in the software')
            print('-'*6)
            time.sleep(0.2)

            # Updated Controls
            print("Please type any one of the commands listed above: \n")
            ####

            prompt2 = input()

            if prompt2 == '1':
                self.add_new_issue()

            elif prompt2 == '2':
                cur_patients = []
                if health_database.count == 0:
                    print("You have no medical patients yet! ")
                else:
                    print("Here is the list of your medical patients: ")
                    for i in health_database.heap_list:
                        if i == None:
                            continue 
                        else:
                            for k,l in self.queue.items():
                                if l == i:
                                    if not k in cur_patients:
                                        cur_patients.append(k)
                
                for i in cur_patients:
                    print(i)

            elif prompt2 == '3':
                self.update_patient_database()
                time.sleep(0.1)
                patient_data = self.checker(list(self.patient_database)[health_database.count])
                try:
                    self.queue[patient_data[0]] = patient_data[-1]
                    health_database.insert_node(self.queue[patient_data[0]])
                except TypeError:
                    print()


            elif prompt2 == '4':
                if health_database.count == 0:
                    print("You do not have any patients yet ")
                else:
                    completed_patient = health_database.retrieve_min()
                    print('You have met: ')
                    
                    for i, j in self.queue.items():
                        if j == completed_patient:
                            print(i)
                            print("More info about the patient: \n")
                            info_patient = self.patient_database[i]
                            for k in range(len(info_patient)):
                                if k == 0:
                                    print('Age: {}'.format(info_patient[k]))
                                elif k == 1:
                                    print('Gender: {}'.format(info_patient[k]))
                                elif k == 2:
                                    print('Issue: {}'.format(info_patient[k]))
                                elif k == 3:
                                    print('Extra Info: {}'.format(info_patient[k]))    
                                print("\n")            
                    

            elif prompt2 == "/quit":
                print("You have quit the hospital's patient's database")
                break

            elif prompt2 == "/view database":
                print(self.big_data_base)

            else:
                print("That value does not seem to be valid... ")


    def updated_database(self, dict):
        for i, j in dict.items():
            self.big_data_base[i] = j 


    def update_patient_database(self):
        name = input('Please enter the patient\'s name: ')
        age = input('Please enter their age: ')
        gender = input('Please enter their gender: ')
        issue = input('Please enter an issue: ')
        extra_info = input('Please type any extra info: ')

        self.patient_database[name] = [age, gender, issue, extra_info]


    def checker(self, name):
        name_data = self.patient_database[name]
        issue = name_data[2]

        if issue in list(self.big_data_base.keys()):
            priority = self.big_data_base[issue]
            patient = [name, priority]
        else:
            print('\n')
            print('That issue of {name} does not seem to be registered in the database.'.format(name=name))
            time.sleep(0.1)
            print('We will be adding it to the database...')
            self.add_new_issue()
            try:
                priority = self.big_data_base[issue]
                patient = [name, priority]
                return patient 
            except KeyError:
                time.sleep(0.5)
                print('There has been an error processing that issue. Looks like you have entered two different issues for one patient at the same time.')
            


    def add_new_issue(self):
        new_entries = prompt()
        self.updated_database(new_entries)



        
        

        



#test = Prompt()

#print(test.intro())
        