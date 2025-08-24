# -*- coding: utf-8 -*-
'''
@File    :   repeaterAgnet.py
@Author  :   zinohome 
'''

from ..builder import AGENTS
from ..agentBase import BaseAgent
from aiengine.protocol import *

__all__ = ["Repeater"]


@AGENTS.register("Repeater")
class RepeaterAgent(BaseAgent):
    async def run(
        self, 
        input: TextMessage, 
        **kwargs
    ):
        yield eventStreamText(input.data)
        yield eventStreamDone()