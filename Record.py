#!/usr/bin/python

class Record:

   date = None
   time = None
   sndRcv = None
   msg = ''

   def setDateAndTime(self, dateAndTime):
      dateAndTime = dateAndTime.split()
      self.date = dateAndTime[0]
      self.time = dateAndTime[1]

   def setSndRcv(self, sndRcv):
      self.sndRcv = sndRcv

   def setMsg(self, msg):
      self.msg = msg
#=============================

   def getDateAndTime(self):
      return self.date, self.time

   def getSndRcv(self):
      return self.sndRcv

   def getMsg(self):
      return self.msg