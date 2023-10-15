class TreeNode:
    def __init__(self,data, children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret=' '*level+ str(self.data)+'\n'
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    
    def addChild(self,treeNode):
        self.children.append(treeNode)

tree=TreeNode('Drinks',[])
hot=TreeNode('hot',[])
cold=TreeNode('cold',[])
tree.addChild(hot)
tree.addChild(cold)
print(tree)
tea=TreeNode('tea',[])
coffee=TreeNode('coffee',[])
cola=TreeNode('cola',[])
fanta=TreeNode('fanta',[])
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fanta)
print(tree)
