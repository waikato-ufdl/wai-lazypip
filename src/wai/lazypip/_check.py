import importlib
import pip
import traceback
from ._venv import is_venv

def install_packages(packages):
    """
    Installs the required packages.

    :param packages: the pip packages list
    :type packages: list
    """

    print("installing", packages)
    try:
        args = ["install"]
        args.extend(packages)
        pip.main(args)
    except:
        print("Failed to install: %s" % ",".join(packages))
        print(traceback.format_exc())



def check_module(module_name, packages=None):
    """
    Checks whether a module is present

    :param module_name: the module to check
    :type module_name: str
    :param packages: the list packages to install, no installation occurs if None
    :type packages: list
    :return: whether the module is present (if packages listed, then if present after installation of these)
    :rtype: bool
    """

    try:
        importlib.import_module(module_name)
        return True
    except:
        if packages is not None and is_venv():
            install_packages(packages)
            return check_module(module_name)
        else:
            return False
