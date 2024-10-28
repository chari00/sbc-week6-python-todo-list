
import json
import sys

def add_task(description):
    #initialize a placeholder to hold the task
    tasks = []
    try:
        #try to read the task.json file. 
        with open('task.json', 'r') as task_file:
            tasks = json.load(task_file)
    except:
        pass  
    # Create a new task - use max() build-in method in python to increment the id number
    new_id = max([task['id'] for task in tasks], default=0) + 1
    #set the structure on how the task will be appended.
    new_task = {'id': new_id, 'description': description, 'status': 'pending'}
    tasks.append(new_task)
    # Save updated tasks back to the JSON file
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
                # print('\n')
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
    try:
        choices == int(choices) 
        match choices:
            case '1':
                #function to write/ADD a task
                description = input('Write a task: ')
                add_task(description)
                print('\n')
                
            case '2':
                #function that read the task.json file
                view_task()
                    
            case '3':
                #write a function to edit/update the task.json file
                def update_task():
                    pass
            case '4':
                #write a function that delete the existing todo from task.json file
                def delete_task():
                    pass
            case '5':
                # exit the App using python exit command
                    print('Exiting the To-Do App...')
                    print('Done.')
                    sys.exit(0)
            # case _:
            #     print('Enter a number from the choices.')
    except Exception as e:
        print('Invalid choice. Please enter a number from the choices.')