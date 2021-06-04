% Lecture Examples(1)
a:- not b.
b:- not a.
c:- a .
c:- b,d.
d:- b,c.
d:- e.
e:-  b, not a.
e:-  c, d.

% Lecture Example(2)

%a:- not b.
%b:- not a.
%c:- a ,b.
%c:- d.
%d:- a.
%d:- b,c.
%e:-  not b, not a.
%e:- a.