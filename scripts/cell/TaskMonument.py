# -*- coding: utf-8 -*-
import KBEngine
import prop_data
import store_data
import zuanshi_data
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject


class TaskMonument(KBEngine.Entity, EntityObject):
    def __init__(self):
        DEBUG_MSG("TaskMonument:__init__")
