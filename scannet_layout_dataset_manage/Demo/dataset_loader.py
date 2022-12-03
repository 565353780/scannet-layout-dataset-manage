#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scannet_layout_dataset_manage.Module.dataset_loader import DatasetLoader


def demo():
    scannet_layout_dataset_folder_path = "/home/chli/chLi/ScanNetLayout/"
    print_progress = True

    dataset_loader = DatasetLoader(scannet_layout_dataset_folder_path,
                                   print_progress)
    return True
