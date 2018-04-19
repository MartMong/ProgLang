
# coding: utf-8

# In[1]:


from pptree import *


# In[2]:


grammar={1:{'S':['Stm','S']},
2:{'S':['lambda']},
3:{'AR':['AE']},
4:{'Stm':['id','=','AE',';']},
5:{'Stm':['Stm1']},
6:{'Stm1':['ForStm']},
7:{'Stm1':['IfStm']},
8:{'Stm1':['Block']},
9:{'Stm2':['Var','=','AE']},
10:{'Stm2':['Stm1']},
11:{'const':['Int']},
12:{'id':['Var','Array']},
13:{'Array':['lambda']},
14:{'Array':['[','AE',']','Array']},
15:{'AE':['T',"AE'"]},
16:{"AE'":['+','T',"AE'"]},
17:{"AE'":['lambda']},
18:{'T':['F',"T'"]},
19:{"T'":['*','F',"T'"]},
20:{"T'":['lambda']},
21:{'F':['(','AE',')']},
22:{'F':['id']},
23:{'F':['const']},
25:{'Block':['{','Block2','}']},
26:{'Block2':['Block3','Block2']},
27:{'Block2':['lambda']},
28:{'Block3':['Stm']},
29:{'IfStm':['if','(','RE',')','Block','else','Block']},
30:{'ForStm':['for','(','Stm2',';','RE',';','Stm2',')','Block']},
31:{'RE':['RE2',"RE'"]},
32:{"RE'":['REop','RE2']},
33:{"RE'":['lambda']},
34:{'RE2':['AR']},
35:{'REop':['<']},
36:{'REop':['>']}}


# In[3]:


parsingTable={
    'S':{
        'Var':1,
        '{':1,
        'if':1,
        'for':1,
        '$':2
        },
    'AR':{
        'Var':3,
        'Int':3,
        '(':3,
        },
    'Stm':{
        'Var':4,
        '{':5,
        'if':5,
        'for':5
        },
    'Stm1':{
        '{':8,
        'if':7,
        'for':6,
        },
    'Stm2':{
        'Var':9,
        '{':10,
        'if':10,
        'for':10
        },
    'const':{
        'Int':11
    },
    'id':{
        'Var':12
    },
    'Array':{
        '=':13,
        ';':13,
        '[':14,
        ']':13,
        '+':13,
        '*':13,
        ')':13,
        '<':13,
        '>':13
    },
    'AE':{
        'Var':15,
        'Int':15,
        '(':15
    },
    "AE'":{
        ';':17,
        ']':17,
        '+':16,
        ')':17,
        '<':17,
        '>':17
    },
    'T':{
        'Var':18,
        'Int':18,
        '(':18,
        
    },
    "T'":{
        ';':20,
        ']':20,
        '+':20,
        '*':19,
        ')':20,
        '<':20,
        '>':20
    },
    'F':{
        'Var':22,
        'Int':23,
        '(':21
    },
    'Block':{
        '{':25
    },
    'Block2':{
        'Var':26,
        '{':26,
        '}':27,
        'if':26,
        'for':26
    },
    'Block3':{
        'Var':28,
        '{':28,
        'if':28,
        'for':28
    },
    'IfStm':{
        'if':29
    },
    'ForStm':{
        'for':30,
    },
    'RE':{
        'Var':31,
        'Int':31,
        '(':31,
    },
    "RE'":{
        ';':33,
        ')':33,
        '<':32,
        '>':32
    },
    'RE2':{
        'Var':34,
        'Int':34,
        '(':34
    },
    'REop':{
        '<':35,
        '>':36
    }
}


# In[4]:


LetterAndDigit = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

state12 = dict({x :23 for x in LetterAndDigit.replace('f','')})
state12.update({'f':13})

state14 = dict({x :23 for x in LetterAndDigit.replace('l','')})
state14.update({'l':15})

state15 = dict({x :23 for x in LetterAndDigit.replace('s','')})
state15.update({'s':16})

state16 = dict({x :23 for x in LetterAndDigit.replace('e','')})
state16.update({'e':17})

state18 = dict({x :23 for x in LetterAndDigit.replace('o','')})
state18.update({'o':19})

state19 = dict({x :23 for x in LetterAndDigit.replace('r','')})
state19.update({'r':20})

dfa = {0:{  ' ':0,
            '{':1,
            '}':2,
            '(':3,
            ')':4,
            ';':5,
            '>':6,
            '<':7,
            '+':8,
            '=':9,
            '[':10,
            ']':11,
            
            'i':12,
            'e':14,
            'f':18,
            '-':21,
            
            '0': 22,
            '1': 22,
            '2': 22,
            '3': 22,
            '4': 22,
            '5': 22,
            '6': 22,
            '7': 22,
            '8': 22,
            '9': 22,
            
            'a': 23,
            'b': 23,
            'c': 23,
            'd': 23,
            'g': 23,
            'h': 23,
            'j': 23,
            'k': 23,
            'l': 23,
            'm': 23,
            'n': 23,
            'o': 23,
            'p': 23,
            'q': 23,
            'r': 23,
            's': 23,
            't': 23,
            'u': 23,
            'v': 23,
            'w': 23,
            'x': 23,
            'y': 23,
            'z': 23,
            
            'A': 23,
            'B': 23,
            'C': 23,
            'D': 23,
            'E': 23,
            'F': 23,
            'G': 23,
            'H': 23,
            'I': 23,
            'J': 23,
            'K': 23,
            'L': 23,
            'M': 23,
            'N': 23,
            'O': 23,
            'P': 23,
            'Q': 23,
            'R': 23,
            'S': 23,
            'T': 23,
            'U': 23,
            'V': 23,
            'W': 23,
            'X': 23,
            'Y': 23,
            'Z': 23,
            
            '*': 24
            },
         12:state12,
         13:{x :23 for x in LetterAndDigit},
         14:state14,
         15:state15,
         16:state16,
         17:{x :23 for x in LetterAndDigit},
         18:state18,
         19:state19,
         20:{x :23 for x in LetterAndDigit},
         21:{x :22 for x in '0123456789'},
         22:{x :22 for x in '0123456789'},
         23:{x :23 for x in LetterAndDigit}
         }


