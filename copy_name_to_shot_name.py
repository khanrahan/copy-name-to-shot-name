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


VERSION = (0, 0, 1)


def copy_segment_name_to_shot_name(selection):

    for segment in selection:
        segment.shot_name = segment.name


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
