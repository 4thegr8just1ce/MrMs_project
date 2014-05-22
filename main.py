#import packages
import MrMs as m
Kris = m.Miss("Kristy",18,100500)
Masha = m.Miss("Maria",17,100500)
Anna = m.Miss("Anna",138,100401)
Vasya = m.Mister("Vasya",18,2001000)
Masha.setRate(1000)
MissItmo2014 = m.Rate(Anna,Kris,Masha)
MissItmo2014.showWinner()
MissItmo2014.candidatesSort()
MissItmo2014.candidatesSort("age")
MissItmo2014.candidatesSort("name")
