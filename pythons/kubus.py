import sys
import os
import math
from math import sin, cos, pi
from pathlib import Path

# ── STEP 1: Panda3D config — HARUS sebelum semua import Ursina
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'load-display pandagl')
loadPrcFileData('', 'aux-display p3tinydisplay')

# ── STEP 2: asset_folder — HARUS sebelum Ursina()
import ursina
from ursina import application
application.asset_folder = Path(os.path.abspath(__file__)).parent

from ursina import *

# =========================================================
# INPUT — builtin input() DIPANGGIL SEBELUM def input(key)
# =========================================================
print("=== SETYASA HOLOGRAM VIEWER v5.1 ===")

try:
    R = float(input("Masukkan sisi kubus (R): "))
    r = float(input("Masukkan jari-jari kerucut (r): "))
    h = float(input("Masukkan tinggi kerucut (h): "))
except ValueError:
    print("[ERROR] Pakai default: R=3, r=0.8, h=2")
    R, r, h = 3.0, 0.8, 2.0

if r >= R / 2:
    r = R / 2 * 0.8
if h > R:
    h = R * 0.9

# =========================================================
# PERHITUNGAN GEOMETRI
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
    title      = "STARK INDUSTRIES HOLOGRAM CAD",
    borderless = False,
    fullscreen = False,
    vsync      = True,
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
# PROCEDURAL MESH BUILDERS
# Dibuat SETELAH app = Ursina() agar Panda3D context sudah ready
# =========================================================

def make_cone_mesh(segments=24):
    verts, tris = [], []
    verts.append((0, 0.5, 0))       # tip = index 0
    for i in range(segments):
        a = 2 * pi * i / segments
        verts.append((cos(a)*0.5, -0.5, sin(a)*0.5))
    # sisi
    for i in range(segments):
        ni = (i + 1) % segments
        tris.append((0, i+1, ni+1))
    # alas
    bc = len(verts)
    verts.append((0, -0.5, 0))
    for i in range(segments):
        ni = (i + 1) % segments
        tris.append((bc, ni+1, i+1))
    return Mesh(vertices=verts, triangles=tris, mode='triangle')

def make_ring_mesh(segments=48, thickness=0.03):
    verts, tris = [], []
    inner = 0.5 - thickness
    outer = 0.5
    for i in range(segments):
        a = 2 * pi * i / segments
        verts.append((cos(a)*outer, 0, sin(a)*outer))
        verts.append((cos(a)*inner, 0, sin(a)*inner))
    for i in range(segments):
        i2 = (i + 1) % segments
        o1 = i * 2;     i1 = i * 2 + 1
        o2 = i2 * 2;    i3 = i2 * 2 + 1
        tris.extend([(o1, o2, i3), (o1, i3, i1)])
    return Mesh(vertices=verts, triangles=tris, mode='triangle')

def make_wire_box_mesh(size=1.0):
    """
    Buat wireframe kubus sebagai satu Mesh dengan mode='line'
    — jauh lebih ringan dari 12 entity cube terpisah.
    """
    h2 = size / 2
    verts = [
        (-h2,-h2,-h2), ( h2,-h2,-h2), ( h2, h2,-h2), (-h2, h2,-h2),  # front
        (-h2,-h2, h2), ( h2,-h2, h2), ( h2, h2, h2), (-h2, h2, h2),  # back
    ]
    lines = [
        0,1, 1,2, 2,3, 3,0,   # front face
        4,5, 5,6, 6,7, 7,4,   # back face
        0,4, 1,5, 2,6, 3,7,   # connectors
    ]
    return Mesh(vertices=verts, triangles=lines, mode='line')

# =========================================================
# BUILD MESHES (setelah app init)
# =========================================================
cone_mesh  = make_cone_mesh()
ring_mesh  = make_ring_mesh(segments=48, thickness=0.025)
rim_mesh   = make_ring_mesh(segments=48, thickness=0.04)
wire_mesh  = make_wire_box_mesh(size=1.0)

# =========================================================
# ROOT ENTITY
# =========================================================
hologram = Entity()

# =========================================================
# KUBUS — solid + shell + wireframe
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
    color  = color.rgba(30, 200, 255, 18),
    scale  = R * 1.022,
)
# Wireframe: satu mesh, bukan 12 entity terpisah
cube_wire = Entity(
    parent = hologram,
    model  = wire_mesh,
    color  = color.rgba(0, 255, 255, 220),
    scale  = R * 1.005,
)

# =========================================================
# CORNER MARKERS — 8 titik sudut
# =========================================================
half = R / 2
for cx in (-half, half):
    for cy in (-half, half):
        for cz in (-half, half):
            Entity(
                parent   = hologram,
                model    = 'cube',
                color    = color.rgba(0, 255, 255, 200),
                scale    = R * 0.04,
                position = Vec3(cx, cy, cz),
            )

# =========================================================
# KERUCUT — embedded di dalam kubus
# cone_y: alas di permukaan atas kubus, tip masuk ke bawah
# =========================================================
cone_y = (R / 2) - (h / 2)

cone_dark = Entity(
    parent     = hologram,
    model      = cone_mesh,
    color      = color.rgba(3, 6, 15, 235),
    scale      = (r*2, h, r*2),
    rotation_x = 180,
    y          = cone_y,
)
cone_glow = Entity(
    parent     = hologram,
    model      = cone_mesh,
    color      = color.rgba(255, 100, 20, 100),
    scale      = (r*1.8, h*0.96, r*1.8),
    rotation_x = 180,
    y          = cone_y,
)
cone_rim = Entity(
    parent = hologram,
    model  = rim_mesh,
    color  = color.rgba(255, 160, 50, 200),
    scale  = r * 2.2,
    y      = R / 2 + 0.005,
)

