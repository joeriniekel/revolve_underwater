# Underwater simulation

This folder contains code used to create and experiment on underwater simulation capabilities in Revolve and Gazebo. The plugins folder contains the C++ and CMake files needed to create the shared library file for the buoyancy plugin.

## Installation

Navigate to `revolve/experiments/underwater/plugins/build` and run the CMake commands.

```bash
cd revolve/experiments/underwater/plugins/build
cmake ../
make -j4
```
This creates the shared library file `libCustomBuoyancyPlugin.so` which needs to be copied to `revolve/build/lib` to be usable.

The build folder in `revolve/experiments/underwater/plugins/build` should also contain the file `libLiftDragPlugin.so`, also copy and paste this into `revolve/build/lib`. If `libLiftDragPlugin.so` is not there or does not work, it can be copied from the gazebo files.

## Usage

To use the underwater physics in your simulation set the parameter `underwater` to `True` in the manager file in the `save_file` and `insert_robot` functions. 

I.E.
```python
robot.save_file(f'{"experiments/examples/yaml/spider.yaml"}.sdf', conf_type='sdf', underwater=True)
robot_manager = await connection.insert_robot(robot, Vector3(0, 0, 0.25), life_timeout=None, underwater=True)
```

To change the density of the fluid, add sub elements to the Lift and Drag and the Buoyancy plugins in the `revolve_bot_to_sdf` function in `revolve_bot_sdf_builder.py` like so:
```python
SDF.sub_element_text(lift_drag_plugin, 'rho', '999.1026') # sets the density to 999.1026 kg/m^3
SDF.sub_element_text(buoyancy_plugin, 'fluidDensity', '999.1026') # sets the density to 999.1026 kg/m^3
```
And to change the surface height, add the following sub element in the same place:
```python
SDF.sub_element_text(buoyancy_plugin, 'surfaceHeight', '10') # sets the surface height to 10
```

## Contributing
To add new types of modules to the buoyancy plugin, make sure that they are defined in the .sdf file with a unique identifier in the name (like 'CoreComponent' for the core module or 'FixedBrick' for the brick module). Then add an `else if` to the `if` statement on line 146 of `BuoyancyPlugin.cc` like so:
```c++
else if (collisionName.find("NewModuleIdentfier") != std::string::npos) // if the module is the new module
    volume = [the_volume_of_the_new_module];
}
```
To change the volume of an existing or new module, first you can calculate the volume from the mesh of the module using the function `volumeOfMesh` in `calculate_volume.py`, this new value can then be put into the `if` or `else if` statements in `BuoyancyPlugin.cc`