# -*- coding:utf-8 -*-
import os, os.path as osp
import time

def strftime(t = None):
    return time.strftime("%d-%m-%Y[%Hh%Mm%Ss]", time.localtime(t or time.time()))

#################
# Logging
#################
import logging
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(format="[%(asctime)s][%(module)s.%(funcName)s][%(levelname)s] %(message)s")

DEFAULT_LEVEL = logging.DEBUG
DEFAULT_LOGGING_DIR = "logs"
fh = None

def init_fh():
    global fh, DEFAULT_LOGGING_DIR
    if fh is not None:
        return
    if DEFAULT_LOGGING_DIR is None:
        return
    if not osp.exists(DEFAULT_LOGGING_DIR): os.makedirs(DEFAULT_LOGGING_DIR)
    logging_path = osp.join(DEFAULT_LOGGING_DIR, strftime() + ".log")
    fh = logging.FileHandler(logging_path)
    fh.setFormatter(logging.Formatter("[%(asctime)s][%(module)s.%(funcName)s][%(levelname)s] %(message)s"))

def update_default_level(level):
    global DEFAULT_LEVEL
    DEFAULT_LEVEL = level

def update_default_logging_dir(logging_dir):
    global DEFAULT_LOGGING_DIR
    DEFAULT_LOGGING_DIR = logging_dir

def get_logger(name="log", level=None):
    global DEFAULT_LEVEL
    level = level or DEFAULT_LEVEL
    logger = logging.getLogger(name)
    logger.setLevel(level)
    init_fh()
    if fh is not None:
        logger.addHandler(fh)
    return logger