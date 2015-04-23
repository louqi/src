# -*- coding:utf-8 -*-

'''
在这个文件中定义了一个类：Rotor类，类中的所有成员变量与Input函数中的所有参数一一对应，对单个桨叶的
所有参数赋值只需要在这个类里面赋值即可
'''

class Rotor():
    PI = 3.141592653589793
    #-----------CASE
    TITLE = 'AEROELASTIC ANALYSI TEST'
    NCASE = 1
    OPINIT = 0
    NPRINT = 1
    
    #-----------AIRFOIL
    NFOIL=2
    
    #-----------ENVIRONMENT
    DENSE  = 1.225                        # KG/M**3
    TEMP   = 15.0                            # DEG
    ALTMSL = 0.0                         # M
    CSOUND = 340.0                    # M/S
    #-----------ROTORSTRUCTURE
    ROTOR_NAME  ='Z10 MODEL ROTOR'
    ROTOR_CONFIG=0
    ROTOR_ROTATE=1
    ROTOR_NBLADE=5
    ROTOR_R=2.0
    ROTOR_RHUB=0.31
    ROTOR_OMEGA=108.7

    rotor_paralist_INT=[NCASE,OPINIT,NPRINT,NFOIL,#1-4
                        ROTOR_CONFIG,ROTOR_ROTATE,ROTOR_NBLADE,#5-7
                        NELEMENT,#8
                        NPANEL,NPSI,NX,NSTEP]#9-12
    rotor_paralist_double = [DENSE,TEMP,ALTMSL,CSOUND,#1-4
                             ROTOR_R,ROTOR_RHUB,ROTOR_OMEGA,#5-7
                             ROTOR_BETAP,ROTOR_ETIP,ROTOR_SIGMA,ROTOR_GAMMA,ROTOR_NU,ROTOR_WK,#8-13
                             ROTOR_THETATW,ROTOR_THETAX,ROTOR_THETAI,ROTOR_RHINGE,#14-17
                             ROTOR_KFLAP,ROTOR_DFLAP,ROTOR_KLAG,ROTOR_DLAG,ROTOR_KPITCH,ROTOR_DPITCH,#18-23
                             ROTOR_GDAMPU,ROTOR_GDAMPV,ROTOR_GDAMPW,ROTOR_GDAMPP,#24-27
                             RNODE_1,RNODE_2,RNODE_3,RNODE_4,RNODE_5,RNODE_6,RNODE_7,RNODE_8,#28-35
                             RC,BTIP,VWIND,ALPHAS,COLL,LATCYC,LNGCYC]#36-42
    rotor_title = TITLE
    rotor_name = ROTOR_NAME
    rotor_carpalpath = "D:\\RotorPython\\datain\\WTE.CARPAL"
'''
rotor = Rotor()
import pyd_one
TRIM_VAR = pyd_one.func(rotor.rotor_name,rotor.rotor_carpalpath,
rotor.rotor_paralist_INT,rotor.rotor_paralist_double,
34.3984256,821.2,0.005,0.0001)
import pyd_two
Result = pyd_two.func(rotor.rotor_name,rotor.rotor_carpalpath,
rotor.rotor_paralist_INT,rotor.rotor_paralist_double,
TRIM_VAR)
	'''
	
rotor = Rotor()
'''print rotor.rotor_paralist_INT
print rotor.rotor_paralist_double
print rotor.rotor_name
print rotor.rotor_title'''
    
'''import FUNCTIONOFINITRIM
print FUNCTIONOFINITRIM.__doc__  
trim_var=FUNCTIONOFINITRIM.functionofinitrim(rotor.rotor_name,rotor.rotor_carpalpath,rotor.rotor_paralist_INT,rotor.rotor_paralist_double,30,1038,0.006,0.0001)  
print trim_var[0],trim_var[1],trim_var[2],trim_var[3]
trim_var=[0.210928355479812 ,-0.02736476263125272, 0.006164083574393392 ,0.02562609098290452]
print trim_var'''
'''import FUNCTIONOFJOCABIAN
print FUNCTIONOFJOCABIAN.__doc__
FUNCTIONOFJOCABIAN.trim_solution(rotor.rotor_name,rotor.rotor_carpalpath,rotor.rotor_paralist_INT,rotor.rotor_paralist_double,34.3984256,821.2,0.005,0.0001)
print rotor.PI
print rotor.rotor_carpalpath'''
'''import FUNCTIONOFPARTONE
print FUNCTIONOFPARTONE.__doc__
TRIM_VAR = FUNCTIONOFPARTONE.trim_solution(rotor.rotor_name,rotor.rotor_carpalpath,rotor.rotor_paralist_INT,rotor.rotor_paralist_double,34.3984256,821.2,0.005,0.0001)
#print TRIM_VAR
print "**"
print TRIM_VAR'''
'''import FUNCTIONOFPARTTWO
print FUNCTIONOFPARTTWO.__doc__
a,b=FUNCTIONOFPARTTWO.trim_solution(rotor.rotor_name,rotor.rotor_carpalpath,rotor.rotor_paralist_INT,rotor.rotor_paralist_double,34.3984256,821.2,0.005,0.0001,TRIM_VAR)
print a,b'''

import FUNCTIONONE
print FUNCTIONONE.__doc__
TRIM_VAR = FUNCTIONONE.trim_solution_partone(rotor.rotor_name,rotor.rotor_carpalpath,rotor.rotor_paralist_INT,rotor.rotor_paralist_double,34.3984256,821.2,0.005,0.0001)
for a in TRIM_VAR:
    a = TRIM_VAR*180.0/3.141592653589793
print TRIM_VAR


'''import FUNCTIONTWO
print FUNCTIONTWO.__doc__
trim_var,jocabian,f = FUNCTIONTWO.trim_solution_parttwo(rotor.rotor_name,rotor.rotor_carpalpath,rotor.rotor_paralist_INT,rotor.rotor_paralist_double,34.3984256,821.2,0.005,0.0001,TRIM_VAR)
print trim_var
print jocabian
print f


import FUNCTIONPARTTHREE
print FUNCTIONPARTTHREE.__doc__
FUNCTIONPARTTHREE.functionpartthree(rotor.rotor_name,rotor.rotor_carpalpath,rotor.rotor_paralist_INT,rotor.rotor_paralist_double,jocabian,f,trim_var,34.3984256,821.2,0.005,0.0001)
'''
