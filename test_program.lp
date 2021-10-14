x_2.
x_3.
x_4.
x_5.
x_6.
x_7.
x_8.
x_9.
x_10.
x_11.
x_12.
x_13.
x_14.
x_15.
x_16.
in(a0_0) :- not x_18.
in(a1_0) :- not x_20.
in(a2_2) :- not x_22.
in(a3_0) :- not x_24.
in(a4_2) :- not x_26.
in(a5_2) :- not x_28.
x_18 :- not in(a0_0).
x_20 :- not in(a1_0).
x_22 :- not in(a2_2).
x_24 :- not in(a3_0).
x_26 :- not in(a4_2).
x_28 :- not in(a5_2).
x_29 :- in(a2_2).
x_30 :- in(a2_2).
x_31 :- in(a2_2).
x_32 :- in(a4_2).
x_33 :- in(a4_2).
x_31 :- in(a4_2).
x_34 :- in(a5_2).
x_33 :- in(a5_2).
x_30 :- in(a5_2).
not_defended(a3_0) :- not x_33.
not_defended(a4_2) :- not x_33.
not_defended(a5_2) :- not x_33.
not_defended(a1_0) :- not x_30.
not_defended(a2_2) :- not x_30.
not_defended(a5_2) :- not x_30.
not_defended(a0_0) :- not x_31.
not_defended(a2_2) :- not x_31.
not_defended(a4_2) :- not x_31.
x_1 :- not_defended(a3_0), in(a3_0).
x_1 :- not_defended(a4_2), in(a4_2).
x_1 :- not_defended(a5_2), in(a5_2).
x_1 :- not_defended(a1_0), in(a1_0).
x_1 :- not_defended(a2_2), in(a2_2).
x_1 :- not_defended(a0_0), in(a0_0).
x_1 :- in(a3_0), in(a2_2).
x_1 :- in(a4_2), in(a2_2).
x_1 :- in(a5_2), in(a2_2).
x_1 :- in(a1_0), in(a4_2).
x_1 :- in(a2_2), in(a4_2).
x_1 :- in(a5_2), in(a4_2).
x_1 :- in(a0_0), in(a5_2).
x_1 :- in(a2_2), in(a5_2).
x_1 :- in(a4_2), in(a5_2).
:- x_1.

#show not_defended/1.