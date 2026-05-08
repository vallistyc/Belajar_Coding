import sys
import os
import math
from math import sin, pi
from pathlib import Path

# ── FIX 1: Panda3D render config (harus sebelum semua import Ursina)
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'load-display pandagl')
loadPrcFileData('', 'aux-display p3tinydisplay')
loadPrcFileData('', 'win-size 1280 720')

# ── FIX 2: asset_folder ke folder models bawaan Ursina
import ursina
from ursina import application
application.asset_folder = Path(ursina.__file__).parent / 'models'

from ursina import *

# =========================================================
# INPUT — builtin input() dipanggil SEBELUM def input(key)
# =========================================================
print("=== SETYASA HOLOGRAM VIEWER v4.0 ===")

try:
    R = float(input("Masukkan sisi kubus (R): "))
    r = float(input("Masukkan jari-jari kerucut (r): "))
    h = float(input("Masukkan tinggi kerucut (h): "))
except ValueError:
    print("[ERROR] Pakai default: R=3, r=0.8, h=2")
    R, r, h = 3.0, 0.8, 2.0

if r >= R / 2:
    print("[WARN] Radius terlalu besar, dikecilkan.")
    r = R / 2 * 0.8

if h > R:
    print("[WARN] Tinggi terlalu besar, dikecilkan.")
    h = R * 0.9

# =========================================================
# PERHITUNGAN
# =========================================================
volume_kubus    = R ** 3
volume_kerucut  = (1/3) * pi * r**2 * h
volume_sisa     = volume_kubus - volume_kerucut

luas_kubus      = 6 * R**2
luas_lubang     = pi * r**2
s               = math.sqrt(r**2 + h**2)
selimut_kerucut = pi * r * s
luas_sisa       = luas_kubus - luas_lubang + selimut_kerucut

# =========================================================
# APP INIT
# =========================================================
app = Ursina(
    title     = "STARK INDUSTRIES HOLOGRAM CAD",
    borderless= False,
    fullscreen= False,
    vsync     = True,
)

window.color               = color.rgb(2, 4, 10)
window.fps_counter.enabled = False
window.exit_button.visible = False

# =========================================================
# CAMERA
# =========================================================
camera.position = Vec3(0, 0, -(R * 5.5))
camera.fov      = 60
ZOOM_MIN = -(R * 10)
ZOOM_MAX = -(R * 2.5)

# =========================================================
# LIGHTING
# =========================================================
AmbientLight(color=color.rgb(10, 20, 40))

key_light = DirectionalLight(color=color.rgb(80, 180, 255), shadows=False)
key_light.look_at(Vec3(-1, -1.5, -1))

rim_light = DirectionalLight(color=color.rgb(255, 140, 30))
rim_light.look_at(Vec3(1, 0.5, 1))

# =========================================================
# ROOT ENTITY
# =========================================================
hologram = Entity()

# =========================================================
# KUBUS — 3 layer (TANPA shader eksternal)
# =========================================================
cube_solid = Entity(
    parent = hologram,
    model  = 'cube',
    color  = color.rgba(0, 160, 255, 85),
    scale  = R,
)

cube_shell = Entity(
    parent = hologram,
    model  = 'cube',
    color  = color.rgba(30, 200, 255, 22),
    scale  = R * 1.02,
)

try:
    cube_wire = Entity(
        parent = hologram,
        model  = 'wireframe_cube',
        color  = color.rgba(0, 255, 255, 200),
        scale  = R * 1.01,
    )
except Exception:
    cube_wire = Entity(
        parent = hologram,
        model  = 'cube',
        color  = color.rgba(0, 255, 255, 55),
        scale  = R * 1.01,
    )

# =========================================================
# KERUCUT — embedded di dalam kubus
# =========================================================
cone_y = (R / 2) - (h / 2)

cone_dark = Entity(
    parent     = hologram,
    model      = 'cone',
    color      = color.rgba(5, 10, 20, 220),
    scale      = (r * 2, h, r * 2),
    rotation_x = 180,
    y          = cone_y,
)

cone_glow = Entity(
    parent     = hologram,
    model      = 'cone',
    color      = color.rgba(255, 100, 20, 110),
    scale      = (r * 1.85, h * 0.97, r * 1.85),
    rotation_x = 180,
    y          = cone_y,
)

cone_rim = Entity(
    parent     = hologram,
    model      = 'circle',
    color      = color.rgba(255, 160, 50, 180),
    scale      = r * 2.1,
    rotation_x = 90,
    y          = R / 2 + 0.01,
)

# =========================================================
# GLOW RINGS
# =========================================================
ring_configs = [
    (1.6, 90, color.rgba(0, 255, 255, 90),  1.0),
    (1.4, 45, color.rgba(0, 180, 255, 70),  1.3),
    (1.2,  0, color.rgba(0, 255, 180, 50),  0.7),
]

rings = []
for scale_mul, rot_x, col, speed in ring_configs:
    ring = Entity(
        parent     = hologram,
        model      = 'circle',
        color      = col,
        scale      = R * scale_mul,
        rotation_x = rot_x,
    )
    rings.append((ring, speed))

