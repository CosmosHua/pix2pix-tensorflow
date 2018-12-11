# coding:utf-8
# !/usr/bin/python3

import numpy as np
import os, cv2, random


################################################################################
def combine(in_folder, out_folder, mod="AtoB"):
    for f in os.listdir(in_folder):
        A = cv2.imread(os.path.join(in_folder,f))
        B = np.zeros(A.shape)
        if mod=="AtoB": B = np.concatenate((A,B),axis=1)
        elif mod=="BtoA": B = np.concatenate((B,A),axis=1)
        cv2.imwrite(os.path.join(out_folder,f), B)


################################################################################
if __name__ == "__main__":
    path = "Test/"; out = "test/"
    combine(path, out, "AtoB")
