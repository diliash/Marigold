import os
import shutil
from glob import glob

output_dir = "./marigold_preprocessed_wss"
os.makedirs(output_dir, exist_ok=True)

data_path = "/project/3dlg-hcvc/diorama/wss/scenes"
model_dirs = glob(f"{data_path}/*")

for model_dir in model_dirs:
    model_id = os.path.basename(model_dir)
    scene_path = f"{model_dir}/scene.png"

    # copy scene.png
    shutil.copy(scene_path, f"{output_dir}/{model_id}.png")

