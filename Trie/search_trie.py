class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfString=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insertString(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endOfString=True
        print('the word is successfully inserted')

    def searchString(self,word):
        current=self.root
        for i in word:
            node=current.children.get(i)
            if node==None:
                return False
            current=node
        if current.endOfString==True:
            return True
        else:
            return False
                


new_trie=Trie()
new_trie.insertString('app')
new_trie.insertString('appl')
print(new_trie.searchString('apple'))


