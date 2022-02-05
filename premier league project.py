import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df=pd.read_csv("C:/Users/prane/Desktop/ip programs/premier_league.csv")
df1=pd.read_csv("C:/Users/prane/Desktop/csv arsenal and chelsea .csv")
df2=pd.read_csv("C:/Users/prane/Desktop/manutd and city csv.csv")
df3=pd.read_csv("C:/Users/prane/Desktop/liverpool & spurs .csv")
df4=pd.read_csv("C:/Users/prane/Desktop/new castle & west ham .csv")
df5=pd.read_csv("C:/Users/prane/Desktop/everton and leichester .csv")


print("**********************WELCOME TO PREMIER LEAGUE SEASON 2021-22 DATABASE**********************")



while(True):
  print("CHOOSE OPTIONS")
  print("1.TO VIEW THE CLUBS IN THE DATABSE")
  print("2.CLUB'S STATS DO YOU WANT TO LOOK AT")
  print("3.TO VIEW TOP 3 GOAL SCORERS AMONG ALL THE CLUBS")
  print("4.TO VIEW TOP 3 GOAL KEEPERS AMONG ALL THE CLUBS")
  print("5.TO VIEW MOST PAID PLAYER AMONG ALL THE CLUBS")
  print("6.TO VIEW ALL THE DATA ON ALL THE CLUBS")
  print("7.TO ADD DATA TO THE DATAFRAME")
  print("8.TO DELETE DATA FROM THE DATAFRAME")
  print("9.TO VIEW STATISTICAL DATA ON THE CLUBS")
  

  a=int(input("choose one the available options"))
#first question 
  if a==1:
    print('1.ARSENAL\n2.CHELSEA\n3.MANCHESTER UNITED\n4.MANCHESTER CITY\n5.LIVERPOOL FC\n6.TOTTENHAM HOTSPUR\n7.NEW CASTLE UTD\n8.WEST HAM UTD\n9.EVERTON\n10.LEICHESTER CITY')
