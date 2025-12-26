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
0.4.31

Update Logs

v0.4.31
- Added native C/C++ core support with automatic loading
- Introduced structured c_core layout (include/src)
- Native math, utility, and GPU placeholders via ctypes
- Automatic window guard for Pygame and Kivy on import
- Fixed duplicate / stuck window issue on Android
- Improved stability when both Pygame and Kivy are present
- Safe fallback to pure Python when native core is missing
- Internal cleanup and initialization hardening