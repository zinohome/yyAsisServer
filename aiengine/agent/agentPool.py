# -*- coding: utf-8 -*-
'''
@File    :   AgentPool.py
@Author  :   zinohome 
'''

from threading import RLock
from typing import List
from yacs.config import CfgNode as CN
from aiengine.utils import log
from .agentBase import BaseAgent
from .core import AgentFactory

__all__ = ["AgentPool"]

class AgentPool():
    singleLock = RLock()
    _init = False

    def __init__(self):
        if not self._init:
            self._pool = dict()
            self._init = True
    
    # Single Instance
    def __new__(cls, *args, **kwargs):
        with AgentPool.singleLock:
            if not hasattr(cls, '_instance'):
                AgentPool._instance = super().__new__(cls)
        return AgentPool._instance

    def __del__(self):
        self._pool.clear()
        self._init = False
    
    def setup(self, config: CN):
        for cfg in config.SUPPORT_LIST:
            self._pool[cfg.NAME] = AgentFactory.create(cfg)
            log.info(f"[AgentPool] AGENT Engine {cfg.NAME} is created.")
        log.info(f"[AgentPool] AGENT Engine default is {config.DEFAULT}.")
            
    def get(self, name: str) -> BaseAgent:
        if name not in self._pool:
            raise KeyError(f"[AgentPool] No such engine: {name}") 
        return self._pool[name]

    def list(self) -> List[str]:
        return list(self._pool.keys())