# -*- coding: utf-8 -*-
'''
@File    :   ttsFactory.py
@Author  :   zinohome 
'''

from ..builder import TTSEngines
from ..engineBase import BaseEngine
from typing import List
from yacs.config import CfgNode as CN
from aiengine.protocol import ENGINE_TYPE
from aiengine.utils import log

__all__ = ["TTSFactory"]

class TTSFactory():
    """
    Text to Speech Factory
    """
    @staticmethod
    def create(config: CN) -> BaseEngine:
        if config.NAME in TTSEngines.list():
            log.info(f"[TTSFactory] Create engine: {config.NAME}")
            return TTSEngines.get(config.NAME)(config, ENGINE_TYPE.TTS)
        else:
            raise RuntimeError(f"[TTSFactory] Please check config, support TTS: {TTSEngines.list()}, but get {config.NAME}")
    @staticmethod
    def list() -> List:
        return TTSEngines.list()