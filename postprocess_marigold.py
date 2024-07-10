import shutil
from glob import glob

import cv2
import numpy as np

postfix = "marigold-lcm"
marigold_exp_path = "/local-scratch2/diliash/diorama/third_party/Marigold/output/marigold_preprocessed_wss_lcm"
exp_path = "/local-scratch2/diliash/diorama/third_party/Inpaint-Anything/results/gt-rerun-vis-pcd/merged"

scene_dirs = glob(f"{exp_path}/*")
for scene_dir in scene_dirs:
    scene_id = scene_dir.split("/")[-1]

    marigold_bw_depth_path = f"{marigold_exp_path}/depth_bw/{scene_id}_pred.png"
    marigold_inpainted_bw_depth_path = f"{marigold_exp_path}/depth_bw/{scene_id}_inpainted_pred.png"

    marigold_color_depth_path = f"{marigold_exp_path}/depth_colored/{scene_id}_pred_colored.png"
    marigold_inpainted_color_depth_path = f"{marigold_exp_path}/depth_colored/{scene_id}_inpainted_pred_colored.png"

    marigold_npy_depth_path = f"{marigold_exp_path}/depth_npy/{scene_id}_pred.npy"
    marigold_inpainted_npy_depth_path = f"{marigold_exp_path}/depth_npy/{scene_id}_inpainted_pred.npy"

    # Copy everyting with appropriate names to exp_path
    shutil.copy(marigold_bw_depth_path, f"{exp_path}/{scene_id}/inpainted-scene-gt-depth-{postfix}.png")
    shutil.copy(marigold_inpainted_bw_depth_path, f"{exp_path}/{scene_id}/inpainted-scene-depth-{postfix}.png")

    shutil.copy(marigold_color_depth_path, f"{exp_path}/{scene_id}/inpainted-scene-gt-depth-color-{postfix}.png")
    shutil.copy(marigold_inpainted_color_depth_path, f"{exp_path}/{scene_id}/inpainted-scene-depth-color-{postfix}.png")

    shutil.copy(marigold_npy_depth_path, f"{exp_path}/{scene_id}/inpainted-scene-gt-depth-{postfix}.npy")
    shutil.copy(marigold_inpainted_npy_depth_path, f"{exp_path}/{scene_id}/inpainted-scene-depth-{postfix}.npy")
