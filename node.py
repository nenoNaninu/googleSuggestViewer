#ノードのクラス。
# 自身がなんのノードであるか、またどこに向かってエッジが伸びているか。
# 出現頻度も保存する。
# -*- coding: utf-8 -*-
class Node:
    def __init__(self,nodeName):
        self.name = nodeName
        self.count = 1
        self.suggestWord = []
    
    def appendSuggestWord (self,name):
        if len(self.suggestWord)==0:
            self.suggestWord.append(name)
        elif (name in self.suggestWord) == False:
            self.suggestWord.append(name)

    def addCount(self):
        self.count += 1
    
    def getNodeJsonString(self,px,py):
        textForJson =  """ 
        "id": "{name}",
        "label":"{label}",
        "x":"{x}",
        "y":"{y}",
        "size":"{size}"
        """.format(name=self.name, label=self.name,x=px*5,y = py*5,size=self.count)

        textForJson = "{\n" + textForJson +"}\n"
        return textForJson

    def getEdgeJsonString(self):
    #     {
    #       "id": "e0",
    #       "source": "n0",
    #       "target": "n1"
    #    }
        textsForJson = ""
        flag = False
        if len(self.suggestWord) == 0:
            return textsForJson
        for s in self.suggestWord:
            idstr = self.name+"2"+s

            textForJson = """
            "id":"{id}",
            "source":"{sorce}",
            "target":"{target}"
            """.format(id=idstr,sorce=self.name,target=s)
            textForJson = "{"+textForJson +"}"
            if flag:
                textForJson = ","+textForJson
            flag = True
            textsForJson += textForJson

        return textsForJson