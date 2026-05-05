# Medieval Fortress Generator

## What It Does
A Maya tool that generates medieval European fortresses from configuration parameters.
Artists can control wall dimensions, tower count, keep height, and materials
without touching the creation logic.

## Planned Features
- [x] Core geometry functions (Week 6)
- [ ] Data-driven configuration (Week 7)
- [ ] Error handling + debug mode (Week 8)
- [ ] Maya UI window + JSON save/load (Week 9)
- [ ] Polish + documentation (Week 10)

## Project Structure
```
fortress_demo/
    fortress_geometry.py   # create_wall, create_merlons, create_tower, create_keep, create_gatehouse
    fortress_materials.py  # create_material, assign_material
    main.py                # Entry point, config, build_fortress()
    README.md              # This file
```

## Functions

### fortress_geometry.py
- `create_wall(length, height, thickness, position)` — Curtain wall segment
- `create_merlons(length, wall_height, merlon_size, spacing, position, axis)` — Row of battlements
- `create_tower(radius, height, position)` — Round tower with conical roof
- `create_keep(width, floors, floor_height, position)` — Central keep with battlements
- `create_gatehouse(width, height, tower_radius, tower_height, position)` — Gate opening + flanking towers

### fortress_materials.py
- `create_material(name, color)` — Lambert shader with RGB color
- `assign_material(obj_name, shader_name)` — Apply shader to object/group

## How to Run
1. Open Maya
2. Open Script Editor (Windows > General Editors > Script Editor)
3. Source `main.py` from the fortress_demo folder

## Author
Anuraj Bhatnagar | DIGM 131 | Drexel University
