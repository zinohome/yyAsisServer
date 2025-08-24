# -*- coding: utf-8 -*-
'''
@File    :   asrFactory.py
@Author  :   zinohome 
'''

from ..builder import ASREngines
from ..engineBase import BaseEngine
from typing import List
from yacs.config import CfgNode as CN
from aiengine.protocol import ENGINE_TYPE
from aiengine.utils import log

__all__ = ["ASRFactory"]

class ASRFactory():
    """
    Automatic Speech Recognition Factory
    """
    @staticmethod
    def create(config: CN) -> BaseEngine:
        if config.NAME in ASREngines.list():
            log.info(f"[ASRFactory] Create engine: {config.NAME}")
            return ASREngines.get(config.NAME)(config, ENGINE_TYPE.ASR)
        else:
            raise RuntimeError(f"[ASRFactory] Please check config, support ASR engine: {ASREngines.list()}")
    @staticmethod
    def list() -> List:
        return ASREngines.list()