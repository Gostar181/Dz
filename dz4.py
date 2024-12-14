class m:
    def __init__(self):
        self.name = "MMMMMMMMMMMMM"

class n:
    def __init__(self):
        self.name = "NNNNNNNNNNNNNN"

class b:
    def __init__(self):
        self.name = "BBBBBBBBBBBBBB"

class mnb(m,n,b):
    def __init__(self):
        m.__init__(self)
        n.__init__(self)
        b.__init__(self)

        print(self.name)
#