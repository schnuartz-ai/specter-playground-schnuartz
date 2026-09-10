"""Widget tree extraction for LVGL."""
import lvgl as lv


def _label_text(obj):
    """Return the text of ``obj`` if it is an lv.label, else None.

    In the MicroPython LVGL binding every object exposes ``get_text``
    regardless of its real type, and calling it on a non-label reads a
    bogus pointer and segfaults the whole simulator. Gate on the real
    LVGL class instead of ``hasattr``.
    """
    try:
        if obj.check_type(lv.label_class):
            return obj.get_text()
    except Exception:
        pass
    return None


def get_widget_info(obj):
    """Extract info from single widget."""
    info = {
        "type": type(obj).__name__,
        "x": obj.get_x(),
        "y": obj.get_y(),
        "width": obj.get_width(),
        "height": obj.get_height(),
        "text": _label_text(obj),
        "children": [],
    }
    return info


def get_widget_tree(obj):
    """Recursively build widget tree from LVGL object."""
    info = get_widget_info(obj)
    child_count = obj.get_child_count()
    for i in range(child_count):
        child = obj.get_child(i)
        info["children"].append(get_widget_tree(child))
    return info


def find_widget_by_text(obj, text, parent=None):
    """Find widget containing label with given text. Returns (widget, parent)."""
    # Check if this is a label with matching text
    if _label_text(obj) == text:
        # Return parent (the button) if exists, else the label itself
        return (parent if parent else obj, obj)

    # Recurse into children
    child_count = obj.get_child_count()
    for i in range(child_count):
        child = obj.get_child(i)
        result = find_widget_by_text(child, text, obj)
        if result[0]:
            return result

    return (None, None)
