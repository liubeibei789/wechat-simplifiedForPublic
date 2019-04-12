#!/usr/bin/python

import Record

class Person:

   ID = ''
   name = ''
   timeBeFriends = None
   msgList = []
   recordList = []
   numRecord = 0

   def setID(self, ID):
      self.ID = ID

   def setName(self, name):
      self.name = name

   def setTimeBeFriends(self, timeBeFriends):
      self.timeBeFriends = timeBeFriends.split()

   def addMsgList(self, msg):
      self.msgList.append(msg)

   def delMsgList(self):
      del self.msgList[:]

   def addRecordList(self, record):
      self.recordList.append(record)

   def delRecordList(self):
      del self.recordList[:]

   def setNumRecord(self, numRecord):
      self.numRecord = numRecord

#=============================

   def getID(self):
      return self.ID

   def getName(self):
      return self.name

   def getTimeBeFriends(self):
      return self.timeBeFriends

   def getMsgList(self):
      return self.msgList

   def getRecordList(self):
      return self.recordList

   def getNumRecord(self):
      return self.numRecord


