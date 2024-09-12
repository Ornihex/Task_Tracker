Yeah, it's just another cli task tracker.

How to install:
1) download https://github.com/Ornihex/Task_Tracker/releases
2) `pip install <path to task_tracker.tar.gz>`

How to use:

Add a new task
```
task_cli add <description of your task>
```

Update the task
```
task_cli update <ID of task> <New description>
```

Update the task status
```
task_cli mark-in-progress <ID>
task_cli mark-done <ID>
task_cli mark-todo <ID>
task_cli mark todo <ID>
task_cli mark done <ID>
task_cli mark in-progress <ID>
task_cli mark <Custom status> <ID>
```

Delete the task
```
task_cli delete <ID>
```

Listing all tasks
```
task_cli list
```

Listing task by status
```
task_cli <status>
```
