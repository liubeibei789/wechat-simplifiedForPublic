#!/usr/bin/python
 # -*- coding: utf-8 -*-
import glob
import os
import sys

import Person
import Record

import xlsxwriter

reload(sys)  
sys.setdefaultencoding('utf8')


personList = []

def readPerson(file_path):

   with open(file_path) as fp:
      contents = fp.readlines()
      
      isFirstLine = True
      person = Person.Person()
      person.delMsgList()
      person.delRecordList()

      for line in contents:
         record = Record.Record()

         if "e029d1bf418527382ef2247e4d95a6a3" in line:
            line = line.replace("e029d1bf418527382ef2247e4d95a6a3", "Beibei    ")
         if not ("－－－" in line or "ID" in line or "Wechat messages" in line):
            # get a valid record
            while line.replace("   ", "  ") != line:
               line = line.replace("   ", "  ")
            fields = line.split("  ")

            if "<" in fields[0] and "/>" in fields[0]:
               print "8888"
               break;

            # parse the record
            # fields 0:ID, 1:dateAndTime, 2:name, 4:sndRcv, 6:msg

            record.setDateAndTime(fields[1])
            record.setSndRcv(fields[4])
            record.setMsg(fields[6])

            if True == isFirstLine and "Beibei" not in fields[0]:
               person.setID(fields[0])
               person.setName(fields[2])
               person.setTimeBeFriends(fields[1])
               isFirstLine = False

            person.addMsgList(fields[6])
            person.addRecordList(record)

      #print "------- msgList -------"
      numRecord = 0
      msgList = person.getMsgList()
      for msg in msgList:
         #print msg
         numRecord += 1
      print "###### total", numRecord
      person.setNumRecord(numRecord)
      personList.append(person)
      #print "******* recordList ******"
      #recordList = person.getRecordList()
      #for record in recordList:
         #print record
   status = 0

   return status, person
            

def readAll():

   numPerson = 0
   
   fileList = glob.glob("./data/*.txt")
   nameList = []

   reload(sys)  
   sys.setdefaultencoding('utf8')

   

   for file in fileList:

      try:
         status, person = readPerson(file)
         #personList.append(person)
      except:
         print "error processing "+ file
         os.system("rm "+file)
      finally:
         pass


      file = file.split("/")[2]
      file = file.split(".")[0]
      nameList.append(file)
      numPerson += 1
      


   print "final numPerson=", numPerson
   return nameList


def write2Xls(nameList):
   # Create a workbook and add a worksheet.
   workbook = xlsxwriter.Workbook('myFriends.xlsx')
   worksheet = workbook.add_worksheet()

   
   printNames = []
   printIDs = []
   printDates = []
   printNumRecord = []
   

   for person in personList:
      print "now processing person ", person.getName()
      printNames.append(person.getName())
      printIDs.append(person.getID())

      try: 
         date = person.getTimeBeFriends()[0]
         printDates.append(date)
      except:
         date = "NA/NA/NA"
         printDates.append(date)

      numRecord = person.getNumRecord()

      print "numRecord...",numRecord
      printNumRecord.append(numRecord)
   
   # Iterate over the data and write it out row by row.
   worksheet.write(0, 0, "Name")
   worksheet.write(0, 1, "Wechat ID")
   worksheet.write(0, 2, "DateBeFriends")
   worksheet.write(0, 3, "MessageNum")
      
   row = 1
   for item in printNames:
      worksheet.write(row, 0, item)
      row += 1

   row = 1
   for item in printIDs:
      worksheet.write(row, 1, item)
      row += 1

   row = 1
   for item in printDates:
      worksheet.write(row, 2, item)
      row += 1

   row = 1
   for item in printNumRecord:
      worksheet.write(row, 3, item)
      row += 1
   # Write a total using a formula.
   #worksheet.write(row, 0, 'Total')
   #worksheet.write(row, 1, '=SUM(B1:B4)')

   workbook.close()



if __name__ == "__main__":
   #personList = readAll()
   nameList = readAll()
   write2Xls(nameList)

