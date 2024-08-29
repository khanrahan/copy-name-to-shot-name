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


import flame

TITLE = 'Find and Replace in Name Advance'
VERSION_INFO = (0, 0, 1, 'dev')
VERSION = '.'.join([str(num) for num in VERSION_INFO])
TITLE_VERSION = f'{TITLE} v{VERSION}'

MESSAGE_PREFIX = '[PYTHON]'


def message(string):
    """Print message to shell window and append global MESSAGE_PREFIX."""
    print(' '.join([MESSAGE_PREFIX, string]))


def copy_segment_name_to_shot_name(selection):

    message(TITLE_VERSION)
    message(f'Script called from {__file__}')

    for segment in selection:
        if isinstance(segment, flame.PySegment):
            segment.shot_name.set_value(segment.name.get_value())

    message('Done!')


def scope_timeline_clip(selection):

    valid_objects = (
            flame.PySegment,
            flame.PyTransition)

    return all(isinstance(item, valid_objects) for item in selection)


def get_timeline_custom_ui_actions():

    return [{'name': 'Copy...',
             'actions': [{'name': 'Segment Name to Shot Name',
                          'isVisible': scope_timeline_clip,
                          'execute': copy_segment_name_to_shot_name,
                          'minimumVersion': '2022'}]
           }]
