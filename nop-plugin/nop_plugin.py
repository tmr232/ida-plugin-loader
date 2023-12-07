import idaapi

class NopPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "Nop Plugin"
    help = "Nop Plugin"
    wanted_name = "Nop Plugin"
    wanted_hotkey = ""

    def init(self):
        return idaapi.PLUGIN_KEEP

    def term(self):
        pass

    def run(self, arg):
        idaapi.msg("Hello, World!")


def PLUGIN_ENTRY():
    return NopPlugin()
