# IDA Plugin Loader
## Why?

IDA provides a single way to install plugins. Just stick them under `plugins` and you're good to go.

While it works, the drawbacks are many.

1. You have to copy your plugins into the plugins directory. For Python plugins, this can get quite cumbersome;
2. Plugins often depend on multiple files. This has the tendency to clutter your `plugins` directory quite a bit;
3. The same plugins are loaded for all users and projects. This is not always desireable;
4. Adding a new plugin requires root access.

The plugin-loader plugin allows you to circumvent all those drawbacks.

## How?

Once installed (the old way) the `plugin_loader.py` plugin allows you to define plugin-lists. There are 3 types of lists - system-wide, user-specific, and project-specific. Listed plugins load automatically at the appropriate time.

### Plugin Lists

All plugin lists are named `plugins.list`, and look something like this:

```
C:\Plugins\my_plugin.py

# This is a comment. Comments are always entire lines.
C:\OtherPlugins\another_plugin.py
```

When IDA starts, both `my_plugin.py` and `another_plugin.py` will be loaded.

#### System-Wide

The system-wide list resides under IDA’s `cfg` subdirectory. The path can be found using `idaapi.idadir(idaapi.CFG_SUBDIR)`. This list requires root access to modify as it is in IDA’s installation directory.

#### User-Specific

Located in IDA’s user-directory. `$HOME/.idapro` on Linux, `%appdata/%HexRays/IDA Pro` on Windows. The path can be found using `idaapi.get_user_idadir()`. Users can set their own plugins to load, thus eliminating the need for root access.

#### Project-Specific

Located in the same directory as the `.idb` you're loading.



## Usage

To install your plugins, just add them to one of the lists. This allows you to easily update plugins as you go without ever needing to copy them.

When IDA starts, the plugin lists the locations of plugin lists in the output window.

```
[PluginLoader] Loading plugins from:
[PluginLoader]   System-wide List:      C:\Program Files\IDA 7.1\cfg\plugins.list
[PluginLoader]   User-specific List:    C:\Users\user\AppData\Roaming\Hex-Rays\IDA Pro\plugins.list
[PluginLoader] Failed creating system plugin list at C:\Program Files\IDA 7.1\cfg\plugins.list
[PluginLoader] Created user plugin list at C:\Users\user\AppData\Roaming\Hex-Rays\IDA Pro\plugins.list
```
_Since IDA is not running as admin - it cannot create the system plugin list._

