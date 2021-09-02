arg(a0_0).
arg(a1_0).
arg(a2_0).
arg(a2_1).
arg(a2_2).
arg(a3_2).
arg(a3_4).
att(a0_0,a1_0).
att(a0_0,a4_2).
att(a0_0,a4_4).
att(a0_0,a4_6).
att(a0_0,a7_2).
att(a0_0,a10_6).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Encoding for admissible extensions
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Guess a set S \subseteq A
in(X) :- not out(X), arg(X).
out(X) :- not in(X), arg(X).

%% S has to be conflict-free
:- in(X), in(Y), att(X,Y).

%% The argument x is defeated by the set S
defeated(X) :- in(Y), att(Y,X).

%% The argument x is not defended by S
not_defended(X) :- att(Y,X), not defeated(Y).

%% All arguments x \in S need to be defended by S
:- in(X), not_defended(X).
