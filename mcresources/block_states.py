"""
A collection of helper functions for creating common vanilla block state Jsons.

Usage:
```python
from mcresources import block_states
```
"""

from mcresources.type_definitions import Json, JsonObject


def slab_variants(block: str, block_slab: str, block_slab_top: str) -> JsonObject:
    return {
        'type=bottom': {'model': block_slab},
        'type=top': {'model': block_slab_top},
        'type=double': {'model': block}
    }


def stairs_variants(stairs: str, stairs_inner: str, stairs_outer: str) -> JsonObject:
    return {
        'facing=east,half=bottom,shape=straight': {'model': stairs},
        'facing=west,half=bottom,shape=straight': {'model': stairs, 'y': 180, 'uvlock': True},
        'facing=south,half=bottom,shape=straight': {'model': stairs, 'y': 90, 'uvlock': True},
        'facing=north,half=bottom,shape=straight': {'model': stairs, 'y': 270, 'uvlock': True},
        'facing=east,half=bottom,shape=outer_right': {'model': stairs_outer},
        'facing=west,half=bottom,shape=outer_right': {'model': stairs_outer, 'y': 180, 'uvlock': True},
        'facing=south,half=bottom,shape=outer_right': {'model': stairs_outer, 'y': 90, 'uvlock': True},
        'facing=north,half=bottom,shape=outer_right': {'model': stairs_outer, 'y': 270, 'uvlock': True},
        'facing=east,half=bottom,shape=outer_left': {'model': stairs_outer, 'y': 270, 'uvlock': True},
        'facing=west,half=bottom,shape=outer_left': {'model': stairs_outer, 'y': 90, 'uvlock': True},
        'facing=south,half=bottom,shape=outer_left': {'model': stairs_outer},
        'facing=north,half=bottom,shape=outer_left': {'model': stairs_outer, 'y': 180, 'uvlock': True},
        'facing=east,half=bottom,shape=inner_right': {'model': stairs_inner},
        'facing=west,half=bottom,shape=inner_right': {'model': stairs_inner, 'y': 180, 'uvlock': True},
        'facing=south,half=bottom,shape=inner_right': {'model': stairs_inner, 'y': 90, 'uvlock': True},
        'facing=north,half=bottom,shape=inner_right': {'model': stairs_inner, 'y': 270, 'uvlock': True},
        'facing=east,half=bottom,shape=inner_left': {'model': stairs_inner, 'y': 270, 'uvlock': True},
        'facing=west,half=bottom,shape=inner_left': {'model': stairs_inner, 'y': 90, 'uvlock': True},
        'facing=south,half=bottom,shape=inner_left': {'model': stairs_inner},
        'facing=north,half=bottom,shape=inner_left': {'model': stairs_inner, 'y': 180, 'uvlock': True},
        'facing=east,half=top,shape=straight': {'model': stairs, 'x': 180, 'uvlock': True},
        'facing=west,half=top,shape=straight': {'model': stairs, 'x': 180, 'y': 180, 'uvlock': True},
        'facing=south,half=top,shape=straight': {'model': stairs, 'x': 180, 'y': 90, 'uvlock': True},
        'facing=north,half=top,shape=straight': {'model': stairs, 'x': 180, 'y': 270, 'uvlock': True},
        'facing=east,half=top,shape=outer_right': {'model': stairs_outer, 'x': 180, 'y': 90, 'uvlock': True},
        'facing=west,half=top,shape=outer_right': {'model': stairs_outer, 'x': 180, 'y': 270, 'uvlock': True},
        'facing=south,half=top,shape=outer_right': {'model': stairs_outer, 'x': 180, 'y': 180, 'uvlock': True},
        'facing=north,half=top,shape=outer_right': {'model': stairs_outer, 'x': 180, 'uvlock': True},
        'facing=east,half=top,shape=outer_left': {'model': stairs_outer, 'x': 180, 'uvlock': True},
        'facing=west,half=top,shape=outer_left': {'model': stairs_outer, 'x': 180, 'y': 180, 'uvlock': True},
        'facing=south,half=top,shape=outer_left': {'model': stairs_outer, 'x': 180, 'y': 90, 'uvlock': True},
        'facing=north,half=top,shape=outer_left': {'model': stairs_outer, 'x': 180, 'y': 270, 'uvlock': True},
        'facing=east,half=top,shape=inner_right': {'model': stairs_inner, 'x': 180, 'y': 90, 'uvlock': True},
        'facing=west,half=top,shape=inner_right': {'model': stairs_inner, 'x': 180, 'y': 270, 'uvlock': True},
        'facing=south,half=top,shape=inner_right': {'model': stairs_inner, 'x': 180, 'y': 180, 'uvlock': True},
        'facing=north,half=top,shape=inner_right': {'model': stairs_inner, 'x': 180, 'uvlock': True},
        'facing=east,half=top,shape=inner_left': {'model': stairs_inner, 'x': 180, 'uvlock': True},
        'facing=west,half=top,shape=inner_left': {'model': stairs_inner, 'x': 180, 'y': 180, 'uvlock': True},
        'facing=south,half=top,shape=inner_left': {'model': stairs_inner, 'x': 180, 'y': 90, 'uvlock': True},
        'facing=north,half=top,shape=inner_left': {'model': stairs_inner, 'x': 180, 'y': 270, 'uvlock': True}
    }


