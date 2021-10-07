a(1) :- not x_5.
x_5 :- not a(1).
b(1) :- not x_6.
x_6 :- not b(1).
c(1) :- not x_7.
x_7 :- not c(1).
x_1 :- not a(1), b(1).
x_1 :- not b(1), c(1).
:- x_1.


