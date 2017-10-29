#Ri
Ai=0.25 
hi=10
Ri=1/(Ai*hi) 
#Rf
Af=Ai
kf=0.026
Lf=0.03
Rf=Lf/(kf*Af)
#Rp1
Ap1=0.25
kp1=0.22
Lp1=0.02
Rp1=Lp1/(Ap1*kp1)
#Rp2
Rp2=Rp1
#Rpc1
Apc1=0.015
kpc1=0.22
Lpc1=0.16
Rpc1=Lpc1/(Apc1*kpc1)
#Rpc2
Rpc2=Rpc1
#Rb
Ab=0.22
kb=0.72
Lb=0.16
Rb=Lb/(Ab*kb)
#R0
A0=Ai
h0=25
R0=1/(h0*A0)
Rpar=1/(1/Rb+1/Rpc1+1/Rpc2)
Rtot=Ri+Rp1+Rp2+R0+Rpar+Rf
Ti=20
T0=-10
Qunit=(Ti-T0)/Rtot
Qwall=Qunit*15/0.25