def fence_multipart(fence_post: str, fence_side: str) -> Json:
    return [
        {'model': fence_post},
        ({'north': 'true'}, {'model': fence_side, 'uvlock': True}),
        ({'east': 'true'}, {'model': fence_side, 'y': 90, 'uvlock': True}),
        ({'south': 'true'}, {'model': fence_side, 'y': 180, 'uvlock': True}),
        ({'west': 'true'}, {'model': fence_side, 'y': 270, 'uvlock': True})
    ]


def fence_gate_variants(fence_gate: str, fence_gate_open: str, fence_gate_wall: str, fence_gate_wall_open: str) -> JsonObject:
    return {
        'facing=south,in_wall=false,open=false': {'model': fence_gate, 'uvlock': True},
        'facing=west,in_wall=false,open=false': {'model': fence_gate, 'uvlock': True, 'y': 90},
        'facing=north,in_wall=false,open=false': {'model': fence_gate, 'uvlock': True, 'y': 180},
        'facing=east,in_wall=false,open=false': {'model': fence_gate, 'uvlock': True, 'y': 270},
        'facing=south,in_wall=false,open=true': {'model': fence_gate_open, 'uvlock': True},
        'facing=west,in_wall=false,open=true': {'model': fence_gate_open, 'uvlock': True, 'y': 90},
        'facing=north,in_wall=false,open=true': {'model': fence_gate_open, 'uvlock': True, 'y': 180},
        'facing=east,in_wall=false,open=true': {'model': fence_gate_open, 'uvlock': True, 'y': 270},
        'facing=south,in_wall=true,open=false': {'model': fence_gate_wall, 'uvlock': True},
        'facing=west,in_wall=true,open=false': {'model': fence_gate_wall, 'uvlock': True, 'y': 90},
        'facing=north,in_wall=true,open=false': {'model': fence_gate_wall, 'uvlock': True, 'y': 180},
        'facing=east,in_wall=true,open=false': {'model': fence_gate_wall, 'uvlock': True, 'y': 270},
        'facing=south,in_wall=true,open=true': {'model': fence_gate_wall_open, 'uvlock': True},
        'facing=west,in_wall=true,open=true': {'model': fence_gate_wall_open, 'uvlock': True, 'y': 90},
        'facing=north,in_wall=true,open=true': {'model': fence_gate_wall_open, 'uvlock': True, 'y': 180},
        'facing=east,in_wall=true,open=true': {'model': fence_gate_wall_open, 'uvlock': True, 'y': 270}
    }


