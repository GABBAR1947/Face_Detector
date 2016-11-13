#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Distributed under terms of the MIT license.

"""
This code is responsible for the creation of a dataset

"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import os, os.path

def create_train(path):

    path_image = [os.path.join(path,i) for i in os.listdir(path)]

