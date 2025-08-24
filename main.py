# -*- coding: utf-8 -*-
'''
@File    :   main.py
@Author  :   zinohome 
'''

from aiengine.utils import log, config
from aiengine.bin import runServer

def showEnv():
    log.info(f"[System] Welcome to Awesome digitalHuman System")
    log.info(f"[System] Runing config:\n{config}")


if __name__ == '__main__':
    showEnv()
    runServer()
