from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction

__all__ = ["create_menu_action"]


def create_menu_action(
    self,
    text,
    slot=None,
    shortcut=None,
    icon=None,
    tip=None,
    checkable=False,
    signal="triggered",
):
    """Create a menu action.

    Parameters
    ----------
    self : instance of `~PyQt5.QtWidgets.QMenu`
        The menu to which the action is added.
    text : str
        The text of the menu action.
    slot : callable, optional
        The callable to be called when the menu action is triggered. Default is None.
    shortcut : str or `PyQt5.QtGui.QKeySequence.StandardKey`, optional
        The shortcut of the menu action. Default is None. If None, the function test if `getattr(self, text)` exists.
        If it does, the shortcut is set to the value of `getattr(self, text)`. Otherwise, the shortcut is set to None.
    icon : str, optional
        The icon of the menu action. Default is None.
    tip : str, optional
        The tip of the menu action. Default is None.
    checkable : bool, optional
        Whether the menu action is checkable. Default is False.
    signal : str, optional
        The signal of the menu action. Default is "triggered".
    """
    action = QAction(text, self)
    if icon is not None:
        action.setIcon(QIcon(icon))
    if shortcut is not None:
        action.setShortcut(shortcut)
    elif hasattr(QKeySequence, text):
        action.setShortcut(getattr(QKeySequence, text))
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if slot is not None:
        getattr(action, signal).connect(slot)
    if checkable:
        action.setCheckable(True)
    return action
