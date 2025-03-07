# Copy Name to Shot Name
Plugin for [Autodesk Flame software](http://www.autodesk.com/products/flame).

Simple script to copy segment name to shot name on all selected segments.

Useful to extrapolate your shot names that are lost when reconforming with segments that already have shot names.
See [this post](https://forum.logik.tv/t/conform-keep-shot-names/932/16) and [this post](https://forum.logik.tv/t/conform-keep-shot-names/932/23) on [this Logik forum thread](https://forum.logik.tv/t/conform-keep-shot-names/932) for further explanation.

## Compatibility
|Release Version|Flame Version|
|---|---|
|v1.X.X|Flame 2022 and newer|
|v0.0.1|Flame 2021 up to 2021.2|

## Installation

### Flame 2025 and newer
To make available to all users on the workstation, copy `copy_name_to_shot_name.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `copy_name_to_shot_name.py` to the appropriate path below...
|Platform|Path|
|---|---|
|Linux|`/home/<user_name>/flame/python/`|
|Mac|`/Users/<user_name>/Library/Preferences/Autodesk/flame/python/`|

### Flame 2021 up to 2024.2
To make available to all users on the workstation, copy `copy_name_to_shot_name.py` to `/opt/Autodesk/shared/python/`

For specific users, copy `copy_name_to_shot_name.py` to `/opt/Autodesk/user/<user name>/python/`

## Menus
 - Right-click selected segments in a sequence `->` Copy... `->` Copy Segment Name to Shot Name
