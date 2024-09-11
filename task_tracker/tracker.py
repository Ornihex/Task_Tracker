from json import dump, load
from os.path import isfile
from datetime import datetime
class Tracker():
    def __init__(self):
        self.check = isfile('tasks.json')
        with open('tasks.json', f'{"r+" if self.check else "w+"}') as file:
            if not self.check:
                dump({}, file, indent=4)
        self.date = datetime.now()
        self.date = f'{self.date.day}.{self.date.month if self.date.month>9 else "0"+str(self.date.month)}.{self.date.year} {self.date.hour}:{self.date.minute}'
    def add(self, task):
        with open("tasks.json", 'r+') as t:
            data = load(t)
            data[len(data)+1] = {
                'id': len(data)+1,
                'description': f"{task}",
                'status': 0,
                'createdAt': self.date,
                'updatedAt': self.date
            }
            t.seek(0)
            dump(data, t, indent=4)
            print(f'Task added succesfully (ID: {len(data)})')
    def update(self, id, text):
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if len(data) >= id:
                data[id]['description'] = str(text)
                data[id]['updatedAt'] = self.date
                t.seek(0)
                dump(data, t, indent=4)
            else:
                print('There is no task with this ID')
    def mark(self, id, status):
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if len(data) >= id:
                data[id]['status'] = status
                data[id]['updatedAt'] = self.date
                t.seek(0)
                dump(data, t, indent=4)
            else:
                print('There is no task with this ID')
    def delete(self, id):
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if id in data:
                data.pop(id)
                t.seek(0)
                dump(data, t, indent=4)
            else:
                print('There is no task with this ID')
    def listing(self, status=None):
        with open('tasks.json', 'r+') as t:
            data = load(t)
            if not status:
                for i in data:
                    print(f'ID: {data[i]['id']} Status: {data[i]['status']} Description: {data[i]['description']}')