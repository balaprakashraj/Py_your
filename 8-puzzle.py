class sol:
    def solve(self, board):
        dict={}
        flatten=[]
        for i in range(len( board)):
            flatten += board[i]
        flatten = tuple(flatten)
        dict[flatten]=0

        if flatten== (0,1,2,3,4,5,6,7,8):
            return 0
        return self.get_pt(dict)
    def get_pt(self,dict):
        cnt=0
        while True:
            current_node= [x for x in dict if dict[x]==cnt ]
            if len(current_node)==0:
                return -1
            for node in current_node:
                next_move= self.find_next(node)
                for move in next_move:
                    if move not in dict:
                        dict[move]= cnt+1
                    if move==(0,1,2,3,4,5,6,7,8):
                        return cnt+1
            cnt+=1
    def find_next(self,node):
        moves={ 0:[1,3],1:[0,2,4],
               2:[1,5],
               3:[0,4,6,],
               4:[1,5,7,3],
               5:[2,4,8],
               6:[3,7],
               7:[6,4,8],
               8:[5,7]}
        result=[]
        pos_0= node.index(0)
        for move in moves[pos_0]:
            new_node= list(node)
            new_node[move],new_node[pos_0]=new_node[pos_0],new_node[move]
            result.append(tuple(new_node))
        return result
ob=sol()
matrix = [
[3, 1, 2],
[4, 7, 5],
[6, 8, 0]
]
print(ob.solve(matrix))
