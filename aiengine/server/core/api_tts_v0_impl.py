# -*- coding: utf-8 -*-
'''
@File    :   tts_api_v0_impl.py
@Author  :   zinohome
'''


from typing import List, Dict
from aiengine.engine import EnginePool, BaseTTSEngine
from aiengine.utils import config
from aiengine.protocol import ParamDesc, EngineDesc, ENGINE_TYPE, UserDesc, AudioMessage, TextMessage, VoiceDesc
from aiengine.server.models import TTSEngineInput

enginePool = EnginePool()

def get_tts_list() -> List[EngineDesc]:
    engines = enginePool.listEngine(ENGINE_TYPE.TTS)
    return [enginePool.getEngine(ENGINE_TYPE.TTS, engine).desc() for engine in engines]

def get_tts_default() -> EngineDesc:
    return enginePool.getEngine(ENGINE_TYPE.TTS, config.SERVER.ENGINES.TTS.DEFAULT).desc()

async def get_tts_voice(name: str, **kwargs) -> List[VoiceDesc]:
    engine: BaseTTSEngine = enginePool.getEngine(ENGINE_TYPE.TTS, name)
    voices = await engine.voices(**kwargs)
    return voices

def get_tts_param(name: str) -> List[ParamDesc]:
    engine = enginePool.getEngine(ENGINE_TYPE.TTS, name)
    return engine.parameters()

async def tts_infer(user: UserDesc, item: TTSEngineInput) -> AudioMessage:
    if item.engine.lower() == "default":
        item.engine = config.SERVER.ENGINES.TTS.DEFAULT
    input = TextMessage(data=item.data)
    engine = enginePool.getEngine(ENGINE_TYPE.TTS, item.engine)
    output: AudioMessage = await engine.run(input=input, user=user, **item.config)
    return output