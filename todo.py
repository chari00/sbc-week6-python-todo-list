import time 
import json
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task(description):
    #initialize a placeholder to hold the task
    tasks = []
    try:
        #try to read the task.json file. 
        with open('task.json', 'r') as task_file:
            tasks = json.load(task_file)
    except:
        pass  
    # Create a new task - use max() built-in method in python to increment the id number
    new_id = max([task['id'] for task in tasks], default=0) + 1
    #set the structure on how the task will be appended.
    new_task = {'id': new_id, 'description': description, 'status': 'pending'}
    tasks.append(new_task)
    clear_screen()
    with open('task.json', 'w') as task_file:
        json.dump(tasks, task_file, indent=4)


def view_task():
    try:
        #open the task.json file in read mode
        with open('task.json', 'r') as task_file:
            #set the converted json dictionary to task
            tasks = json.load(task_file)
            print('\n')
            print(f'My Todo list:')
            for task in tasks:
                print(task)
    except Exception as e:
        print(e)

def update_task(task_id, new_description, new_status):
    try:
        #open the task.json file in read mode
        with open('task.json', 'r') as task_file:
            #load the existing json dictionary to tasks
            tasks = json.load(task_file)
        # Check if the task_id exists in the list
        # Find the task with the matching id using python built-in function next()
        task_to_update = next((task for task in tasks if task['id'] == task_id), None)
        if task_to_update: #check if the task id is existing/true
            # Update the value of the task
            task_to_update['description'] = new_description
            task_to_update['status'] = new_status
            print('updating...')
            time.sleep(1)
            print(f"Updated task: {task_to_update}")
            # Save updated tasks back to the JSON file
            with open('task.json', 'w') as task_file:
                json.dump(tasks, task_file, indent=4)

            time.sleep(1)
            print("Task updated successfully")
        else:
            print(f"No task found with id {task_id}")
            time.sleep(2)
            print("Updating failed.")
        time.sleep(2)
    
    except Exception as e:
        print(e)

def delete_task(task_id):
    try:
        #open the task.json file in read mode
        with open('task.json', 'r') as task_file:
            #load the existing json dictionary to tasks
            tasks = json.load(task_file)      
        # Find the task with the matching id using python build-in function next()
        task_to_delete = next((task for task in tasks if task['id'] == task_id), None)
        if task_to_delete: #check if the task id is existing/true
            # remove the task from the file
            tasks.remove(task_to_delete)
            print('deleting...')
            time.sleep(1)
            # Save updated tasks back to the JSON file
            with open('task.json', 'w') as task_file:
                json.dump(tasks, task_file, indent=4)

            time.sleep(1)
            print("Task deleted successfully")
        else:
            print(f"No task found with id {task_id}")
            time.sleep(2)
            print("Deletion failed.")
        time.sleep(2)
    
    except Exception as e:
        print(e)
  
print('Welcome to the To-Do List App')
print('Please choose an option.')

while True:
    print('1. Add a Task')
    print('2. View Tasks')
    print('3. Update a Task')
    print('4. Delete a Task')
    print('5. Exit')
    choices = input('Please enter the number of your chosen option: ')
    time.sleep(1)
    try:
        match choices:
            case '1':
                #function to write/ADD a task
                description = input('Write a task: ')
                print('Adding...')
                time.sleep(2)
                print('Task added')
                time.sleep(1)
                add_task(description)
                print('\n')
                                
            case '2':
                #function that read the task.json file
                view_task()
                print('\n')
                                   
            case '3':
                #function to edit/update the task.json file
                while True:
                    try:
                        task_id = int(input('Enter the id that you want to edit: '))
                        time.sleep(1)
                        break  # Exit the loop if input is valid
                    except:
                        print('Invalid id, please choose from the options above.')

                new_description = input('New task description: ').title()
                time.sleep(1)
                new_status = input('Enter task status: ').lower()
                update_task(task_id, new_description, new_status)
                print('\n')
                                   
            case '4':
                #function that delete the existing todo from task.json file
                while True:
                    try:
                        task_id = int(input('Enter the id that you want to delete: '))
                        time.sleep(1)
                        break  # Exit the loop if input is valid
                    except:
                        print('Invalid id, please choose from the options above.')
                delete_task(task_id)
                print('\n')
                    
            case '5':
                # exit the App using python exit command
                    print('Exiting the To-Do App...')
                    time.sleep(2)
                    print('Done.')
                    time.sleep(2)
                    sys.exit(0) #exit the program without any issue.
            case _:
                if choices <=5:
                    print('Enter a number from the choices.')
                
    except Exception as e:
        print('Invalid choice. Please enter a number from the choices.')
        print('\n')
        time.sleep(2)