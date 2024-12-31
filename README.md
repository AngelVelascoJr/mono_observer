# mono_observer
Repostory related to the development of a 3dof monocular robot

## mono_observer_driver

the mono_observer_driver pkg requires the 'serial' library, I recomend to create a venv in this proyect, add it to the .gitignore (it already has a myvenv ignore instruction, but rename it as you wish), activate it and install the requirements.txt file:

```sh
python -m venv myvnev
source myvenv/bin/activate
pip install -r requirements.txt
```

then use the venv each time you require to run the [serial-comunication.py](./mono_observer_driver/mono_observer_driver/serial_comunication.py) file (or test files)

## Virtual Machine recomendations
for testing in VMWare you must have the usb device conected to the virtual machine, also if the driver (arduino or esp32) disconects automaticaly while checking it's port availability at the end of the output of the next line

```sh
sudo dmesg
```

then check for the brltty package(a braille e-reader), as it has priority over serial devices, as stated [here](https://askubuntu.com/questions/1454633/dev-ttyusb0-device-connects-then-is-forced-to-disconnect-by-another-device#:~:text=It%20happen%20due%20to%20brltty%20accessibility%20service%20for,system%20later.%20Simply%20disable%20or%20remove%20this%20service.) and [here](https://stackoverflow.com/questions/70123431/why-would-ch341-uart-be-disconnected-from-ttyusb)

the solution proposed is to uninstall the pkg directly if is not used, or to dissable it:

```sh
sudo apt remove brltty
```

you also may encounter the next error while trying to conect to your device 

```
PermissionError: [Errno 13] Permission denied: '/dev/ttyUSB0'
```

finaly, in [this](https://techoverflow.net/2022/06/10/how-to-fix-dev-ttyusb0-or-dev-ttyacm0-permission-error/) page they mention to add your user to the dialgroup with the next command and then login and logout or restart your machine

```sh
sudo usermod -a -G dialout $USER
```