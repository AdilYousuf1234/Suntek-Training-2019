#ans=[]
def Solution(op,cp,s):      
    if(op==0 and cp==0):    #if open paranthesis and closed paranthesis are reduced then print s
        print(s)
        #ans.append(s) 
    if(op>cp):              #if no of open paranthesisis is not same as no of closed paranthesis
        return
    if(op>0):
        Solution(op-1,cp,s+"(") #reduce the no of open paranthesis and solve
    if(cp>0):
        Solution(op,cp-1,s+")") #reduce the no of closed paranthesis and solve
#inputs=[6,3,-1,10,16]
#expectedoutputs=[["((()))","(()())","(())()","()(())","()()()"],[]]
n=int(input())
Solution(n//2,n//2,"")
#print(ans==expectedoutputs)
