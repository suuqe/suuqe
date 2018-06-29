import os
def run():
    print('In the directory lister module')
    files = os.listdir('.')
    return str(files)
