PyKimix

Python game / engine utility library with optional native acceleration.

GitHub
https://github.com/stormm-dev/pykimix

Features
- Python-first
- Optional C/C++ core via .so
- Pygame and Kivy safe coexistence
- Automatic single-window handling
- Resource helpers
- Font system
- Modular engine parts
- Android friendly

Usage
import pykimix

Nothing else required. Core logic runs on import.

Math
add(a, b)
sub(a, b)
mul(a, b)

Uses native core if available, otherwise Python fallback.

Fonts
Loaded from pykimix/assets/fonts
Accessed by numeric ID.

font(id, size)
list_fonts()

Windows
Automatically keeps only one window alive.
No manual calls.
No configuration.

Native Core
pykimix/c_core/libpykimix.so
Loaded automatically if present.

Platforms
Windows
Linux
Android

Python
3.8+

Version
0.4.3

Update Logs

v0.4.3
- Fixed window bug on Android
- Improved window handling when using Pygame and Kivy together
- Stabilized automatic single-window control
- Minor internal cleanup