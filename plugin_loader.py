import importlib.metadata
import importlib.util

import idaapi
import ida_loader


ENTRY_POINT_GROUP = "idapython"


def find_entry_points() -> importlib.metadata.EntryPoints:
    return importlib.metadata.entry_points().select(group=ENTRY_POINT_GROUP)


def get_plugin_path(module: str):
    spec = importlib.util.find_spec(module)
    return spec.origin


def message(*messages):
    for msg in messages:
        for line in msg.splitlines():
            idaapi.msg("[PluginLoader] {}\n".format(line))


class PluginLoader(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "Plugin Loader"
    help = "Plugin Loader"
    wanted_name = "PluginLoader"
    wanted_hotkey = ""

    def init(self):
        for ep in find_entry_points():
            plugin_path = get_plugin_path(ep.module)
            ida_loader.load_plugin(plugin_path)
            message(f"Loaded {ep.name} from {plugin_path}")
        return idaapi.PLUGIN_SKIP

    def term(self):
        pass

    def run(self, arg):
        pass


def PLUGIN_ENTRY():
    return PluginLoader()
