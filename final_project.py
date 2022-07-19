#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Final Project: A star search in map """
__author__ = "Ivan Ivanov"

import sys
import re


def read_file(fn):
    f = open(fn)
    text = f.read()
    return text

def extract_heuristic(line):
    h = line.split(" ")
    for i in h:
        h1 = i.split("=")
        s1= h1[0]
        s2 = int(h1[1])
        heuristic.update({s1:s2})

def extract_distance(line_1, line_2):
    s1 = line_1.replace("=","")
    s1 = re.sub("[0-9]", "",s1)
    list_vert = s1.split(" ")
    for i in list_vert:
        distance.update({str(i):{}})
    
    list_dist = line_2.split(" ")
    for i in list_dist:
        strr = str(i)
        strr = strr.replace("-", " ")
        strr = strr.replace("=", " ")
        list_val = strr.split(" ")
        distance[list_val[0]].update({list_val[1]:int(list_val[2])})
            
def print_help():
    print()
    print("This program uses A* search to output the best route from point A to point B in a map.")
    print()
    print("The program is designed to be executed through the command line. It takes a text file(.txt) from the command line.")
    print("Currently the program has three text files inside the fina_project folder: graph.txt , graph_chile.txt and graph_romania.txt . All those files represent maps.")
    print("A proper way to execute the program is by typing in command line the following:")
    print()
    print("EXAMPLE 1: python final_project.py graph.txt")
    print()
    print("EXAMPLE 2: python final_project.py graph_chile.txt")
    print()
    print("EXAMPLE 3: python final_project.py graph_romania.txt")
    print()
    print("You can import your own text file but in order for it to work it should follow the same format as graph.txt , graph_chile.txt and graph_romania.txt.")
    print("Thank you!")
    print()
    
def print_frontier(frontier):
    i=0
    print("Nodes in the frontier:",end="")
    while i <len(frontier):
        (fn,cost,node,route)=frontier[i]
        print(" ",route,fn,end="")
        i=i+1
    print("\n")


def a_star(origin,dest):
    frontier = []
    frontier.append((heuristic[origin],0,origin,[origin]))
    while len(frontier) != 0:
        frontier.sort()
        print_frontier(frontier)
        (fn, cost, node, route) = frontier.pop(0)
        
        
        if node == dest:
            print("Route: ",end="")
            for i in range(0,len(route)):
                if i < len(route)-1:
                    print(route[i],end="--->")
                else:
                    print(route[i])
            
            print("Distance: "+str(fn))
            print()
            return
    
        for next_node in distance[node].keys():
            gn = cost + distance[node][next_node]
            hn = heuristic[next_node]
            fn = gn + hn
            frontier.append((fn,gn,next_node,route + [next_node]))
            

if (__name__ == "__main__"):
    cmd_inp = sys.argv[1]
    text = ""
    if(cmd_inp == "help" or cmd_inp =="Help"):
        print_help()
    else:
        text = read_file(cmd_inp)
        heuristic = {}
        distance = {}
        lines = text.split("\n")
        line_1 =lines[0]
        line_2 =lines[1]
        line_3 =lines[2]
        line_4 =lines[3]
        extract_heuristic(line_1)
        extract_distance(line_1,line_2)
        origin = re.sub("[A-Za-z0-1]*:", "", line_3)
        dest = re.sub("[A-Za-z0-1]*:", "", line_4)
        a_star(origin,dest)