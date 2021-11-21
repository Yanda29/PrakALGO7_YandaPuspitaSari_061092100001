# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:37:18 2021

@author: Yanda Puspita Sari
"""
print("@   @  @@@@@  @    @  @@@@    @@@@@")
print(" @ @   @   @  @ @  @  @   @   @   @")
print("  @    @@@@@  @  @ @  @    @  @@@@@")
print("  @    @   @  @   @@  @   @   @   @")
print("  @    @   @  @    @  @@@@    @   @")

string = list(map(str, input("masukan sesuatu: ").lower()))

def vokal_kon(n):
  consonan=0
  vokal=0
  for i in range(0, len(string)):
    if string[i]=='a' or string[i]=='i' or string[i]=='u' or string[i]=='e' or string[i]=='o':
      vokal+=1
    else:
      consonan+=1
  print("Jumlah huruf Vokal: ",vokal)
  print("Jumlah huruf konsonan:",consonan)
vokal_kon(string)
