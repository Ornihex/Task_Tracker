from json import dump, load, loads, dumps
from os.path import isfile
from datetime import datetime
class Tracker():
    def __init__(self):
        pass
    def add(self, task):
        date = datetime.now()
        if isfile('tasks.json'):
            with open("tasks.json", 'r+') as fh:
                data = load(fh)
                data[len(data)+1] = {
                    'id': len(data)+1,
                    'description': f"{task}",
                    'status': 0,
                    'createdAt': f'{date.day}.{date.month if date.month>9 else "0"+str(date.month)}.{date.year} {date.hour}:{date.minute}',
                    'updatedAt': f'{date.day}.{date.month if date.month>9 else "0"+str(date.month)}.{date.year} {date.hour}:{date.minute}'
                }
                fh.seek(0)
                dump(data, fh, indent=4)
                print(f'Task added succesfully (ID: {len(data)})')
        else:
            data = {
                    1: {
                    'id': 1,
                    'description': f'{task}',
                    'status': 0, # 0 - todo, 1 - in-progress, 2 - done
                    'createdAt': f'{date.day}.{date.month if date.month>9 else "0"+str(date.month)}.{date.year} {date.hour}:{date.minute}',
                    'updatedAt': f'{date.day}.{date.month if date.month>9 else "0"+str(date.month)}.{date.year} {date.hour}:{date.minute}'
                }
            }
            with open('tasks.json', 'w+') as t:
                dump(data, t, indent=4)
                print(f'Task added succesfully (ID: {len(data)})')
tracker = Tracker()
tracker.add(input())