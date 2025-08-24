# -*- coding: utf-8 -*-
'''
@File    :   engineBase.py
@Author  :   zinohome 
'''

from fastapi import WebSocket
from typing import List
from abc import abstractmethod
from aiengine.core import BaseRunner
from aiengine.protocol import BaseMessage, TextMessage, AudioMessage, VoiceDesc

__all__ = ["BaseEngine"]

class BaseEngine(BaseRunner):
    @abstractmethod
    async def run(self, input: BaseMessage, **kwargs) -> BaseMessage:
        raise NotImplementedError

class BaseLLMEngine(BaseEngine):
    @abstractmethod
    async def run(self, input, streaming: bool = True, **kwargs):
        raise NotImplementedError

class BaseASREngine(BaseEngine):
    @abstractmethod
    async def run(self, input: AudioMessage, **kwargs) -> TextMessage:
        raise NotImplementedError

class BaseTTSEngine(BaseEngine):
    async def voices(self, **kwargs) -> List[VoiceDesc]:
        return []

    @abstractmethod
    async def run(self, input: TextMessage, **kwargs) -> AudioMessage:
        raise NotImplementedError

class StreamBaseEngine(BaseEngine):
    @abstractmethod
    async def run(self, websocket: WebSocket, **kwargs) -> None:
        raise NotImplementedError
