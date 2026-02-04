from taichi._lib import core as _ti_core

from .camera import Camera  # pylint: disable=unused-import
from .canvas import Canvas  # pylint: disable=unused-import
from .constants import *  # pylint: disable=unused-import,wildcard-import
from .imgui import Gui  # pylint: disable=unused-import
from .scene import Scene  # pylint: disable=unused-import
from .utils import check_ggui_availability  # pylint: disable=unused-import
from .window import Window  # pylint: disable=unused-import


# ----------------------
ProjectionMode = _ti_core.ProjectionMode if _ti_core.GGUI_AVAILABLE else None
"""Camera projection mode, 0 for perspective and 1 for orthogonal.
"""

MonitorInfo = _ti_core.MonitorInfo if _ti_core.GGUI_AVAILABLE else None
"""Information about a connected monitor.

Attributes:
    name (str | None): Human-readable monitor name, or None if unavailable.
    x (int): Monitor x position in virtual screen coordinates.
    y (int): Monitor y position in virtual screen coordinates.
    width (int): Monitor width in pixels.
    height (int): Monitor height in pixels.
    work_x (int): Work area x position (excludes taskbar/dock).
    work_y (int): Work area y position.
    work_width (int): Work area width.
    work_height (int): Work area height.
    scale_x (float): Horizontal DPI scale factor.
    scale_y (float): Vertical DPI scale factor.
    refresh_rate (int): Refresh rate in Hz.
    is_primary (bool): True if this is the primary monitor.
"""


def get_monitors():
    """Get information about all connected monitors.

    Returns:
        list[MonitorInfo]: List of monitor information objects.

    Example::

        monitors = ti.ui.get_monitors()
        for m in monitors:
            print(f"{m.name}: {m.width}x{m.height} @ {m.x},{m.y}")

        # Center window on primary monitor
        primary = next(m for m in monitors if m.is_primary)
        win_w, win_h = 800, 600
        x = primary.work_x + (primary.work_width - win_w) // 2
        y = primary.work_y + (primary.work_height - win_h) // 2
        window = ti.ui.Window("Centered", (win_w, win_h), pos=(x, y))
    """
    check_ggui_availability()
    return _ti_core.get_monitors()


def make_camera():
    return Camera()