# =========================================================
# GLOW RINGS
# =========================================================
ring_configs = [
    (1.6,  0, color.rgba(0, 255, 255, 100), 1.0),
    (1.4, 30, color.rgba(0, 180, 255,  80), 1.3),
    (1.2, 60, color.rgba(0, 255, 180,  60), 0.7),
]
rings = []
for scale_mul, rx, col, speed in ring_configs:
    ring = Entity(
        parent     = hologram,
        model      = ring_mesh,
        color      = col,
        scale      = R * scale_mul,
        rotation_x = rx,
    )
    rings.append((ring, speed))

# =========================================================
# HUD
# =========================================================
def hud(txt, x, y, col=color.cyan, sc=0.7):
    return Text(text=txt, x=x, y=y, color=col, scale=sc, parent=camera.ui)

hud("STARK INDUSTRIES  |  HOLOGRAM CAD",  -0.85,  0.45, color.rgba(0,255,255,220), 0.80)
hud("-----------------------------------", -0.85,  0.42, color.rgba(0,180,255,100), 0.60)
hud(f"CUBE SIDE   : {R:.2f}",             -0.85,  0.36)
hud(f"CONE RADIUS : {r:.2f}",             -0.85,  0.31)
hud(f"CONE HEIGHT : {h:.2f}",             -0.85,  0.26)
hud("-----------------------------------", -0.85,  0.22, color.rgba(0,180,255,100), 0.60)
hud("VOLUME ANALYSIS",                     -0.85,  0.16, color.rgba(255,200,50,220), 0.75)
hud(f"  Kubus   : {volume_kubus:.2f}",     -0.85,  0.11)
hud(f"  Kerucut : {volume_kerucut:.2f}",   -0.85,  0.06)
hud(f"  Sisa    : {volume_sisa:.2f}",      -0.85,  0.01, color.rgba(100,255,150,220))
hud("-----------------------------------", -0.85, -0.04, color.rgba(0,180,255,100), 0.60)
hud("SURFACE ANALYSIS",                    -0.85, -0.10, color.rgba(255,200,50,220), 0.75)
hud(f"  Kubus   : {luas_kubus:.2f}",       -0.85, -0.15)
hud(f"  Lubang  : {luas_lubang:.2f}",      -0.85, -0.20)
hud(f"  Selimut : {selimut_kerucut:.2f}",  -0.85, -0.25)
hud(f"  Sisa    : {luas_sisa:.2f}",        -0.85, -0.30, color.rgba(100,255,150,220))
hud("-----------------------------------", -0.85, -0.39, color.rgba(0,180,255,100), 0.60)
hud("[LMB] Rotate  [Scroll] Zoom  [R] Reset  [SPACE] Pause  [ESC] Exit",
                                           -0.85, -0.44, color.rgba(120,220,255,160), 0.58)

# =========================================================
# STATE
# =========================================================
drag_sensitivity  = 80
auto_rotate       = True
auto_rotate_speed = 8
flicker_timer     = 0.0
cube_solid_normal = color.rgba(0, 160, 255, 85)   # simpan warna normal

# =========================================================
# INPUT HANDLER — SETELAH semua builtin input() selesai
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
        application.quit()

# =========================================================
# UPDATE LOOP
# =========================================================
def update():
    global flicker_timer
    t  = time.time()
    dt = time.dt

    # Auto-rotate
    if auto_rotate and not mouse.left:
        hologram.rotation_y += dt * auto_rotate_speed

    # Mouse drag
    if mouse.left:
        hologram.rotation_y += mouse.velocity[0] * drag_sensitivity
        hologram.rotation_x -= mouse.velocity[1] * drag_sensitivity

    # Rings
    for i, (ring, speed) in enumerate(rings):
        ring.rotation_y += dt * (20 + i * 12) * speed
        ring.alpha = sin(t * 1.8 + i) * 0.3 + 0.7

    # Cone rim spin
    cone_rim.rotation_y += dt * 40
    cone_rim.alpha = 0.7 + sin(t * 4) * 0.3

    # Cone glow pulse — gunakan warna baru tiap frame, tanpa invoke
    glow_g = 100 + int(sin(t * 4) * 40)
    cone_glow.color = color.rgba(255, glow_g, 20, 100)

    # Shell breathing
    cube_shell.scale = R * (1.022 + sin(t * 1.5) * 0.004)

    # Hologram flicker — tanpa lambda/invoke untuk menghindari crash
    flicker_timer += dt
    if flicker_timer > 2.5 + sin(t * 0.3) * 1.5:
        flicker_timer = 0.0
        cube_solid.color = color.rgba(0, 180, 255, 20)

    # Restore flicker setelah 0.08s dengan counter sederhana
    if cube_solid.color[3] < 0.4 and flicker_timer > 0.08:
        cube_solid.color = cube_solid_normal

# =========================================================
# RUN
# =========================================================
print(f"\n=== HOLOGRAM ONLINE ===")
print(f"Volume Sisa : {volume_sisa:.2f}")
print(f"Luas Sisa   : {luas_sisa:.2f}")
print("========================\n")

app.run()