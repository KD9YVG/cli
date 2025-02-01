def setup():
    print('\033[H\033[J')
    print('Text editor 0.0.1 Alpha')
    print('-----------------------')
    dir = input('File name/path: ')
    try:
        f = open(dir, 'r+')
    except FileNotFoundError:
        f = open(dir, 'w+')
    except PermissionError:
        print('Permission denied.')
        return None
    return f

class editor:
    def __init__(self):
        self.f = setup()
        if self.f == None:
            return
        print(self.f.read())
        self.f.close()
    def close(self):
        self.f.close()
        return

f = setup()
print(f.read())
f.close()