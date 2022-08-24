# -*- coding: utf-8 -*-
###############################################################################
# Python Parsing Code for Mission Planner Data Logs
# By: Brandon Hickey
# Date: 5/18/2022

# Description: This code will be used to convert a mission planner log file
#               to a comma separate values document containing
#               Vertical Position, Velocity, and Acceleration.

# IMPORTANT NOTE: You MUST convert the ".BIN" file logs from 
#                  Navio2 to a ".log" otherwise you will get an error.
###############################################################################


# Import Packages
import csv # Used for parsing CSV files
import tkinter as tk # Used for dialog boxes
from tkinter import filedialog as fd # sub module for dialog boxes

# Initialize dialog box object
root = tk.Tk() 

# Ask for ".log" file here to open
firstFile = fd.askopenfilename()
secondFile=fd.askopenfilename()
# Ask for the name of the final parsed log.
fileSaveName=fd.asksaveasfilename(defaultextension = '.csv')
# Make sure to include .csv
firstData=[]
secondData=[]
mergeData=[]
label=['First','Last','AlF ID','ADP ID']
mergeData.append(label)
# Extract Experimental Data from Log File
with open(firstFile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)      # creating a csv reader object
    for row in csvreader:                
        firstData.append(row)     # extracting each data row one by one
        
        
with open(secondFile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)      # creating a csv reader object
    for row in csvreader:                
        secondData.append(row)     # extracting each data row one by one
skipFirst=0
# Check for duplicates
for row1 in firstData:
    # Skip First Row
    if skipFirst==0:
        skipFirst=1
    # Compare first row of first CSV to all of second CSV
    else:
        skipFirst=0
        matchFound=False
        for row2 in secondData:
            if skipFirst==0:
                skipFirst=1
            else:
                # Check if the two rows compared match
                print('')
                print(row1)
                print(row2)
                if row1[0]==row2[0] and row1[1]==row2[1] and matchFound==False:
                
                    print("Matches with file 2")
                    matchFound=True
                    
                    #Check if a duplicate exists in the merge
                    noDuplicate=1
                    for row3 in mergeData:
                        if row1[0]==row3[0] and row1[1]==row3[1]:
                            print("Already duplicated")
                            noDuplicate=0
                            
                            
                            
                    # If No duplicates found, add to the merged data
                    if noDuplicate==1:
                        data=[row1[0],row1[1],row1[2],row2[2]]
                        mergeData.append(data)
                        print(data)
                        
        if matchFound==False:
            data=[row1[0],row1[1],row1[2],'']
            mergeData.append(data)
            print(data)
            
skipFirst=0
# Now check File 2 against just duplicates in the merged file
for row2 in secondData:
    # Skip First Row
    if skipFirst==0:
        skipFirst=1
    # Compare first row of first CSV to all of second CSV
    else:
        skipFirst=0
        matchFound=False
        for row3 in mergeData:
            if skipFirst==0:
                skipFirst=1
            else:
                # Check if the two rows compared match
                print('')
                print(row2)
                print(row3)
                if row2[0]==row3[0] and row2[1]==row3[1] and matchFound==False:
                
                    print("Matches with merge")
                    matchFound=True
                        
        if matchFound==False:
            data=[row2[0],row2[1],'',row2[2]]
            mergeData.append(data)
            print(data)
                        
    
                    


        
#Write log to file
with open(fileSaveName, 'w') as file:
  for row in mergeData:
      firstCheck=0
      for col in row:
          if firstCheck==0:
              file.write(str(col))
              firstCheck=1
          else:
              file.write(',')
              file.write(str(col))
      file.write('\r')
#############################################################################

root.destroy()
print("Parsing Finished")