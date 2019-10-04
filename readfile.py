import os


def read_file(path='/Users/imac/Desktop/test/images'):
    # path = '/Users/imac/Desktop/test/images'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        # print(r, d, f)
        for file in f:
            if '.jpg' in file:
                # files.append(os.path.join(r, file))
                files.append(os.path.join('images', file))

    return files

a = read_file()
for b in a:
    print(b)