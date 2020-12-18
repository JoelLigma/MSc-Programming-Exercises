# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:21:35 2020

@author: Joel
"""
# Ex04: OOP - Implementing a tree data structure

class Expr : # super class   

    # method to return a string
    def __str__(self) :
        return self.str_aux(0) # we use 0 as default fixity parameter
    
class Var(Expr) :  # this is a subclass with inheritance from super class Expr
    
    # constuctor to initialize variables
    def __init__(self, name) :
        self.name = name
        
    # method to evaluate an expression when a dictionary env is provided    
    def eval(self, env) :
        return env[self.name]
    
    # method to return a string
    def str_aux(self, fixity) :
        return self.name
    
    def Vars(self) :
        return self.name
       
class Not(Expr) : # this is a subclass with inheritance from super class Expr

    # class variables
    fixity = 4
    symbol = "!"
    
    # constuctor to initialize variables
    def __init__(self, name) :
        self.name = name
        
    # method to evaluate an expression when a dictionary env is provided  
    def eval(self, env) :
        return not(self.name.eval(env))
    
    # method to return a string
    def str_aux(self, fixity) :
        return f"!{self.name.str_aux(self.fixity)}"
       
    def Vars(self) :
        return self.name.Vars()
        
class BinOp(Expr) : # intermediate class for all logical operators that have 2 child nodes

    # constuctor to initialize variables
    def __init__(self, left, right) :
        self.left = left
        self.right = right
        
    # method to evaluate an expression when a dictionary env is provided                 
    def eval(self, env) :
        return self.op(self.left.eval(env),self.right.eval(env))  
    
    # method to return the string
    def str_aux(self, fixity) :
        s = self.left.str_aux(self.fixity) + self.symbol + self.right.str_aux(self.fixity)
        if self.fixity < fixity : # if inside fixity < outside fixity... 
            return "(" + s + ")" # add brackets
        else :
            return s # else don't
        
    def Vars(self) :
        """
        This method creates a list of all variables in the expression.
        """
        lst = []
        lst += self.left.Vars()
        lst += self.right.Vars()
        
        return lst
    
    def compute_combinations(self, n) :
        """
        This method computes all boolean combinations in a list of lists for
        the total number of unique variables n in an expression.
        """
        if n == 0: # stopping condition
            return [[]]
        boolean_lst = []
        for i in self.compute_combinations(n-1):
            boolean_lst += [i + [True]]
            boolean_lst += [i + [False]]
            
        return boolean_lst
    
    def evaluate_expression(self) :
        """
        This method evaluates an expression and adds the result as last element 
        to the list of boolean combinations.
        """
        # step 1 retrieve all variables in an expression and convert them to set
        var_set = set(self.Vars())
        # step 2 retrieve total number of unique variables
        n = len(var_set)
        # step 3 compute the boolean combinations
        combinations = self.compute_combinations(n)
        # step 4 create a list of dictionaries out of var_set and the combinations for evaluation
        lst_of_d = []
        for row in range(len(combinations)) :
            d = {}
            for col in range(len(combinations[0])) :
                d[list(var_set)[col]] = combinations[row][col]
            lst_of_d += [d]
        # step 5 add evaluation as last element to each sublist in boolean combination using list_of_d
        for row in range(len(combinations)) :
            combinations[row] += [self.eval(lst_of_d[row])] # evaluate each row of the dictionary
        return combinations, n, var_set
        
    def make_tt(self) :
        """
        This method returns the truth table as a string.
        """
        # access values from evaluate_expression()
        combinations, n, var_set = self.evaluate_expression()
        # initialize empty string to store the truth table 
        output = ""
        # add the unique variables to the empty string
        for var in var_set :
            output += var + "     |" + "\t"
        # add the expression to the string and then go to next line using '\n'
        output += str(self) + '\n'
        # add the boolean combinations to the string
        for row in range(len(combinations)) :
            for col in range(len(combinations[0])) :
                if str(combinations[row][col]) == "True" and col < n :
                    output += str(combinations[row][col]) + "  |" + "\t"
                elif str(combinations[row][col]) == "False" and col < n :
                    output += str(combinations[row][col]) + " |" + "\t"
                # if we reach the evaluation we want to add it to the string WITHOUT adding a "|"
                else :
                    output += str(combinations[row][col]) + "\t"
            # next line
            output += '\n'
        return output   
    
    def isTauto(self) :
        """
        A proposition is called a tautology if it is always true. That is, the
        truthtable contains only True| in the last column.
        """
        # accesing selected values of evalute_expression()
        evaluated_booleans, n = self.evaluate_expression()[0:2]
        lst = []
        # keeping track whether the last column only contains True or not
        for row in range(len(evaluated_booleans)) :
            lst += [evaluated_booleans[row][n]] # n to access last column
        if sum(lst) == len(evaluated_booleans) : # only sums the number of Trues so we can verify hereby
            return True
        else :
            return False

# subclasses with inheritance from intermediate class BinOp and super class Expr
class Or(BinOp) : 
    
    # class variables
    fixity = 2
    symbol = "|"
    
    def op(self, x, y) :
        return x or y       
        
class Eq(BinOp) :
    
    # class variables
    fixity = 1
    symbol = "=="

    def op(self, x, y) :
        return x == y 
    
class And(BinOp) :
    
    # class variables
    fixity = 3
    symbol = "&"

    def op(self, x, y) :
        return x and y

"test data"

e1 = Or(Var("x"),Not(Var("x")))
e2 = Eq(Var("x"),Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Eq(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))
e5 = Eq(Eq(Eq(Var("p"),Var("q")),Var("r")),Eq(Var("p"),Eq(Var("q"),Var("r"))))

print(e1)
print(e2)
print(e3)
print(e4)
print(e5)

print(And(Not(Var("p")),Var("q")))
print(Not(And(Var("p"),Var("q"))))
print(Or(And(Var("p"),Var("q")),Var("r")))
print(And(Var("p"),Or(Var("q"),Var("r"))))
print(Eq(Or(Var("p"),Var("q")),Var("r")))
print(Or(Var("p"),Eq(Var("q"),Var("r"))))

print (e2.eval({"x" : True}))
print (e3.eval({"x" : True, "y" : True}))
print (e4.eval({"x" : False, "y" : True}))

print(e1.make_tt())
print(e2.make_tt())
print(e3.make_tt())
print(e4.make_tt())
print(e5.make_tt())

print (And(Var("x"),And(Var("y"),Var("z"))))
print (And(And(Var("x"),Var("y")),Var("z")))

print (e1.isTauto())
print (e2.isTauto())
print (e3.isTauto())
print (e4.isTauto())
print (e5.isTauto())