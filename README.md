# IDA Plugin Loader

What if you could install IDA plugins using `pip`?

What if they could bring their dependencies along?

Well, now you can!

## Installation

Copy the `plugin_loader.py` plugin into your IDA plugins directory

## Creating Installable Plugins

You need to add an entry-point in the `idapython` group to your package.
See the `nop-plugin` for an example:

```toml
[project.entry-points.idapython]
nop-plugin = "nop_plugin"
```

Note that no two plugins can have the same entry-point name!

## Installing Plugins

Using the Python version IDA uses (see `idapyswitch.exe`), install the package containing your plugin.
Either from its directory, or from PyPI.

```shell
py -3.10 -m pip install some-cool-plugin
```

While developing locally, you can use an editable installation:

```shell
py -3.10 -m pip install -e ./nop-plugin
```