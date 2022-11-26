class node():
    def __init__(self, roam=None, scrub=None, leer=None):
        self.roam = roam
        self.scrub = scrub
        self.leer = leer


class main():
    def __init__(self):
        self.a = node(roam=(0, 'b'), scrub=(1, 'e'))
        self.b = node(scrub=(2, 'c'))
        self.c = node(scrub=(3, 'd'))
        self.d = node(leer=(6, 'f'), roam=(4, 'e'), scrub=(5, 'd'))
        self.e = node(roam=(7, 'f'))
        self.f = node(leer=(8, 'b'))
        self.current = self.a

    def roam(self):
        if self.current.roam is None:
            raise KeyError
        ans = self.current.roam[0]
        exec(f'self.current = self.{self.current.roam[1]}')
        return ans

    def scrub(self):
        if self.current.scrub is None:
            raise KeyError
        ans = self.current.scrub[0]
        exec(f'self.current = self.{self.current.scrub[1]}')
        return ans

    def leer(self):
        if self.current.leer is None:
            raise KeyError
        ans = self.current.leer[0]
        exec(f'self.current = self.{self.current.leer[1]}')
        return ans


o = main()
example = ['roam', 'scrub', 'roam', 'roam', 'leer', 'leer', 'leer', 'roam', 'leer', 'leer', 'leer', 'scrub', 'roam']
for i in example:
    exec(f'print(o.{i}())')