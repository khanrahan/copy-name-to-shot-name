#!/usr/bin/env python

"""
Copy Segment Name to Shot Name

URL:

    https://github.com/khanrahan/copy-name-to-shot-name

Description:

    Simple script to copy segment name to shot name on all selected segments.

Menus:

    Right-click selected segments in a sequence -> Copy... -> Segment Name to Shot Name

To Install:

    For all users, copy this file to:
    /opt/Autodesk/shared/python

    For a specific user, copy this file to:
    /opt/Autodesk/user/<user name>/python
"""

from __future__ import print_function

__title__ = "Copy Segment to Shot Name"
__version_info__ = (0, 0, 2)
__version__ = ".".join([str(num) for num in __version_info__])
__version_title__ = "{} v{}".format(__title__, __version__)

MESSAGE_PREFIX = "[PYTHON HOOK]"

def message(string):
    """Print message to shell window and append global MESSAGE_PREFIX."""

    print(" ".join([MESSAGE_PREFIX, string]))


def copy_segment_name_to_shot_name(selection):

    message(__version_title__)
    message("Script called from {}".format(__file__))

    for segment in selection:
        segment.shot_name = segment.name
        message("{} copied to shot name.".format(segment.name.get_value()))


def scope_timeline_clip(selection):
    import flame

    for item in selection:
        if isinstance(item, flame.PySegment):
            return True
    return False


def get_timeline_custom_ui_actions():

    return [{'name': "Copy...",
             'actions': [{'name': "Segment Name to Shot Name",
                          'isVisible': scope_timeline_clip,
                          'execute': copy_segment_name_to_shot_name,
                          'minimumVersion': "2020"}]
           }]
