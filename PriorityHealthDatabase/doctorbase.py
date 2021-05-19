
import time
from user_prompt import Prompt
from hashmap import HashMap

class Interface:
    
    user_database = HashMap(10)

    def runtime(self):
        self.intro()
        
        running = True 
        while running:
            prompt3 = input()

            if prompt3 == "1":
                hospital_name = input("Please enter the name of your hospital: ")
                self.user_database.setter(hospital_name, Prompt())
                print('\n')
                

            elif prompt3 == "2":
                hospital_name = input("Please enter the name of your hospital: ")

                checker = False 
                for i in self.user_database.array:
                    if i == None:
                        continue
                    elif i[0] == hospital_name:
                        checker = True 
                        break 
                
                if checker != True:
                    print('The hospital does not seem to be registered under this runtime')
                    print('\n')
                else:
                    self.user_database.delete(hospital_name)
                    print('\n')

            elif prompt3 == "3":
                None_checker = False 
                counter = 0

                for i in self.user_database.array:
                    if i == None:
                        counter += 1
                
                if counter == len(self.user_database.array):
                    print('Your database is empty')
                    print('\n')
                else:
                    for i in self.user_database.array:
                        if i == None:
                            pass
                        else:
                            print(i[0])

                print('\n')

            elif prompt3 == "4":
                hospital_name = input("Please enter the name of your hospital: ")
                
                checker = False 
                for i in self.user_database.array:
                    if i == None:
                        continue 
                    elif i[0] == hospital_name:
                        checker = True 
                        break 

                if checker != True:
                    print('The hospital does not seem to be registered under this runtime')
                    print('\n')
                else:
                    hospital = self.user_database.getter(hospital_name)
                    print(hospital.intro())
                    time.sleep(0.2)
                    print('\n')

            elif prompt3 == "/quit":
                print('You have quit the software ')
                break 

            else:
                print("That input does not seem to be valid ")
                print('\n')




    def intro(self):
        print("-"*6)
        print('Welcome to your personal patient database')
        time.sleep(0.2)
        print('You have three options: ')
        time.sleep(0.2)
        print("1: You can add a hospital you work in to keep track of your patients \n")
        print("2: You can delete a hospital that you do not need \n")
        print("3: You can view all your hospitals under your runtime \n")
        print("4: You can acess your patient's database from a specific hospital \n")
        print("/quit: Quit the program \n")
        print("-"*6)
        time.sleep(0.2)
        print("Please select one of the options stated \n")


            

runtime = Interface()

print(runtime.runtime())
        

        