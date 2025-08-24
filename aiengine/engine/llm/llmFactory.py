# -*- coding: utf-8 -*-
'''
@File    :   ttsFactory.py
@Author  :   zinohome 
'''

from ..builder import LLMEngines
from ..engineBase import BaseEngine
from typing import List
from yacs.config import CfgNode as CN
from aiengine.protocol import ENGINE_TYPE
from aiengine.utils import log

__all__ = ["LLMFactory"]

class LLMFactory():
    """
    Large Language Model Factory
    """
    @staticmethod
    def create(config: CN) -> BaseEngine:
        if config.NAME in LLMEngines.list():
            log.info(f"[LLMFactory] Create engine: {config.NAME}")
            return LLMEngines.get(config.NAME)(config, ENGINE_TYPE.LLM)
        else:
            raise RuntimeError(f"[LLMFactory] Please check config, support LLM: {LLMEngines.list()}")
    @staticmethod
    def list() -> List:
        return LLMEngines.list()