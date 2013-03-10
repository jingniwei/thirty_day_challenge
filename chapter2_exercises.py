# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Jingni Wei

#2.1
'''
It seems that python will interpret numbers which start with 0 as hexidecimals. 
Hexidecimals must have digits smaller than 8.  So >>> zipcode = 02132 will work since 
it contains numbers no larger than 8, >>> zipcode = 02492 contains a 9 which will cause 
a syntax error. 
'''

#2.2
'''
print 5 
x=5 
print x
ans=x+1
print(ans)

There is no output from running the program as it. 

'''

#2.3
'''
1. 8 type int
2. 8.5 type float
3. 4.0 type float
4. 11 type int
5. ..... type string
'''

#2.4
'''
1. 
pi = 3.1415926535897932
print((4.0/3.0)*pi*5**3)

volume= 523.598775598

2. 
price= 24.95
copies= 60
shipping= (copies-1)*.75 + 3.0
cost = .6*price*copies + shipping

print(cost)

cost= 945.45

3. 
start= 6*60*60+52*60 # TIME IN SECONDS 
run = 8*60+15 + 3*(7*60 + 12) + 8*60+15
endtime = start+run
endhour= endtime/3600
endmin= (endtime%3600)/60
endsec= (endtime%3600)%60

print (str(endhour)+":" + str(endmin) + ":" + str(endsec))

Time finish run is 7:30:06
'''
