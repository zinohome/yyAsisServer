# -*- coding: utf-8 -*-
'''
@File    :   engineBase.py
@Author  :   一力辉 
'''

from uuid import uuid4
from abc import abstractmethod
from aiengine.protocol import BaseMessage
from aiengine.core import BaseRunner

__all__ = ["BaseAgent"]

class BaseAgent(BaseRunner):
    async def createConversation(self, **kwargs) -> str:
        return str(uuid4())

    @abstractmethod
    async def run(self, input: BaseMessage, **kwargs):
        raise NotImplementedError  