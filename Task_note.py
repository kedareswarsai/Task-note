my_tasks=[]

my_choice=None 
while True:
  my_choice=int(input("1.add tasks\n2.remove tasks\n3.replace tasks\n4.show all tasks\n5.exit\nenter choice(1,2,3,4,5):"))  
  if my_choice ==5:
      break
  match my_choice:

    case 1:

           task=input("enter task:")
           my_tasks.append(task)
           
    case 2:
           
           no=int(input("enter the sr.no of choice   you want to remove:"))
           if 1 <= no <= len(my_tasks):
             print("removed the task no ",no)
             my_tasks.pop(no-1)

             
           else:
               print("not present ! invalid value ")  
            
    case 3:            
    
           no=int(input("enter the sr.no of choice   you want to replace:"))    
           if 1 <= no <= len(my_tasks):
             task = input("Enter task: ")
             my_tasks[no-1] = task
             print("Successfully replaced with new task.")
           else:
             print("Not present! Invalid value.")

    case 4:
           if my_tasks != []:
             for i in  range(len(my_tasks)):
               print(i+1,")",my_tasks[i])
           else:
               print("no tasks added") 
               
    case 5:break           
              
                      
              
    