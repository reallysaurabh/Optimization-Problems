import random
from pulp import *

######@@@@@@@@@@--Initializations and Declarations--@@@@@@@@@@###########

#Supply limits
#s1=[random.randint(30,35), random.randint(30,35), random.randint(30,35)]
s1=random.randint(90,100)

s2=random.randint(90, 100)

s3=random.randint(90, 100)


#Demand Limits
d1=random.randint(90, 100)

d2=random.randint(90, 100)

d3=random.randint(90, 100)

#Prices of products
p1=random.randint(70,80)

p2=random.randint(35,45)

p3=random.randint(55,65)

#Cost of production and processing
c1=random.randint(50,60)

c2=random.randint(15,25)

c3=random.randint(35,45)

#quality of sources, blends and final products
a1=random.random()

a2=random.random()

a3=random.random()

b1=random.random()

b2=random.random()

b3=random.random()

q1=random.random()

q2=random.random()

q3=random.random()


#Creating variables of flow from source to pool, with a lower limit of zero
x11=LpVariable("x11",0,None,LpInteger)

x12=LpVariable("x12",0,None,LpInteger)

x13=LpVariable("x13",0,None,LpInteger)

x21=LpVariable("x21",0,None,LpInteger)

x22=LpVariable("x22",0,None,LpInteger)

x23=LpVariable("x23",0,None,LpInteger)

x31=LpVariable("x31",0,None,LpInteger)

x32=LpVariable("x32",0,None,LpInteger)

x33=LpVariable("x33",0,None,LpInteger)


#Creating variables of flow from pool to final product, with a lower limit of zero
y11=LpVariable("y11",0,None,LpInteger)

y12=LpVariable("y12",0,None,LpInteger)

y13=LpVariable("y13",0,None,LpInteger)

y21=LpVariable("y21",0,None,LpInteger)

y22=LpVariable("y22",0,None,LpInteger)

y23=LpVariable("y23",0,None,LpInteger)

y31=LpVariable("y31",0,None,LpInteger)

y32=LpVariable("y32",0,None,LpInteger)

y33=LpVariable("y33",0,None,LpInteger)

######@@@@@@@@@@------------------------------------@@@@@@@@@@###########











####### 1. Minimizing cost of flow from S1 ##############################

#Variable to contain problem data
prob=LpProblem("Pooling Problem", LpMinimize)

#adding objective function to prob
prob+= c1*x11+ c1*x12+ c1*x13,"flows from s1 to p1, p2 and p3"

#entering constraints to prob
prob+=x11+x12+x13 <= s1, "supply quantity from source 1  "
prob+=b1*(x11+x21+x31)>=a1*x11+a2*x21+a3*x31,"Mixing rule for pool 1"
prob+=y11+y12+y13==x11+x21+x31,"Mass balance on pool 1"


#writing the problem in a file poolingproblem.lp
prob.writeLP("poolingproblem.lp")

#calling the solver to solve the problem
prob.solve()

#printing status

print LpStatus[prob.status]

for v in prob.variables():
    print v.name,"=", v.varValue
    
cost1=value(prob.objective)
print "cost of flow from Source 1:  ", cost1, '\n'

#######################################################################




####### 2. Minimizing cost of flow from S2 ##############################

#Variable to contain problem data
prob=LpProblem("Pooling Problem", LpMinimize)

#adding objective function to prob
prob+= c2*x21+ c2*x22+ c2*x23,"flows from s2 to p1, p2 and p3"

#entering constraints to prob
prob+=x21+x22+x23 <= s2, "supply quantity from source 2"
prob+=b2*(x12+x22+x32)>=a1*x12+a2*x22+a3*x32,"Mixing rule for pool 2"
prob+=y21+y22+y23==x12+x22+x32,"Mass balance on pool 2"


#writing the problem in a file poolingproblem.lp
prob.writeLP("poolingproblem.lp")

#calling the solver to solve the problem
prob.solve()

