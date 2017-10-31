from pythonforandroid.toolchain import Recipe


class Hostpython3Recipe(Recipe):
    version = '3.5'
    name = 'hostpython3crystax'
    conflicts = [('hostpython2', 'hostpython2crystax', 'hostpython3')]

    def build_arch(self, arch):
        self.ctx.hostpython = '/usr/bin/false'
        self.ctx.hostpgen = '/usr/bin/false'


def get_recipe():
    return (Hostpython3Recipe(), __file__)
