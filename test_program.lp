arg(a0_0).
arg(a1_0).
arg(a2_2).
arg(a3_0).
arg(a4_2).
arg(a5_2).
att(a2_2,a3_0).
att(a2_2,a4_2).
att(a2_2,a5_2).
att(a4_2,a1_0).
att(a4_2,a2_2).
att(a4_2,a5_2).
att(a5_2,a0_0).
att(a5_2,a2_2).
att(a5_2,a4_2).
in(a0_0):-not out(a0_0).
in(a1_0):-not out(a1_0).
in(a2_2):-not out(a2_2).
in(a3_0):-not out(a3_0).
in(a4_2):-not out(a4_2).
in(a5_2):-not out(a5_2).
out(a0_0):-not in(a0_0).
out(a1_0):-not in(a1_0).
out(a2_2):-not in(a2_2).
out(a3_0):-not in(a3_0).
out(a4_2):-not in(a4_2).
out(a5_2):-not in(a5_2).
defeated(a3_0):-in(a2_2).
defeated(a4_2):-in(a2_2).
defeated(a5_2):-in(a2_2).
defeated(a1_0):-in(a4_2).
defeated(a2_2):-in(a4_2).
defeated(a5_2):-in(a4_2).
defeated(a0_0):-in(a5_2).
defeated(a2_2):-in(a5_2).
defeated(a4_2):-in(a5_2).
not_defended(a3_0):-not defeated(a2_2).
not_defended(a4_2):-not defeated(a2_2).
not_defended(a5_2):-not defeated(a2_2).
not_defended(a1_0):-not defeated(a4_2).
not_defended(a2_2):-not defeated(a4_2).
not_defended(a5_2):-not defeated(a4_2).
not_defended(a0_0):-not defeated(a5_2).
not_defended(a2_2):-not defeated(a5_2).
not_defended(a4_2):-not defeated(a5_2).
:-not_defended(a3_0),in(a3_0).
:-not_defended(a4_2),in(a4_2).
:-not_defended(a5_2),in(a5_2).
:-not_defended(a1_0),in(a1_0).
:-not_defended(a2_2),in(a2_2).
:-not_defended(a0_0),in(a0_0).
:-in(a3_0),in(a2_2).
:-in(a4_2),in(a2_2).
:-in(a5_2),in(a2_2).
:-in(a1_0),in(a4_2).
:-in(a2_2),in(a4_2).
:-in(a5_2),in(a4_2).
:-in(a0_0),in(a5_2).
:-in(a2_2),in(a5_2).
:-in(a4_2),in(a5_2).
#show in/1.
#show not_defended/1.
