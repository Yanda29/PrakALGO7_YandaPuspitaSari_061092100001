# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:37:17 2021

@author: Yanda Puspita Sari
"""
print("@   @  @@@@@  @    @  @@@@    @@@@@")
print(" @ @   @   @  @ @  @  @   @   @   @")
print("  @    @@@@@  @  @ @  @    @  @@@@@")
print("  @    @   @  @   @@  @   @   @   @")
print("  @    @   @  @    @  @@@@    @   @")

def main(n):
    if n %3==0:
        n**3 
        print ("hasilnya adalah",n**3)
    else:
        cek(num)
def cek(n):
    if n %3!=0:
        print ("false")
        exit(0)
num=int(input("masukan nilai: "))
main(num)
