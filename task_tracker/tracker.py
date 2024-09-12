from json import dump, load
from os.path import isfile
from datetime import datetime
class Tracker():
    def __init__(self):
        self.check = isfile('tasks.json')
        with open('tasks.json', f'{"r+" if self.check else "w+"}') as file:
            if not self.check:
                dump({"total": 0}, file, indent=4)
        self.date = datetime.now()
        self.date = f'{self.date.day}.{self.date.month if self.date.month>9 else "0"+str(self.date.month)}.{self.date.year} {self.date.hour}:{self.date.minute}'
    def add(self, task):
        with open("tasks.json", 'r+') as t:
            data = load(t)
            data['total'] += 1
            total = data['total']
            data[total] = {
                'id': total,
                'description': task,
                'status': 'todo',
                'createdAt': self.date,
                'updatedAt': self.date
            }
            t.seek(0)
            dump(data, t, indent=4)
            return f'Task added succesfully (ID: {total})'
    def update(self, id, text):
        global data
        data = {}
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if id in data:
                data[id]['description'] = text
                data[id]['updatedAt'] = self.date
                with open('tasks.json', 'w'):
                    pass
                t.seek(0)
                dump(data, t, indent=4)
                return 'Task updated succesfully!'
            else:
                return 'ERROR: There is no task with this ID'
    def mark(self, id, status):
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if id in data:
                data[id]['status'] = status
                data[id]['updatedAt'] = self.date
                with open('tasks.json', 'w') as r:
                    pass
                t.seek(0)
                dump(data, t, indent=4)
                return 'Task marked succesfully!'
            else:
                return 'ERROR: There is no task with this ID'
    def delete(self, id):
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if id in data:
                data.pop(id)
                with open('tasks.json', 'w'):
                    pass
                t.seek(0)
                dump(data, t, indent=4)
                return "Task deleted succesfully!"
            else:
                return 'ERROR: There is no task with this ID'
    def listing(self, status=None):
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if not status:
                for i in data:
                    if i == 'total':
                        continue
                    yield f'ID: {data[i]['id']} Status: {data[i]['status']} Description: {data[i]['description']}\n'
            else:
                for i in data:
                    if i == 'total':
                        continue
                    if data[i]['status'] == status:
                        yield f'ID: {data[i]['id']} Status: {data[i]['status']} Description: {data[i]['description']}\n'