def wall_multipart(wall_post: str, wall_side: str, wall_side_tall: str) -> Json:
    return [
        ({'up': 'true'}, {'model': wall_post}),
        ({'north': 'low'}, {'model': wall_side, 'uvlock': True}),
        ({'east': 'low'}, {'model': wall_side, 'y': 90, 'uvlock': True}),
        ({'south': 'low'}, {'model': wall_side, 'y': 180, 'uvlock': True}),
        ({'west': 'low'}, {'model': wall_side, 'y': 270, 'uvlock': True}),
        ({'north': 'tall'}, {'model': wall_side_tall, 'uvlock': True}),
        ({'east': 'tall'}, {'model': wall_side_tall, 'y': 90, 'uvlock': True}),
        ({'south': 'tall'}, {'model': wall_side_tall, 'y': 180, 'uvlock': True}),
        ({'west': 'tall'}, {'model': wall_side_tall, 'y': 270, 'uvlock': True})
    ]


def door_blockstate(base: str) -> JsonObject:
    left = base + '_bottom_left'
    left_open = base + '_bottom_left_open'
    right = base + '_bottom_right'
    right_open = base + '_bottom_right_open'
    top_left = base + '_top_left'
    top_left_open = base + '_top_left_open'
    top_right = base + '_top_right'
    top_right_open = base + '_top_right_open'
    return {
        'facing=east,half=lower,hinge=left,open=false': {'model': left},
        'facing=east,half=lower,hinge=left,open=true': {'model': left_open, 'y': 90},
        'facing=east,half=lower,hinge=right,open=false': {'model': right},
        'facing=east,half=lower,hinge=right,open=true': {'model': right_open, 'y': 270},
        'facing=east,half=upper,hinge=left,open=false': {'model': top_left},
        'facing=east,half=upper,hinge=left,open=true': {'model': top_left_open, 'y': 90},
        'facing=east,half=upper,hinge=right,open=false': {'model': top_right},
        'facing=east,half=upper,hinge=right,open=true': {'model': top_right_open, 'y': 270},
        'facing=north,half=lower,hinge=left,open=false': {'model': left, 'y': 270},
        'facing=north,half=lower,hinge=left,open=true': {'model': left_open},
        'facing=north,half=lower,hinge=right,open=false': {'model': right, 'y': 270},
        'facing=north,half=lower,hinge=right,open=true': {'model': right_open, 'y': 180},
        'facing=north,half=upper,hinge=left,open=false': {'model': top_left, 'y': 270},
        'facing=north,half=upper,hinge=left,open=true': {'model': top_left_open},
        'facing=north,half=upper,hinge=right,open=false': {'model': top_right, 'y': 270},
        'facing=north,half=upper,hinge=right,open=true': {'model': top_right_open, 'y': 180},
        'facing=south,half=lower,hinge=left,open=false': {'model': left, 'y': 90},
        'facing=south,half=lower,hinge=left,open=true': {'model': left_open, 'y': 180},
        'facing=south,half=lower,hinge=right,open=false': {'model': right, 'y': 90},
        'facing=south,half=lower,hinge=right,open=true': {'model': right_open},
        'facing=south,half=upper,hinge=left,open=false': {'model': top_left, 'y': 90},
        'facing=south,half=upper,hinge=left,open=true': {'model': top_left_open, 'y': 180},
        'facing=south,half=upper,hinge=right,open=false': {'model': top_right, 'y': 90},
        'facing=south,half=upper,hinge=right,open=true': {'model': top_right_open},
        'facing=west,half=lower,hinge=left,open=false': {'model': left, 'y': 180},
        'facing=west,half=lower,hinge=left,open=true': {'model': left_open, 'y': 270},
        'facing=west,half=lower,hinge=right,open=false': {'model': right, 'y': 180},
        'facing=west,half=lower,hinge=right,open=true': {'model': right_open, 'y': 90},
        'facing=west,half=upper,hinge=left,open=false': {'model': top_left, 'y': 180},
        'facing=west,half=upper,hinge=left,open=true': {'model': top_left_open, 'y': 270},
        'facing=west,half=upper,hinge=right,open=false': {'model': top_right, 'y': 180},
        'facing=west,half=upper,hinge=right,open=true': {'model': top_right_open, 'y': 90}
    }


def pressure_plate_variants(pressure_plate: str, pressure_plate_down: str) -> JsonObject:
    return {
        'powered=false': {'model': pressure_plate},
        'powered=true': {'model': pressure_plate_down}
    }
