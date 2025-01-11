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

f = setup()
if f:
    print(f.read())

f.close()