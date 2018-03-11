# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
from PROP_LIST import TProp
from PROP_LIST import TPropList
import json
import PyDatas.prop_config_Table as prop_config_Table
import PyDatas.store_config_Table as store_config_Table
import copy




class MagicWeaponSystem:
    def __init__(self):
        DEBUG_MSG("MagicWeaponSystem:__init__")
        self.freeIndexSet = []
        for i in range(0, 9):
            self.freeIndexSet.insert(0, i)
        for propUUID, prop in self.magicWeaponList.items():
            self.freeIndexSet.remove(prop["index"])
        DEBUG_MSG(self.freeIndexSet)
    #     propUUIDList = self.getPropUUIDList()
    #     for propUUID, prop in self.propList.items():
    #         propData = json.loads(prop["propData"])
    #         if propData["type"] == 2:
    #             if propUUID not in propUUIDList:
    #                 self.addMagicWeapon(propUUID, prop["propData"])


    # def calculateFreeIndexSet(self):
    #     DEBUG_MSG("MagicWeaponSystem:calculateFreeIndexSet")
    #     freeIndexSet = []
    #     removeIndexSet = []
    #     for i in range(8, -1, -1):
    #         freeIndexSet.append(i)
    #     for index, weaponProp in self.magicWeaponList.items():
    #         if weaponProp["propUUID"] not in self.propList:
    #             removeIndexSet.append(index)
    #             continue
    #         freeIndexSet.remove(index)
    #     for index in removeIndexSet:
    #         del self.magicWeaponList[index]
    #     return freeIndexSet


    # def getPropUUIDList(self):
    #     DEBUG_MSG("MagicWeaponSystem:getPropUUIDList")
    #     propUUIDList = []
    #     for index, weaponProp in self.magicWeaponList.items():
    #         propUUIDList.append(weaponProp["propUUID"])
    #     return propUUIDList


    def onAddProp(self, prop):
        DEBUG_MSG("MagicWeaponSystem:onAddProp")
        propData = json.loads(prop["propData"])
        if propData["type"] == 2:
            self.addMagicWeapon(prop["propUUID"], prop["propData"])


    def onRemoveProp(self, propUUID):
        DEBUG_MSG("MagicWeaponSystem:onRemoveProp")
        self.removeMagicWeapon(propUUID)


    def addMagicWeapon(self, propUUID, jsonData):
        DEBUG_MSG("MagicWeaponSystem:addMagicWeapon")
        weaponProp = TProp()
        weaponProp["index"] = self.freeIndexSet.pop()
        weaponProp["propUUID"] = propUUID
        weaponProp["propData"] = jsonData
        self.magicWeaponList[propUUID] = weaponProp


    def removeMagicWeapon(self, propUUID):
        DEBUG_MSG("MagicWeaponSystem:addMagicWeapon")
        index = self.magicWeaponList[propUUID]["index"]
        self.freeIndexSet.insert(0, index)
        del self.magicWeaponList[propUUID]
