"""
main.py -- Medieval Fortress Generator
========================================
DIGM 131 - Week 6 Demo | Author: Anuraj Bhatnagar

Assembles a complete fortress using geometry and material modules.
"""

import os
import sys
import maya.cmds as cmds

try:
    _THIS_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _THIS_DIR = cmds.workspace(query=True, rootDirectory=True)

if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import fortress_geometry as geo
import fortress_materials as mat


# --- Fortress configuration ---
WALL_LENGTH = 16
WALL_HEIGHT = 5
TOWER_RADIUS = 1.5

MATERIAL_PALETTE = {
    "walls":  ("castle_stone",  (0.55, 0.55, 0.50)),
    "towers": ("tower_stone",   (0.50, 0.48, 0.45)),
    "keep":   ("keep_dark",     (0.40, 0.38, 0.35)),
    "roof":   ("slate_roof",    (0.30, 0.32, 0.35)),
    "gate":   ("iron_gate",     (0.25, 0.22, 0.20)),
}


def build_fortress(position=(0, 0, 0)):
    """Assemble a complete medieval fortress at the given position.

    Args:
        position (tuple): (x, y, z) center of the fortress.

    Returns:
        str: Name of the fortress group.
    """
    px, py, pz = position
    half = WALL_LENGTH / 2.0
    parts = []

    # Create materials
    shaders = {}
    for key, (name, color) in MATERIAL_PALETTE.items():
        shaders[key] = mat.create_material(name, color)

    # Ground plane
    ground = cmds.polyPlane(
        w=WALL_LENGTH * 2, h=WALL_LENGTH * 2,
        sx=1, sy=1, name="fortress_ground_#"
    )[0]
    cmds.move(px, py, pz, ground)
    parts.append(ground)

    # Curtain walls (4 sides)
    wall_configs = [
        {"length": WALL_LENGTH, "height": WALL_HEIGHT,
         "position": (px, py, pz + half)},
        {"length": WALL_LENGTH, "height": WALL_HEIGHT,
         "position": (px, py, pz - half)},
        {"length": WALL_LENGTH, "height": WALL_HEIGHT,
         "position": (px + half, py, pz)},
        {"length": WALL_LENGTH, "height": WALL_HEIGHT,
         "position": (px - half, py, pz)},
    ]
    for i, config in enumerate(wall_configs):
        wall = geo.create_wall(**config)
        if i >= 2:
            cmds.rotate(0, 90, 0, wall)
        mat.assign_material(wall, shaders["walls"])
        parts.append(wall)

    # Corner towers
    corners = [
        (px + half, py, pz + half),
        (px - half, py, pz + half),
        (px + half, py, pz - half),
        (px - half, py, pz - half),
    ]
    tower_height = WALL_HEIGHT * 1.6
    for corner in corners:
        tower = geo.create_tower(
            radius=TOWER_RADIUS, height=tower_height, position=corner
        )
        mat.assign_material(tower, shaders["towers"])
        parts.append(tower)

    # Central keep
    keep = geo.create_keep(
        width=6, floors=3, floor_height=WALL_HEIGHT * 0.8,
        position=(px, py, pz)
    )
    mat.assign_material(keep, shaders["keep"])
    parts.append(keep)

    # Gatehouse on the south wall
    gatehouse = geo.create_gatehouse(
        position=(px, py, pz - half)
    )
    mat.assign_material(gatehouse, shaders["gate"])
    parts.append(gatehouse)

    cmds.viewFit(allObjects=True)
    print("=== Fortress Complete ===")
    print("  {} parts assembled.".format(len(parts)))

    return cmds.group(parts, name="fortress_#")


# -------------------------------------------------------------------
if __name__ == "__main__":
    cmds.file(new=True, force=True)
    build_fortress()
