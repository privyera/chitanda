import importlib
import sys
from pkgutil import iter_modules

from snowball.config import config


def load_commands(bot):
    for name in _get_module_names():
        if not _is_module_enabled(name) and name in sys.modules:
            del sys.modules[name]
        else:
            importlib.import_module(name)
            if hasattr(sys.modules[name], 'setup'):
                sys.modules[name].setup(bot)


def reload_commands():
    for name in _get_module_names():
        if name in sys.modules:
            importlib.reload(sys.modules[name])
        else:
            importlib.import_module(sys.modules[name])


def _is_module_enabled(full_name):
    if config['modules_enabled']:
        try:
            short_name = full_name.lstrip('snowball.commands.').split('.')[0]
            if short_name not in config['modules_enabled']:
                return False
        except IndexError:
            pass
    return True


def _get_module_names(pkg_path=__name__):
    for module_info in iter_modules(sys.modules[pkg_path].__path__):
        modname = f'{pkg_path}.{module_info.name}'
        if module_info.ispkg:
            importlib.import_module(modname)
            for modname_ in _get_module_names(modname):
                yield modname_
        yield modname
