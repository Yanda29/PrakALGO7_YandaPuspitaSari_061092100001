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

def faktorial(n):
    faktorial = 1
    
    for i in range(1,n + 1):
        faktorial = faktorial*i
    print("Faktorial dari",n,"adalah",faktorial)
num = int(input("nilai: "))
faktorial(num)