# =========================================================
# CORNER MARKERS
# =========================================================
half = R / 2
for cx in (-half, half):
    for cy in (-half, half):
        for cz in (-half, half):
            Entity(
                parent   = hologram,
                model    = 'sphere',
                color    = color.rgba(0, 255, 255, 180),
                scale    = R * 0.04,
                position = Vec3(cx, cy, cz),
            )

# =========================================================
# HUD
# =========================================================
def hud(txt, x, y, col=color.cyan, sc=0.7):
    return Text(text=txt, x=x, y=y, color=col, scale=sc, parent=camera.ui)

hud("STARK INDUSTRIES | HOLOGRAM CAD",     -0.85,  0.45, color.rgba(0,255,255,220), 0.80)
hud("-----------------------------------",  -0.85,  0.42, color.rgba(0,180,255,100), 0.60)
hud(f"CUBE SIDE   : {R:.2f}",              -0.85,  0.36)
hud(f"CONE RADIUS : {r:.2f}",              -0.85,  0.31)
hud(f"CONE HEIGHT : {h:.2f}",              -0.85,  0.26)
hud("-----------------------------------",  -0.85,  0.22, color.rgba(0,180,255,100), 0.60)
hud("VOLUME ANALYSIS",                      -0.85,  0.16, color.rgba(255,200,50,220), 0.75)
hud(f"  Kubus   : {volume_kubus:.2f}",      -0.85,  0.11)
hud(f"  Kerucut : {volume_kerucut:.2f}",    -0.85,  0.06)
hud(f"  Sisa    : {volume_sisa:.2f}",       -0.85,  0.01, color.rgba(100,255,150,220))
hud("-----------------------------------",  -0.85, -0.04, color.rgba(0,180,255,100), 0.60)
hud("SURFACE ANALYSIS",                     -0.85, -0.10, color.rgba(255,200,50,220), 0.75)
hud(f"  Kubus   : {luas_kubus:.2f}",        -0.85, -0.15)
hud(f"  Lubang  : {luas_lubang:.2f}",       -0.85, -0.20)
hud(f"  Selimut : {selimut_kerucut:.2f}",   -0.85, -0.25)
hud(f"  Sisa    : {luas_sisa:.2f}",         -0.85, -0.30, color.rgba(100,255,150,220))
hud("-----------------------------------",  -0.85, -0.39, color.rgba(0,180,255,100), 0.60)
hud("[LMB] Rotate  [Scroll] Zoom  [R] Reset  [SPACE] Pause  [ESC] Exit",
                                            -0.85, -0.44, color.rgba(120,220,255,160), 0.60)

Entity(
    parent = camera.ui,
    model  = 'quad',
    color  = color.rgba(0, 20, 40, 20),
    scale  = (2, 2),
    z      = 1,
)

# =========================================================
# STATE
# =========================================================
drag_sensitivity = 80
auto_rotate      = True
auto_rotate_speed = 8
flicker_timer    = 0.0

# =========================================================
# INPUT HANDLER — didefinisikan SETELAH builtin input() selesai
# =========================================================
def input(key):
    global auto_rotate
    if key == 'scroll up':
        camera.z = min(camera.z + R * 0.4, ZOOM_MAX)
    elif key == 'scroll down':
        camera.z = max(camera.z - R * 0.4, ZOOM_MIN)
    elif key == 'space':
        auto_rotate = not auto_rotate
        print("[AUTO-ROTATE]", "ON" if auto_rotate else "OFF")
    elif key == 'r':
        hologram.rotation = Vec3(0, 0, 0)
        auto_rotate = True
    elif key == 'escape':
        sys.exit()

# =========================================================
# UPDATE LOOP
# =========================================================
def update():
    global flicker_timer
    t  = time.time()
    dt = time.dt

    if auto_rotate and not mouse.left:
        hologram.rotation_y += dt * auto_rotate_speed

    if mouse.left:
        hologram.rotation_y += mouse.velocity[0] * drag_sensitivity
        hologram.rotation_x -= mouse.velocity[1] * drag_sensitivity

    for i, (ring, speed) in enumerate(rings):
        ring.rotation_z += dt * (25 + i * 15) * speed
        pulse = sin(t * 1.8 + i) * 0.3 + 0.7
        ring.alpha = pulse

    cone_rim.alpha = 0.7 + sin(t * 4) * 0.3

    glow_g = 100 + int(sin(t * 4) * 40)
    cone_glow.color = color.rgba(255, glow_g, 20, 110)

    cube_shell.scale = R * (1.02 + sin(t * 1.5) * 0.005)

    flicker_timer += dt
    if flicker_timer > (2.5 + sin(t * 0.3) * 1.5):
        flicker_timer = 0.0
        cube_solid.color = color.rgba(0, 180, 255, 25)
        invoke(lambda: setattr(cube_solid, 'color', color.rgba(0, 160, 255, 85)), delay=0.08)

# =========================================================
# RUN
# =========================================================
print()
print("=== HOLOGRAM ONLINE ===")
print(f"Volume Sisa : {volume_sisa:.2f}")
print(f"Luas Sisa   : {luas_sisa:.2f}")
print("========================")

app.run()