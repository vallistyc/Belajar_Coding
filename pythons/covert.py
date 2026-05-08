import ursina
from pathlib import Path
from panda3d.core import Filename, LoaderOptions, ModelPool
from direct.showbase.ShowBase import ShowBase

base = ShowBase()

models_dir = Path(ursina.__file__).parent / 'models'
blend_files = list(models_dir.glob('*.blend'))
egg_files   = list(models_dir.glob('*.egg'))
gltf_files  = list(models_dir.glob('*.gltf'))

print(f"Models dir: {models_dir}")
print(f".blend : {len(blend_files)}")
print(f".egg   : {len(egg_files)}")
print(f".gltf  : {len(gltf_files)}")

for f in blend_files + egg_files + gltf_files:
    print(f"Loading: {f.name} ...", end=" ")
    try:
        base.loader.loadModel(str(f))
        print("OK")
    except Exception as e:
        print(f"FAIL: {e}")

print("Done.")