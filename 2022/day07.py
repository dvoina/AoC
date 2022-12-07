class FSEntry(object):
    def __init__(self, name:str, type: str, parent = None):
        self.name = name
        self.type = type
        self.size = 0
        self.children:list[FSEntry] = None
        self.parent = parent

    def __repr__(self) -> str:
        return f"{self.type} {self.name}"

    def getSize(self):
        return 0

    def getPath(self):
        def _getPath(node:FSEntry):
            if node != None:
                return f"{_getPath(node.parent)}/{node.name}"
            else:
                return "/"
        
        return _getPath(self)


class Dir(FSEntry):
    def __init__(self, name:str, parent:FSEntry):
        FSEntry.__init__(self, name, "dir", parent)
        self.size = 0
        self.children = []

    def getSize(self):
        return sum([c.getSize() for c in self.children])



class File(FSEntry):
    def __init__(self, name:str, size:int, parent:FSEntry):
        FSEntry.__init__(self, name, "file", parent)
        self.size = size
        self.children = None
        
    def getSize(self):
        return self.size

data = [l.strip() for l in open("2022/day07.txt").readlines()]


def traverse(root:Dir, dirs=[], value=100000):
    for c in root.children:
        if c.type=="dir":
            traverse(c, dirs, value)
            dirs.append(c)


root = Dir('/', None)
cwd = root
idx = 0
cont = True
while cont:
    try:
        l = data[idx]
        if l.startswith('$'):
            if l == "$ cd /":
                cwd = root
                idx+=1
                continue
            if l == "$ cd ..":
                if cwd.parent != None:
                    cwd = cwd.parent
                else:
                    cwd = root 
                idx+=1
                continue
            if l == "$ ls":
                idx += 1
                try:    
                    while True:
                        l = data[idx]
                        if l.startswith("$"):
                            break
                        else:
                            l = l.split()
                            if l[0] == 'dir':
                                cwd.children.append(Dir(l[1], cwd))
                            else:
                                cwd.children.append(File(l[1], int(l[0]), cwd))                                
                            idx +=1
                except IndexError as e:
                    cont = False
                continue
            else:
                for c in cwd.children:
                    if c.type == "dir" and c.name == l.split()[2]:
                        cwd = c
                        break
                idx+=1
                continue
    except IndexError as e:
        cont = False

t=[]
traverse(root, t)
t = list(filter(lambda x: x.getSize()<=100000, t))
print(sum([x.getSize() for x in t]))

t=[]
traverse(root, t)

unused = 70000000 - root.getSize()
need = 30000000 - unused

t = [(x.getPath(), x.getSize()) for x in sorted(t, key=lambda x: x.getSize()) if x.getSize()>=need]
print(t[0])
