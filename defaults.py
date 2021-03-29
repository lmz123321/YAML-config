# simulation of using yaml
import os
from yacs.config import CfgNode as CN

_C = CN()

_C.MODEL = CN()
_C.MODEL.ARCH = "ASPP"
_C.MODEL.BACKBONE = "UNet"

_C.INPUT = CN()
_C.INPUT.SIZE_CLS = 48
_C.INPUT.SIZE_DET = 96
_C.INPUT.PADDING = 170

_C.SOLVER = CN()
_C.SOLVER.BATCH_SIZE_CLS = 16
_C.SOLVER.BATCH_SIZE_DET = 16
_C.SOLVER.BASE_LR = 0.01
_C.SOLVER.MOMENTUM  = 0.00001

_C.DATA = CN()
_C.DATA.TYPE = 'TYPE1'
_C.DATA.PATH = '/path/path/TYPE1/'
