# wai-lazypip

Allows installation of additional packages at runtime (from within virtual environments).
Uses `pip` underneath the hood for installing the packages.


## Installation

TODO


## Functionality

The following methods are available from module `wai.lazypip`:

* `check_module` - checks whether the module is present and, if a list of packages has 
  been provided, installs these and performs check again.
* `require_module` - like `check_module`, but instead of returning a boolean, will
  raise an Exception in case the module is not present.

The packages list

## Examples

* checking whether we are in a virtual environment

  ```python
  from wai.lazypip import is_venv
  if is_venv():
      print("yep, in a virtual environment")
  else:
      print("sorry, not a virtual environment")
  ```

* checking for the `matplotlib` module and installing matplotlib older than 3.3.0 if
  not yet present in the virtual environment 

  ```python
  from wai.lazypip import check_module
  m = "matplotlib"
  p = [m + "<3.3.0"]
  print(m, check_module(m, p))
  ```

* checking whether the `matplotlib` module has method `validate_backend` and installing 
  matplotlib older than 3.3.0 if not yet present in the virtual environment 

  ```python
  from wai.lazypip import check_fun
  m = "matplotlib"
  f = "validate_backend"
  p = [m + "<3.3.0"]
  print(m, check_fun(m, f, p))
  ```
