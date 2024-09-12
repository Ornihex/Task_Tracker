Yeah, it's just another cli task tracker.

https://roadmap.sh/projects/task-tracker

How to install:
1) download https://github.com/Ornihex/Task_Tracker/releases
2) `pip install <path to task_tracker.tar.gz>`

How to use:

Add a new task
```
task-cli add <description of your task>
```

Update the task
```
task-cli update <ID of task> <New description>
```

Update the task status
```
task-cli mark-in-progress <ID>
task-cli mark-done <ID>
task-cli mark-todo <ID>
task-cli mark todo <ID>
task-cli mark done <ID>
task-cli mark in-progress <ID>
task-cli mark <Custom status> <ID>
```

Delete the task
```
task-cli delete <ID>
```

Listing all tasks
```
task-cli list
```

Listing task by status
```
task-cli <status>
```
