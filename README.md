# task-cli

This a task cli app that allows you to track your progress doing tasks along the day
If the code is massy just keep in mind that i'm still learning to code
# project idea
i got this idea from this site https://roadmap.sh/projects/task-tracker 
# Adding a new task
python3 task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python3 task-cli update 1 "Buy groceries and cook dinner"
python3 task-cli delete 1

# Marking a task as in progress or done
python3 task-cli mark-in-progress 1
python3 task-cli mark-done 1

# Listing all tasks
python3 task-cli list

# Listing tasks by status
python3 task-cli list done
python3 task-cli list todo
python3 task-cli list in-progress