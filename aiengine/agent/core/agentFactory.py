# -*- coding: utf-8 -*-
'''
@File    :   agentFactory.py
@Author  :   zinohome 
'''

from ..builder import AGENTS
from ..agentBase import BaseAgent
from typing import List
from yacs.config import CfgNode as CN
from aiengine.utils import log
from aiengine.protocol import ENGINE_TYPE

class AgentFactory():
    """
    Agent Factory
    """
    @staticmethod
    def create(config: CN) -> BaseAgent:
        if config.NAME in AGENTS.list():
            log.info(f"[AgentFactory] Create instance: {config.NAME}")
            return AGENTS.get(config.NAME)(config, ENGINE_TYPE.AGENT)
        else:
            raise RuntimeError(f"[AgentFactory] Please check config, support AGENT engine: {AGENTS.list()}")
    @staticmethod
    def list() -> List:
        return AGENTS.list()