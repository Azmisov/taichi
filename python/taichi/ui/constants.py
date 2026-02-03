"""Key constants for :mod:`~taichi.ui`"""

from taichi._lib import core as _ti_core

SHIFT = "Shift"
ALT = "Alt"
CTRL = "Control"
ESCAPE = "Escape"
RETURN = "Return"
TAB = "Tab"
BACKSPACE = "BackSpace"
SPACE = " "
UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"
CAPSLOCK = "CapsLock"
LMB = "LMB"
MMB = "MMB"
RMB = "RMB"

# Function keys
F1 = "F1"
F2 = "F2"
F3 = "F3"
F4 = "F4"
F5 = "F5"
F6 = "F6"
F7 = "F7"
F8 = "F8"
F9 = "F9"
F10 = "F10"
F11 = "F11"
F12 = "F12"

# Navigation keys
INSERT = "Insert"
DELETE = "Delete"
HOME = "Home"
END = "End"
PAGEUP = "PageUp"
PAGEDOWN = "PageDown"

# Numpad keys
NUMPAD0 = "Numpad0"
NUMPAD1 = "Numpad1"
NUMPAD2 = "Numpad2"
NUMPAD3 = "Numpad3"
NUMPAD4 = "Numpad4"
NUMPAD5 = "Numpad5"
NUMPAD6 = "Numpad6"
NUMPAD7 = "Numpad7"
NUMPAD8 = "Numpad8"
NUMPAD9 = "Numpad9"
NUMPAD_DECIMAL = "NumpadDecimal"
NUMPAD_DIVIDE = "NumpadDivide"
NUMPAD_MULTIPLY = "NumpadMultiply"
NUMPAD_SUBTRACT = "NumpadSubtract"
NUMPAD_ADD = "NumpadAdd"
NUMPAD_ENTER = "NumpadEnter"

# Event types
PRESS = "Press"
RELEASE = "Release"

# Cursor shapes
try:
    CURSOR_DEFAULT = _ti_core.CURSOR_DEFAULT  # Reset to default (ImGui manages)
    CURSOR_NONE = _ti_core.CURSOR_NONE  # Hide cursor
    CURSOR_ARROW = _ti_core.CURSOR_ARROW
    CURSOR_IBEAM = _ti_core.CURSOR_IBEAM
    CURSOR_CROSSHAIR = _ti_core.CURSOR_CROSSHAIR
    CURSOR_HAND = _ti_core.CURSOR_HAND
    CURSOR_RESIZE_EW = _ti_core.CURSOR_RESIZE_EW
    CURSOR_RESIZE_NS = _ti_core.CURSOR_RESIZE_NS
    CURSOR_RESIZE_NWSE = _ti_core.CURSOR_RESIZE_NWSE
    CURSOR_RESIZE_NESW = _ti_core.CURSOR_RESIZE_NESW
    CURSOR_RESIZE_ALL = _ti_core.CURSOR_RESIZE_ALL
    CURSOR_NOT_ALLOWED = _ti_core.CURSOR_NOT_ALLOWED
except AttributeError:
    # Fallback if GGUI is not available
    pass
