#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def getLayoutDepthImage(view):
    layout_depth_npy_file_path = view.layout_depth_npy_file_path
    layout_depth_image = np.load(layout_depth_npy_file_path)
    max_depth = np.max(layout_depth_image)
    layout_depth_image = layout_depth_image * 255.0 / max_depth
    layout_depth_image = layout_depth_image.astype(np.uint8)
    return layout_depth_image
