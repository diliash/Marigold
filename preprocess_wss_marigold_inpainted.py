import os
import shutil
from glob import glob

output_dir = "./marigold_preprocessed_wss"
os.makedirs(output_dir, exist_ok=True)

exp_dir = "/local-scratch2/diliash/diorama/third_party/Inpaint-Anything/results/gt-rerun-vis-pcd/merged"
model_dirs = glob(f"{exp_dir}/*")

for model_dir in model_dirs:
    model_id = os.path.basename(model_dir)
    scene_path = f"{model_dir}/inpainted_merged.png"

    # copy scene.png
    shutil.copy(scene_path, f"{output_dir}/{model_id}_inpainted.png")
