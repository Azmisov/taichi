from contextlib import contextmanager


class Gui:
    """For declaring IMGUI components in a :class:`taichi.ui.Window`
    created by the GGUI system.

    Args:
        gui: reference to a `PyGui`.
    """

    def __init__(self, gui) -> None:
        self.gui = gui

    @contextmanager
    def sub_window(self, name, x, y, width, height):
        """Creating a context manager for subwindow.

        Note:
            All args of this method should align with `begin`.

        Args:
            x (float): The x-coordinate (between 0 and 1) of the top-left \
                corner of the subwindow, relative to the full window.
            y (float): The y-coordinate (between 0 and 1) of the top-left \
                corner of the subwindow, relative to the full window.
            width (float): The width of the subwindow relative to the full window.
            height (float): The height of the subwindow relative to the full window.

        Example::

            >>> with gui.sub_window(name, x, y, width, height) as g:
            >>>     g.text("Hello, World!")
        """
        self.begin(name, x, y, width, height)
        try:
            yield self
        finally:
            self.end()

    def begin(self, name, x, y, width, height):
        """Creates a subwindow that holds imgui widgets.

        All widget function calls (e.g. `text`, `button`) after the `begin`
        and before the next `end` will describe the widgets within this subwindow.

        Args:
            x (float): The x-coordinate (between 0 and 1) of the top-left \
                corner of the subwindow, relative to the full window.
            y (float): The y-coordinate (between 0 and 1) of the top-left \
                corner of the subwindow, relative to the full window.
            width (float): The width of the subwindow relative to the full window.
            height (float): The height of the subwindow relative to the full window.
        """
        self.gui.begin(name, x, y, width, height)

    def end(self):
        """End the description of the current subwindow."""
        self.gui.end()

    def text(self, text, color=None):
        """Declares a line of text."""
        if color is None:
            self.gui.text(text)
        else:
            self.gui.text_colored(text, color)

    def checkbox(self, text, old_value):
        """Declares a checkbox, and returns whether or not it has been checked.

        Args:
            text (str): a line of text to be shown next to the checkbox.
            old_value (bool): whether the checkbox is currently checked.
        """
        return self.gui.checkbox(text, old_value)

    def slider_int(self, text, old_value, minimum, maximum):
        """Declares a slider, and returns its newest value.

        Args:
            text (str): a line of text to be shown next to the slider
            old_value (int) : the current value of the slider.
            minimum (int): the minimum value of the slider.
            maximum (int): the maximum value of the slider.

        Returns:
            int: the updated value of the slider.
        """
        return self.gui.slider_int(text, old_value, minimum, maximum)

    def slider_float(self, text, old_value, minimum, maximum):
        """Declares a slider, and returns its newest value.

        Args:
            text (str): a line of text to be shown next to the slider
            old_value (float): the current value of the slider.
            minimum (float): the minimum value of the slider.
            maximum (float): the maximum value of the slider.
        """
        return self.gui.slider_float(text, old_value, minimum, maximum)

    def color_edit_3(self, text, old_value):
        """Declares a color edit palate.

        Args:
            text (str): a line of text to be shown next to the palate.
            old_value (Tuple[float]): the current value of the color, this \
                should be a tuple of floats in [0,1] that indicates RGB values.
        """
        return self.gui.color_edit_3(text, old_value)

    def button(self, text):
        """Declares a button, and returns whether or not it had just been clicked.

        Args:
            text (str): a line of text to be shown next to the button.
        """
        return self.gui.button(text)

    def input_int(self, label, old_value):
        """Integer input field with +/- buttons.

        Args:
            label (str): Label for the input field.
            old_value (int): Current value.

        Returns:
            int: The updated value.
        """
        return self.gui.input_int(label, old_value)

    def input_float(self, label, old_value):
        """Float input field with +/- buttons.

        Args:
            label (str): Label for the input field.
            old_value (float): Current value.

        Returns:
            float: The updated value.
        """
        return self.gui.input_float(label, old_value)

    def drag_int(self, label, old_value, speed=1.0, minimum=0, maximum=0):
        """Draggable integer input.

        Args:
            label (str): Label for the input.
            old_value (int): Current value.
            speed (float): Drag speed multiplier.
            minimum (int): Minimum value (0 for no limit).
            maximum (int): Maximum value (0 for no limit).

        Returns:
            int: The updated value.
        """
        return self.gui.drag_int(label, old_value, speed, minimum, maximum)

    def drag_float(self, label, old_value, speed=1.0, minimum=0.0, maximum=0.0):
        """Draggable float input.

        Args:
            label (str): Label for the input.
            old_value (float): Current value.
            speed (float): Drag speed multiplier.
            minimum (float): Minimum value (0.0 for no limit).
            maximum (float): Maximum value (0.0 for no limit).

        Returns:
            float: The updated value.
        """
        return self.gui.drag_float(label, old_value, speed, minimum, maximum)

    def combo(self, label, current_index, items):
        """Combo box (dropdown) for selecting from a tuple of items.

        Args:
            label (str): Label for the combo box.
            current_index (int): Currently selected index (0-based).
            items (tuple[str, ...]): Tuple of string options.

        Returns:
            int: The newly selected index.

        Note:
            Converting Python strings to ImGui format is cached when the same
            tuple object is passed across frames. For best performance, define
            options at module or class level (not inside the render loop)::

                DIFFICULTIES = ("Easy", "Medium", "Hard")  # module level

                while window.running:
                    with gui.sub_window(...) as w:
                        # Cached - same tuple object each frame
                        idx = w.combo("Difficulty", idx, DIFFICULTIES)
                    window.show()
        """
        return self.gui.combo(label, current_index, items)
