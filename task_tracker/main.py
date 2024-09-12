from .tracker import Tracker
from sys import argv

def main():
    tracker = Tracker()
    if argv[1] == 'add':
        print(tracker.add(argv[2]))
    elif argv[1] == 'update':
        print(tracker.update(argv[2], argv[3]))
    elif argv[1] == 'delete':
        print(tracker.delete(argv[2]))
    elif argv[1] == 'list':
        try:
            status = argv[2]
        except IndexError:
            status = None
        print(*tracker.listing(status))
    elif argv[1][:4] == 'mark':
        if len(argv[1])>5:
            mark = argv[1][5:]
            id = argv[2]
        else:
            try:
                mark = argv[2]
                id = argv[3]
            except IndexError:
                print("""You probably didn't specify a label or ID. Usage examples:
                                            mark-done <ID>
                                            mark done <ID>""")
        print(tracker.mark(id, mark))

if __name__ == '__main__':
    main()