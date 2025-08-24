# -*- coding: utf-8 -*-
'''
@File    :   app.py
@Author  :   zinohome 
'''

import uvicorn
from aiengine.engine import EnginePool
from aiengine.agent import AgentPool
from aiengine.server import app
from aiengine.utils import config

__all__ = ["runServer"]

def runServer():
    enginePool = EnginePool()
    enginePool.setup(config.SERVER.ENGINES)
    agentPool = AgentPool()
    agentPool.setup(config.SERVER.AGENTS)
    uvicorn.run(app, host=config.SERVER.IP, port=config.SERVER.PORT, log_level="info")