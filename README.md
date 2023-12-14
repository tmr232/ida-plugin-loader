# IDA Plugin Loader

What if you could install IDA plugins using `pip`?

What if they could bring their dependencies along?

Well, now you can!

## Installation

Copy the `plugin_loader.py` plugin into your IDA plugins directory

## Creating Installable Plugins

You'll have to create a proper Python package.
With [Hatch](https://hatch.pypa.io/latest/), it's relatively straightforward.
You can look at [`nop-plugin`][./nop-plugin] for an example.

To keep things orderly, I recommend prefixing the package name with `idapython-`.

Once you have a package, you need the plugin-loader to find it!
To do that, add an `idapython` entry-point to your package, pointing to your plugin module.
See the `nop-plugin` for an example:

```toml
#                      Specify the idapython group
#                        |
#                        v
[project.entry-points.idapython]
nop-plugin = "nop_plugin"
#   ^             ^
#   |             |
# Plugin name     |
#               Plugin module name
```

Note that no two plugins can have the same entry-point name!


## Installing Plugins

Using the Python version IDA uses (see `idapyswitch.exe`), install the package containing your plugin.
Either from its directory, from git, or from PyPI.

```shell
py -3.10 -m pip install "git+https://github.com/tmr232/ida-plugin-loader@python-entry-point#egg=idapython-nop-plugin&subdirectory=nop-plugin"
```

While developing locally, you can use an editable installation:

```shell
py -3.10 -m pip install -e ./nop-plugin
```