# In[5]:


class Node(object):
    def __init__(self, id_):
        self.id = id_
        self.children = []
        
    def __repr__(self):
        return str(self.id)
    
    def add_child(self, node):
        self.children.append(node) 
    
    def get_children(self):
        return self.children         
    
    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children


# In[6]:


def valueAndType(state,token):
    result = ''
    if state == 1:
        result = '{','openCurlyBracket'
    elif state == 2:
        result = '}','closeCurlyBracket'
    elif state == 3:
        result = '(','openParenthese'
    elif state == 4:
        result = ')','closeParenthese'
    elif state == 5:
        result = ';','semicolon'
    elif state == 6:
        result = '>','greaterThan'
    elif state == 7:
        result = '<','lessThan'
    elif state == 8:
        result = '+','plus'
    elif state == 9:
        result = '=','equal'
    elif state == 10:
        result = '[','openSqBracket'
    elif state == 11:
        result = ']','closeSqBracket'
    elif state == 13:
        result = 'if','reserveWord'
        symbolTable.update({'if':'reserveWord'})
    elif state == 17:
        result = 'else','reserveWord'
        symbolTable.update({'else':'reserveWord'})
    elif state == 20:
        result = 'for','reserveWord'
        symbolTable.update({'for':'reserveWord'})
    elif state == 22:
#         result = token,'number'
        result = 'Int','number'
        symbolTable.update({token:'number'})
    elif state == 23:
#         result = token,'identifier'
        result = 'Var','identifier'
        symbolTable.update({token:'identifier'})
    elif state == 24:
        result = '*','multiplication'
    return result


def getToken(input):
    pointer = -1
    state = 0
    token = ''
    steamOfToken = []
    while pointer < len(input):
#         อ่านต่อได้
        if pointer < len(input)-1:
            if state in dfa and input[pointer+1] in dfa[state]:
                state = dfa[state][input[pointer+1]]
                if state != 0:
                    token = token + input[pointer+1]
                pointer = pointer + 1
            else:
                if state in [12,14,15,16,18,19,]:
                    state = 23
                steamOfToken.append(valueAndType(state,token))
                token = ''
                state = 0
#         อ่านต่อไม่ได้
        else:
            steamOfToken.append(valueAndType(state,token))
            pointer = pointer + 1
    return steamOfToken


# In[90]:


def parsing(input):
    steamOfToken = [x[0] for x in input]
    print(steamOfToken)
    #dot = Digraph(comment='parsing tree')
    
    steamOfToken.append('$')
 
    stack = []
    root = Node('S')
#     stack.append('$')
    stack.append(Node('$'))
    stack.append(root)
    
    
    stackTree = []
    stackTree.append(root)
    
    tree = []
    i=1
    tree.append('S(0)')
    
#     print(stack)
    pointer = 0

    while len(stack)>0 and len(steamOfToken)>0 :
    #     can reduce
        if str(stack[-1]) not in parsingTable and len(stack)>1 :

            if str(stack[-1])==steamOfToken[pointer]:
                stack.pop()
                pointer = pointer + 1 
                
#       cannot reduce push new grammar
        elif str(stack[-1]) in parsingTable:
#             print('pointer',steamOfToken[pointer])
#             print('last',stack[-1])
#             print(parsingTable[stack[-1]])
            if steamOfToken[pointer] in parsingTable[str(stack[-1])]:
                last = stack.pop()
#                 print('last',last)
#                 print('root',root)
#                 print_tree(root)
                temp = parsingTable[str(last)][steamOfToken[pointer]]
                g = grammar[temp]
                
                
                
                if g[str(last)][0] != 'lambda':
                    a = []
                    for s in  reversed(g[str(last)]):
                        t = Node(s)
                        stack.append(t)
                        a.append(t)
                        
#                         last.add_child(t)
                        
                        
                    for m in  reversed(a):
                        last.add_child(m)



#                     for a in g[last]:
                        
#                         for j in tree:
#                             if last+'(' in j:
#                                 parent = j
# #                             print(parent)
                        
#                         dot.edge(parent,a+'('+str(i)+')',constraint='true')
                        
#                         tree.append(a+'('+str(i)+')')
#                         i=i+1
        
            else:
                return 'error1'
#         else:
#             return 'error2'
#         print('steam::',type(steamOfToken[pointer]))
#         print('stack[-1]:',type(str(stack[-1])))
#         print(str(stack[-1])== '$' and steamOfToken[pointer] == '$')
        if str(stack[-1])== '$' and steamOfToken[pointer] == '$':
#             dot.render('parsingTree',view=True)
            return 'accept',root
            
#         print('---')
        print(stack)
#         print_tree(root)
#         print('--------------')


# In[109]:


ip = input("Input : ")


# In[110]:


symbolTable = {}
token = getToken(ip)
a,root=parsing(token)


# In[105]:


print_tree(root)

