# pico_dev_template

A template Git repository for developing code for the  Raspberry Pi Pico W.

The `configure.bsh` script:
1. Sets up the Virtural envvironment (venv), 
2. Installs the required stubs as a Python package 
3. Configures VS Code so the stubs are used so you don't see issues with intellisense
4. Installs mpremote so you can connect to the Pico and run code on it easily.


Setup Steps:

1. When you create your new repo, use this one as the template (you may wish to fork this repo)
2. In your cloned repo, execute:

 ```bash
 configure.bsh
 ``` 
     (Yes you need to be using Linux.)

3. Activate the virtual environment:
```bash
source venv/bin/activate
```
4. Then you should be able to develop withoput micropython import errors - as VS Code will be using the stubs.
