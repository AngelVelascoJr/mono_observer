# Guia de uso urdf2mjcf

obtenido de: https://docs.kscale.dev/docs/urdf2mjcf

## Installation
You can install the package using pip:
```sh
pip install urdf2mjcf
```

## Usage
### Command Line
To run the conversion script from the command line, use:
```sh
urdf2mjcf path/to/your/robot.urdf
```
This will save the MJCF file in the same directory as the URDF file.

To see all the options, use:
```sh
urdf2mjcf -h
```

### Python
To run the conversion script from Python, use:

```py
from urdf2mjcf import run

run(
    urdf_path="path/to/your/robot.urdf",
    mjcf_path="path/to/save/robot.mjcf",
    copy_meshes=True,
)
```