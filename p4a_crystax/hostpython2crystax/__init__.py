from pythonforandroid.toolchain import Recipe


class Hostpython2Recipe(Recipe):
    version = '2.7'
    name = 'hostpython2crystax'
    conflicts = ['hostpython3','hostpython2','hostpython3crystax']

    def build_arch(self, arch):
        self.ctx.hostpython = '/usr/bin/false'
        self.ctx.hostpgen = '/usr/bin/false'


def get_recipe():
    return (Hostpython2Recipe(), __file__)
