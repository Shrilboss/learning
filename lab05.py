class Lab05:

    def solve01(self, list1, list2):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        X=set(list1)
        Y=set(list2)
        Z=Y-X
       
        return(list(Z))

    def solve02(self, S):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        k=len(S)
        l=[]
        for i in range(len(S)-1):
            a= S[:i] + S[i+1:]
            l.append(a)
        l.append(S[:(k-1)])
        X=set(l)
        return(len(X))
    def solve03(self, N, a):
        #Write your solution here.
        #Remember to replae "pass" with your own return statement!
        cnt=0
        for i in range(N-1):
            for j in range(i+1,N):
                if(a[i]==a[j]):
                    cnt+=1
        return(cnt)
    def solve04(self, arr, A, B):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        X=set(arr)
        Y=set(A)
        Z=set(B)
        
        return(len(X&Y)-len(X&Z))

    def solve05(self, n, guesses):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        k=len(guesses)
        A=set()
        D=set()
        for i in range(k):
            if(guesses[i][1]=="NO"):
                s1=(guesses[i][0].split())
                B=(A | set(s1))
            else:
                s2=(guesses[i][0].split())
                C=(D | set(s2))
        E= C - (C & B)
        t=list(E)
        t.sort()
        s3=""
        s3=s3+str(t[0])
        for i in range(1,len((t))):
            s3=s3+" " +str(t[i])
        return(s3)  
    def solve06(self, S, Q, engines, queries):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        l=[]
        cnt=0

        for i in range(len(queries)):
            if(queries[i] in engines):
                cnt+=1
                engines.remove(queries[i])
                
                l.append(queries[i])
                if(cnt==(S-1)):
                    break
        ans=0
        for i in range(len(queries)):
            if(engines[0]==queries[i]):
                ans+=1
        return(ans)
    def solve07(self, n):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        l=[]
        a=2
        while(a<=(n)):
            l.append(a)
            a+=1
        l.append(1)
        return(l)
        
    def solve08(self, wires):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve09(self, elevations):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve10(self, ratings):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

#--------IMPORTANT:
#--------Before uploading this file on gradescope, delete or comment out all the lines below.

#These print statements will show the output for the given test cases.
#Feel free to experiment with your own.


# soln = Lab05()

# print(soln.solve01(['BCE017', 'BIT049', 'BCE017'],
#                    ['BCE017', 'BIT059', 'BIT049', 'BIT059']))
# # Expected Output: ['BIT059']

# print(soln.solve02("ABA"))
# # Expected Output: 3

# print(soln.solve02("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"))
# # Expected Output: 1

# print(soln.solve03(4, [1, 2, 3, 2]))
# # Expected Output: 1

# print(soln.solve03(3, [1, 2, 3]))
# # Expected Output: 0

# print(soln.solve04([5, 1, 3, 3, 2], [4, 3], [5, 7]))
# # Expected Output: 1

# print(soln.solve05(10, [("1 2 3 4 5", "YES"), ("2 4 6 8 10", "NO")]))
# # Expected Output: "1 3 5"

# print(soln.solve06(5, 10, ["Yeehaw", "NSM", "Dont Ask", "B9", "Googol"],
#                    ["Yeehaw", "Yeehaw", "Googol", "B9", "Googol", "NSM", "B9", "NSM", "Dont Ask", "Googol"]))
# # Expected Output: 1

# print(soln.solve07(10))
# # Expected Output: [2, 3, 1]

# print(soln.solve08([(1, 10), (5, 5), (7, 7)]))
# # Expected Output: 2

# print(soln.solve09([[9, 6, 3], [5, 9, 6], [3, 5, 9]]))
# # Expected Output: [['a', 'b', 'b'], ['a', 'a', 'b'], ['a', 'a', 'a']]

# print(soln.solve09([[0, 1, 2, 3, 4, 5, 6, 7, 8, 7]]))
# # Expected Output: [['a','a','a','a','a','a','a','a','a','b']]

# print(soln.solve10([1, 2, 2]))
# # Expected Output: 4

# print(soln.solve10([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
# # Expected Output: 19
