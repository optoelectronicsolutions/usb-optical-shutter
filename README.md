# USB Optical Shutter & Filter Wheel Dev Kit

A hackable, open-source USB optical shutter and prototyping kit designed for optics benches, laser labs, and microscopy experimentation. Designed as a budget-friendly educational alternative to commercial shutters, this kit friction-fits standard 1" optical tubes (Thorlabs SM1 series) and mounts directly to standard optical posts via a 1/4"-20 threaded base.

## Hardware Features
* **Optical Bench Ready:** 1/4"-20 base mount and Thorlabs SM1 1-inch tube friction fit.
* **RP2040 Controller:** Powered by a Seeed Studio XIAO RP2040 microcontroller. 
* **Actuation:** Uses an MG90S 9g metal-gear servo for fast shutter operation or 3-position optical filtering.
* **Expansion Ready:** Custom PCB includes a built-in Hall-effect sensor circuit, allowing users to swap to a continuous rotation servo and embed magnets for a custom multi-position indexed filter wheel.

## Quick Start Setup (CircuitPython)
If your RP2040 is not pre-flashed, or you want to reset it, follow these steps:

1. **Install CircuitPython:** 
   * Hold the `BOOT` button on the XIAO RP2040 and plug it into your PC via USB.
   * A drive named `RPI-RP2` will appear. 
   * Download the latest CircuitPython `.uf2` file for the Seeed XIAO RP2040 from the official CircuitPython website.
   * Drag and drop the `.uf2` file onto the `RPI-RP2` drive. The board will reboot and appear as a `CIRCUITPY` drive.
2. **Load the Code:**
   * Download the `code.py` script and the `lib` folder from the `/Code/` directory of this repository.
   * Drag both `code.py` and the `lib` folder directly onto the `CIRCUITPY` drive.
3. **Control:**
   * The shutter can be toggled manually via the onboard physical button.
   * You can control it via USB serial by sending `open` or `close` commands.

## Customization & 3D Files
The included `.STL` files in the `/Hardware/` folder contain the standard open housing, the shutter flag, and fully enclosed tube-shield designs if your beamline requires an enclosed setup. You are free to modify and print these as needed!

## ⚠️ Important Disclaimers

**Development & Educational Notice:**  
This kit is an educational development and prototyping component designed for experimental use, benchtop testing, and maker projects. It is a starting point for optomechanical control, not a finished, certified consumer appliance. 

**NOT A LASER SAFETY INTERLOCK:**  
This device uses standard hobbyist servo actuation and is intended solely for optical path routing, attenuation, and experimental filtering. **It must NOT be used as a primary laser safety interlock, fail-safe beam dump, or personal protection device.** Always adhere to standard laser laboratory safety protocols and use certified safety equipment for hazardous light sources. Hardware and code are provided open-source "AS-IS" without warranties of any kind.