#printing status
print LpStatus[prob.status]

for v in prob.variables():
    print v.name,"=", v.varValue
    
cost2=value(prob.objective)
print "cost of flow from Source 2:  ", cost2, '\n'

#######################################################################


####### 3. Minimizing cost of flow from S3 ##############################

#Variable to contain problem data
prob=LpProblem("Pooling Problem", LpMinimize)

#adding objective function to prob
prob+= c3*x31+ c3*x32+ c3*x33,"flows from s3 to p1, p2 and p3"

#entering constraints to prob
prob+=x31+x32+x33 <= s3, "supply quantity from source 3 "
prob+=b3*(x13+x23+x33)>=a1*x13+a2*x23+a3*x33,"Mixing rule for pool 3"
prob+=y31+y32+y33==x13+x23+x33,"Mass balance on pool 3"


#writing the problem in a file poolingproblem.lp
prob.writeLP("poolingproblem.lp")

#calling the solver to solve the problem
prob.solve()

#printing status
print LpStatus[prob.status]

for v in prob.variables():
    print v.name,"=", v.varValue
    
cost3=value(prob.objective)
print "cost of flow from Source 3:  ", cost3, '\n'

#######################################################################


####### 1. Maximizing cost of flow from Pool 1 ##############################

#Variable to contain problem data
prob=LpProblem("Pooling Problem", LpMaximize)

#adding objective function to prob
prob+= p1*y11+ p1*y21+ p1*y31,"flows from pools to product 1"

#entering constraints to prob
prob+=y11+y21+y31 <= d1, "demand for product 1  "
prob+=q1*y11+q1*y21+q1*y31>=b1*y11+b2*y21+b3*y31,"Mixing rule of Product 1"

#writing the problem in a file poolingproblem.lp
prob.writeLP("poolingproblem.lp")

#calling the solver to solve the problem
prob.solve()

#printing status
print LpStatus[prob.status]

for v in prob.variables():
    print v.name,"=", v.varValue
    
sp1=value(prob.objective)
print "selling price of product 1:  ", sp1,'\n'

#######################################################################


####### 2. Maximizing cost of flow from Pool 2 ##############################

#Variable to contain problem data
prob=LpProblem("Pooling Problem", LpMaximize)

#adding objective function to prob
prob+= p2*y12+ p2*y22+ p2*y32,"flows from pools to product 2 "

#entering constraints to prob
prob+=y12+y22+y32 <= d2, "demand for product 2  "
prob+=q2*y12+q2*y22+q2*y32>=b1*y12+b2*y22+b3*y32,"Mixing rule of product 2"


#writing the problem in a file poolingproblem.lp
prob.writeLP("poolingproblem.lp")

#calling the solver to solve the problem
prob.solve()

#printing status
print LpStatus[prob.status]

for v in prob.variables():
    print v.name,"=", v.varValue
    
sp2=value(prob.objective)
print "selling price of product 2:  ", sp2, '\n'

#######################################################################


####### 3. Maximizing cost of flow from Pool 3 ##############################

#Variable to contain problem data
prob=LpProblem("Pooling Problem", LpMaximize)

#adding objective function to prob
prob+= p3*y13+ p3*y23+ p3*y33,"flows from pools to product 3"

#entering constraints to prob
prob+=y13+y23+y33 <= d3, "demand for product 3  "
prob+=q3*(y13+y23+y33)>=b1*y13+b2*y23+b3*y33,"Mixing rule for product 3"


#writing the problem in a file poolingproblem.lp
prob.writeLP("poolingproblem.lp")

#calling the solver to solve the problem
prob.solve()

#printing status
print LpStatus[prob.status]

for v in prob.variables():
    print v.name,"=", v.varValue
    
sp3=value(prob.objective)
print "selling price of product 3:  ", sp3, '\n'

#######################################################################


print "\nFinal Maximized profit :  ", (sp1-cost1)+(sp2-cost2)+(sp3-cost3)

