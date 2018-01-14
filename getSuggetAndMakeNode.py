# -*- coding: utf-8 -*-
from getSuggest import GoogleAutoComplete
from node import Node
import argparse
from time import sleep
from string import ascii_lowercase
from string import digits
import requests
import urllib.parse
import codecs
from graphviz import Digraph

def recursiveDitect(gs,query,nodeDic):    
    ret = gs.get_suggest(query)

    if len(ret) <= 1:
        return

    #まずはノード作成とかその辺
    splited = query.split()
    if len(splited) == 1:
        nodeDic[splited[0]] = Node(splited[0])
    else:
        newWord = splited[-1]
        if splited[-2] in nodeDic:
            node = nodeDic[splited[-2]]
        else:
            node = nodeDic[splited[-2]] = Node(splited[-2])
        node.appendSuggestWord(newWord)
        if newWord in nodeDic:
            alreadyNode = nodeDic[newWord]
            alreadyNode.addCount()
        else:
            newNode = Node(newWord)
            nodeDic[newWord] = newNode

    for suggetWord in ret:
        splitedSuggest = suggetWord.split()
        if suggetWord == query or splitedSuggest[0] != splited[0]:
            continue
        #h = input()
        recursiveDitect(gs,str(suggetWord),nodeDic)


#sigmaJS用json吐き出し関数
def exportJson(nodeDic):
    f = codecs.open('graph.json','w','utf-8')
    
    #初めにNodeを列挙してから
    f.write("""{"nodes": [ """)

    flag = False
    i = 1
    j = 1
    for node in nodeDic.values():
        if flag:
            f.write(",")
        f.write(node.getNodeJsonString(i,j))
        flag = True
        i += 1
        if i > 10:
            i = 0
            j +=1

    f.write("],")

    f.write(""" "edges": [ """)
    flag = False

    flag = False
    for node in nodeDic.values():
        nodeJsonString = node.getEdgeJsonString()
        if nodeJsonString == "":
            continue

        if flag == True:
            nodeJsonString = "," + nodeJsonString
        f.write(nodeJsonString)
        flag = True

    f.write("]}")
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phrase", help="調べたい単語")
    parser.add_argument("file", help="保存するファイル名")
    args = parser.parse_args()


    nodeDic = {}

    # Google Suggest キーワード取得
    gs = GoogleAutoComplete()

    ret = gs.get_suggest(args.phrase)

    recursiveDitect(gs,args.phrase,nodeDic)
    # exportJson(nodeDic)

    g = Digraph(format='png')
    g.attr("node", style="filled")

    for node in nodeDic.values():
        g.node(node.name, **{'width':str(node.count), 'height':str(node.count),'fontname':"MS UI Gothic"})

    for node in nodeDic.values():
        for word in node.suggestWord:
            g.edge(node.name,word)
            
    g.render(args.file)