#second question 
  if a==2:
      club=input("ENTER YOUR PREFFERED CLUB(IN ALL CAPS)")
      if club=="ARSENAL":
        while(True):
        
          print("1.TO DISPLAY THE PLAYERS NAME IN ARSENAL")
          print("2.TO DISPLAY POSTION OF PLAYERS IN ARSENAL")
          print("3.TO DISPLAY SALARY OF PLAYERS IN ARSENAL")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN ARSENAL")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN ARSENAL")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.head(12))
              
            
          if ch==2:
              print(df1[['PLAYERS','POSITION']].head(12))
              
          if ch==3:
              print(df1[['PLAYERS','SALARY']].head(12))

          if ch==4:
              asc=df1.iloc[0:13,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)

          if ch==5:
              asc=df1.iloc[0:13,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)

          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].head(12))

          if ch==7:
              print("The number of championships won by Arsenal is 3\n in the years 1997, 2001, 2003")

          if ch==8:
              print("The manager of Arsenal is Mikel Arteta")

          
          if ch==9:
              break

      if club=="CHELSEA":
        while(True):
          
          print("1.TO DISPLAY THE PLAYERS NAME IN CHELSEA")
          print("2.TO DISPLAY POSTION OF PLAYERS IN CHELSEA")
          print("3.TO DISPLAY SALARY OF PLAYERS IN CHELSEA")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN CHELSEA")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN CHELSEA")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.tail(12))
                
              
          if ch==2:
              print(df1[['PLAYERS','POSITION']].tail(12))
                
          if ch==3:
              print(df1[['PLAYERS','SALARY']].tail(12))

          if ch==4:
              asc=df1.iloc[13:25,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)

          if ch==5:
              asc=df1.iloc[13:25,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)

          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].tail(12))

          if ch==7:
              print("The number of championships won by Chelsea is 5\n in the years 2004, 2005, 2009, 2014, 2016")

          if ch==8:
              print("The manager of Chelsea is Thomas Tuchel")

            
          if ch==9:
              break

      if club=="MANCHESTER UNITED":
        while(True):
          
        
          print("1.TO DISPLAY THE PLAYERS NAME IN MANCHESTER UNITED")
          print("2.TO DISPLAY POSTION OF PLAYERS IN MANCHESTER UNITED")
          print("3.TO DISPLAY SALARY OF PLAYERS IN MANCHESTER UNITED")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN MANCHESTER UNITED")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN MANCHESTER UNITED")
          print("7.TO DISPLAY THE PLAYER WITH MOST NUMBER OF FOULS")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.head(12))
         
          if ch==2:
              print(df1[['PLAYERS','POSITION']].head(12))
                  
          if ch==3:
              print(df1[['PLAYERS','SALARY']].head(12))
    
          if ch==4:
              asc=df1.iloc[0:13,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)
    
          if ch==5:
              asc=df1.iloc[0:13,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)
    
          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].head(12))
    
          if ch==7:
              print("The number of championships won by MANCHESTER UNITED is 13\n in the years 1994, 1996, 1997, 1999, 2000, 2001, 2003, 2007, 2008, 2009, 2011 and 2013")
    
          if ch==8:
              print("The manager of MANCHESTER UNITED is Ralf Rangnick")
         
          if ch==9:
              break
        
      if club=="MANCHESTER CITY":
        while(True):
              
          print("1.TO DISPLAY THE PLAYERS NAME IN MANCHESTER CITY")
          print("2.TO DISPLAY POSTION OF PLAYERS IN MMANCHESTER CITY")
          print("3.TO DISPLAY SALARY OF PLAYERS IN MANCHESTER CITY")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN MANCHESTER CITY")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN MANCHESTER CITY")
          print("7.TO DISPLAY THE PLAYER WITH MOST NUMBER OF FOULS")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.tail(12))
         
          if ch==2:
              print(df1[['PLAYERS','POSITION']].tail(12))
                  
          if ch==3:
              print(df1[['PLAYERS','SALARY']].tail(12))
    
          if ch==4:
              asc=df1.iloc[0:13,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)
    
          if ch==5:
              asc=df1.iloc[0:13,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)
    
          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].tail(12))
    
          if ch==7:
              print("The number of championships won by MANCHESTER CITY is 5\n in the years 2011, 2013, 2017, 2018, 2020")
    
          if ch==8:
              print("The manager of MANCHESTER CITY is Pep Guardiola")
    
              
          if ch==9:
              break
   
      if club=="LIVERPOOL FC":
        while(True):
          print("1.TO DISPLAY THE PLAYERS NAME IN LIVERPOOL FC")
          print("2.TO DISPLAY POSTION OF PLAYERS IN LIVERPOOL FC")
          print("3.TO DISPLAY SALARY OF PLAYERS IN LIVERPOOL FC")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN LIVERPOOL FC")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN LIVERPOOL FC")
          print("7.TO DISPLAY THE PLAYER WITH MOST NUMBER OF FOULS")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.head(12))
         
          if ch==2:
              print(df1[['PLAYERS','POSITION']].head(12))
                  
          if ch==3:
              print(df1[['PLAYERS','SALARY']].head(12))
    
          if ch==4:
              asc=df1.iloc[0:13,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)
    
          if ch==5:
              asc=df1.iloc[0:13,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)
    
          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].head(12))
    
          if ch==7:
              print("The number of championships won by LIVERPOOL FC is 1\n in the years 2019")
    
          if ch==8:
              print("The manager of LIVERPOOL FC is Jurgen Klopp")
    
              
          if ch==9:
              break
        
      if club=="TOTTENHAM HOTSPUR":
        while(True):
          print("1.TO DISPLAY THE PLAYERS NAME IN TOTTENHAM HOTSPUR")
          print("2.TO DISPLAY POSTION OF PLAYERS IN TOTTENHAM HOTSPUR")
          print("3.TO DISPLAY SALARY OF PLAYERS IN TOTTENHAM HOTSPUR")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN TOTTENHAM HOTSPUR")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN TOTTENHAM HOTSPUR")
          print("7.TO DISPLAY THE PLAYER WITH MOST NUMBER OF FOULS")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.tail(12))
         
          if ch==2:
              print(df1[['PLAYERS','POSITION']].tail(12))
                  
          if ch==3:
              print(df1[['PLAYERS','SALARY']].tail(12))
    
          if ch==4:
              asc=df1.iloc[0:13,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)
    
          if ch==5:
              asc=df1.iloc[0:13,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)
    
          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].tail(12))
    
          if ch==7:
              print("The number of championships won by TOTTENHAM HOTSPUR is 0")
    
          if ch==8:
              print("The manager of TOTTENHAM HOTSPUR is Antonio Conte")
    
              
          if ch==9:
              break

      if club=="NEW CASTLE UTD":
        while(True):
          print("1.TO DISPLAY THE PLAYERS NAME IN NEW CASTLE UTD")
          print("2.TO DISPLAY POSTION OF PLAYERS IN NEW CASTLE UTD")
          print("3.TO DISPLAY SALARY OF PLAYERS IN NEW CASTLE UTD")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN NEW CASTLE UTD")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN NEW CASTLE UTD")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")
          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.head(12))
              
            
          if ch==2:
              print(df1[['PLAYERS','POSITION']].head(12))
              
          if ch==3:
              print(df1[['PLAYERS','SALARY']].head(12))

          if ch==4:
              asc=df1.iloc[0:13,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)

          if ch==5:
              asc=df1.iloc[0:13,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)

          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].head(12))

          if ch==7:
              print("The number of championships won by New Castle UTD is 0")

          if ch==8:
              print("The manager of New Castle UTD is Eddie Howe")

          
          if ch==9:
              break

      if club=="WEST HAM UNITED":
        while(True):
          
          print("1.TO DISPLAY THE PLAYERS NAME IN WEST HAM UNITED")
          print("2.TO DISPLAY POSTION OF PLAYERS IN WEST HAM UNITED")
          print("3.TO DISPLAY SALARY OF PLAYERS IN WEST HAM UNITED")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN WEST HAM UNITED")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN WEST HAM UNITED")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.tail(12))
                
              
          if ch==2:
              print(df1[['PLAYERS','POSITION']].tail(12))
                
          if ch==3:
              print(df1[['PLAYERS','SALARY']].tail(12))

          if ch==4:
              asc=df1.iloc[13:25,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)
          if ch==5:
           
              asc=df1.iloc[13:25,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)

          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].tail(12))

          if ch==7:
              print("The number of championships won by West Ham United is 0")

          if ch==8:
              print("The manager of West Ham United is David Moyes")

            
          if ch==9:
              break
      if club=="EVERTON":
        while(True):
          print("1.TO DISPLAY THE PLAYERS NAME IN EVERTON")
          print("2.TO DISPLAY POSTION OF PLAYERS IN EVERTON")
          print("3.TO DISPLAY SALARY OF PLAYERS IN EVERTON")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN EVERTON")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN EVERTON")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.head(12))
              
            
          if ch==2:
              print(df1[['PLAYERS','POSITION']].head(12))
              
          if ch==3:
              print(df1[['PLAYERS','SALARY']].head(12))

          if ch==4:
              asc=df1.iloc[0:13,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)

          if ch==5:
              asc=df1.iloc[0:13,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)

          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].head(12))

          if ch==7:
              print("The number of championships won by Everton is 0")

          if ch==8:
              print("The manager of Everton is Duncan Ferguson")

          
          if ch==9:
              break

      if club=="LEICHESTER CITY":
         
        while(True):
          
          print("1.TO DISPLAY THE PLAYERS NAME IN LEICHESTER CITY")
          print("2.TO DISPLAY POSTION OF PLAYERS IN LEICHESTER CITY")
          print("3.TO DISPLAY SALARY OF PLAYERS IN LEICHESTER CITY")
          print("4.TO DISPLAY TOP THREE GOAL SCORER IN LEICHESTER CITY")
          print("5.TO DISPLAY THE PLAYER WHO SAVED THE MOST NUMBER OF GOALS")
          print("6.TO DISPLAY THE NATIONALITY OF PLAYERS IN LEICHESTER CITY")
          print("7.TO DISPLAY THE NUMBER OF CHAMPIONSHIPS WON BY THE CLUB")
          print("8.TO DISPLAY THE MANAGER OF THE TEAM")
          print("9.EXIT BACK TO MAIN MENU")

          ch=int(input("SELECT YOUR PREFFERED CHOICE"))
          if ch==1:
              print(df1.PLAYERS.tail(12))
                
              
          if ch==2:
              print(df1[['PLAYERS','POSITION']].tail(12))
                
          if ch==3:
              print(df1[['PLAYERS','SALARY']].tail(12))

          if ch==4:
              asc=df1.iloc[13:25,3:5]
              X=asc.sort_values(by='GOALS_SCORED').tail(3)
              print(X)

          if ch==5:
              asc=df1.iloc[13:25,2:4]
              X=asc.sort_values(by='GOALS_SAVED').tail(1)
              print(X)

          if ch==6:
              print(df1[['PLAYERS','NATIONALITY']].tail(12))

          if ch==7:
              print("The number of championships won by Leichester City is 1\n in the year 2015")

          if ch==8:
              print("The manager of Leichester City is  Brendan Rodgers")

            
          if ch==9:
              break


  if a==3:
    top=df.iloc[0:120,3:5]
    X=top.sort_values(by='GOALS_SCORED').tail(3)
    print(X)
    
  if a==4:
    top=df.iloc[0:120,2:4]
    X=top.sort_values(by='GOALS_SAVED').tail(3)
    print(X)
    
  if a==5:
    top=df.iloc[0:120,7:9]
    X=top.sort_values(by='SALARY').tail(1)
    print(X)

  if a==6:
    print(df)

  if a==7:
    print('The columns available to add data are\nGOALS_SAVED\nPLAYERS\nGOALS_SCORED\nPOSITION\nNATIONALITY\nSALARY')
    print("Then,please fill the required details")
    club=input("club name")
    if club=="ARSENAL":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df1.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df1)

    if club=="CHELSEA":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df1.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df1)

    if club=="MANCHESTER UNITED":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df2.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df2)

    if club=="MANCHESTER CITY":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df2.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df2)

    if club=="LIVERPOOL FC":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df3.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df3)

    if club=="TOTTENHAM HOTSPUR":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df3.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df3)

    if club=="NEW CASTLE UTD":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df4.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df4)

    if club=="WEST HAM UNITED":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df4.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df4)

    if club=="EVERTON":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df5.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df5)

    if club=="LEICHESTER CITY":
      sl=int(input("Enter the serial number"))
      gs=float(input("ENTER THE GOALS SAVED"))
      name=input("ENTER THE NAME OF THE PLAYER")
      scored=float(input("ENTER THE GOALS SCORED BY THE PLAYER"))
      POS=input("ENTER THE POSITION OF THE PLAYER")
      NATIONALITY=input("ENTER THE NATIONALITY OF THE PLAYER")
      MONEY=float(input("ENTER THE SALARY OF THE PLAYER"))
      df5.loc[club]=[sl,club,gs,name,scored,POS,NATIONALITY,MONEY]
      print(df5)


  if a==8:
    club=input("club name")

    if club=="ARSENAL":
      print(df1.PLAYERS)
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df1=df1.drop(nm,axis=0)
      print(df1)

    if club=="CHELSEA":
      print(df1['PLAYERS'].tail(12))
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df1=df1.drop(nm,axis=0)
      print(df1)

    if club=="MANCHESTER UNITED":
      print(df2.PLAYERS)
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df2=df2.drop(nm,axis=0)
      print(df2)

    if club=="MANCHESTER CITY":
      print(df2['PLAYERS'].tail(12))
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df2=df2.drop(nm,axis=0)
      print(df2)

    if club=="LIVERPOOL FC":
      print(df3.PLAYERS)
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df3=df3.drop(nm,axis=0)
      print(df3)

    if club=="TOTTENHAM HOTSPUR":
      print(df3['PLAYERS'].tail(12))
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df3=df3.drop(nm,axis=0)
      print(df3)

    if club=="NEW CASTLE UTD":
      print(df4.PLAYERS)
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df4=df4.drop(nm,axis=0)
      print(df4)

    if club=="WEST HAM UNITED":
      print(df4['PLAYERS'].tail(12))
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df4=df4.drop(nm,axis=0)
      print(df4)

    if club=="EVERTON":
      print(df5.PLAYERS)
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df5=df5.drop(nm,axis=0)
      print(df5)

    if club=="LEICHESTER CITY":
      print(df5['PLAYERS'].tail(12))
      nm=int(input("Which players data do you want to delete(ENTER THE SERIAL NUMBER)?"))
      df5=df5.drop(nm,axis=0)
      print(df5)
  

  if a==9:         
       
    cl=input("ENTER THE CLUB NAME(ALL CAPS):")
   
    if cl=="ARSENAL":
      
       
      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      
      print("CHOICES ARE 1,2")
      ch=int(input("Enter the preferred option:"))                                                  #put in the club u want to see 
      if ch==1:
        X=df1["PLAYERS"].head(12)
        Y=df1["SALARY"].head(12)
        plt.plot(X,Y,marker="^",markersize=12,color="red",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df1["NATIONALITY"].head(12)
        Y=df1["PLAYERS"].head(12)
        plt.plot(Y,X,marker="v",markersize=23,color="red",linestyle="dashdot")
        plt.show()
        

    if cl=="CHELSEA":

      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      
      print("CHOICES ARE 1,2")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df1["PLAYERS"].tail(12)
        Y=df1["SALARY"].tail(12)
        plt.plot(X,Y,marker="^",markersize=12,color="blue",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df1["NATIONALITY"].tail(12)
        Y=df1["PLAYERS"].tail(12)
        plt.plot(Y,X,marker="v",markersize=23,color="blue",linestyle="dashdot")
        plt.show()


    if cl=="MANCHESTER UNITED":

      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      
      print("CHOICES ARE 1,2")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df2["PLAYERS"].head(12)
        Y=df2["SALARY"].head(12)
        plt.plot(X,Y,marker="^",markersize=12,color="red",linestyle="dashdot")
        plt.title("1unit = 10million")
        plt.show()
        print("1unit = 10million")
      if ch==2:
        X=df2["NATIONALITY"].head(12)
        Y=df2["PLAYERS"].head(12)
        plt.plot(Y,X,marker="v",markersize=23,color="red",linestyle="dashdot")
        plt.show()

    if cl=="MANCHESTER CITY":

      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      
      print("CHOICES ARE 1,2")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df2["PLAYERS"].tail(12)
        Y=df2["SALARY"].tail(12)
        plt.plot(X,Y,marker="^",markersize=12,color="blue",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df2["NATIONALITY"].tail(12)
        Y=df2["PLAYERS"].tail(12)
        plt.plot(Y,X,marker="v",markersize=23,color="blue",linestyle="dashdot")
        plt.show()


    if cl=="LIVERPOOL FC":
      
       
      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      print("3.TO VIEW STATISTICAL DATA ON THE NUMBER OF TROPHIES WON")
      print("CHOICES ARE 1,2")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df3["PLAYERS"].head(12)
        Y=df3["SALARY"].head(12)
        plt.plot(X,Y,marker="^",markersize=12,color="red",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df3["NATIONALITY"].head(12)
        Y=df3["PLAYERS"].head(12)
        plt.plot(Y,X,marker="v",markersize=23,color="red",linestyle="dashdot")
        plt.show()
   

   
    if cl=="TOTTENHAM HOTSPUR":
      
       
      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
     
      print("CHOICES ARE 1,2,3,4,5")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df3["PLAYERS"].tail(12)
        Y=df3["SALARY"].tail(12)
        plt.plot(X,Y,marker="^",markersize=12,color="blue",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df3["NATIONALITY"].tail(12)
        Y=df3["PLAYERS"].tail(12)
        plt.plot(Y,X,marker="v",markersize=23,color="blue",linestyle="dashdot")
        plt.show()
        

   
    if cl=="NEW CASTLE UTD":
      
       
      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      print("3.TO VIEW STATISTICAL DATA ON THE NUMBER OF TROPHIES WON")
      print("CHOICES ARE 1,2,3,4,5")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df4["PLAYERS"].head(12)
        Y=df4["SALARY"].head(12)
        plt.plot(X,Y,marker="^",markersize=12,color="red",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df4["NATIONALITY"].head(12)
        Y=df4["PLAYERS"].head(12)
        plt.plot(Y,X,marker="v",markersize=23,color="red",linestyle="dashdot")
        plt.show()
        
    if cl=="WEST HAM UNITED":
      
       
      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
     
      print("CHOICES ARE 1,2,3,4,5")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df4["PLAYERS"].tail(12)
        Y=df4["SALARY"].tail(12)
        plt.plot(X,Y,marker="^",markersize=12,color="blue",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df4["NATIONALITY"].tail(12)
        Y=df4["PLAYERS"].tail(12)
        plt.plot(Y,X,marker="v",markersize=23,color="blue",linestyle="dashdot")
        plt.show()
        
    if cl=="EVERTON":
      
       
      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      print("3.TO VIEW STATISTICAL DATA ON THE NUMBER OF TROPHIES WON")
      print("CHOICES ARE 1,2,3,4,5")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df5["PLAYERS"].head(12)
        Y=df5["SALARY"].head(12)
        plt.plot(X,Y,marker="^",markersize=12,color="red",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df5["NATIONALITY"].head(12)
        Y=df5["PLAYERS"].head(12)
        plt.plot(Y,X,marker="v",markersize=23,color="red",linestyle="dashdot")
        plt.show()
        
    if cl=="LEICHESTER CITY":
      
       
      print("1.TO VIEW STATISTICAL DATA ON THE SALARIES OF THE PLAYERS")
      print("2.TO VIEW STATISTICAL DATA ON THE NATIONALTIES OF THE PLAYERS")
      print("3.TO VIEW STATISTICAL DATA ON THE NUMBER OF TROPHIES WON")
      print("CHOICES ARE 1,2,3,4,5")
      ch=int(input("Enter the preferred option:"))
      if ch==1:
        X=df5["PLAYERS"].tail(12)
        Y=df5["SALARY"].tail(12)
        plt.plot(X,Y,marker="^",markersize=12,color="blue",linestyle="dashdot")
        plt.title("1unit = 1million")
        plt.show()
        print("1unit = 1million")
      if ch==2:
        X=df5["NATIONALITY"].tail(12)
        Y=df5["PLAYERS"].tail(12)
        plt.plot(Y,X,marker="v",markersize=23,color="blue",linestyle="dashdot")
        plt.show()

    break


      



        

      

    

  


      
        
      

      
    
      
      
    
    
    
    

    
          



           

              
              

              
          



          

          
          
        
    



  



