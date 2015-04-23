# -*- coding:utf-8 -*-
'''
Created on 2015-4-23

@author: Administrator
'''
from plugin_super import ComputePlugin
class Test2222Plugin(ComputePlugin):
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b 
        self.c = c 
        self.d = d 
        
    def run_plugin(self):
        if self.use_able == True:
            import test2222
            self.A,self.B,self.ARRAY =  test2222.cal(self.a,self.b,self.c,self.d)
        
    def save_result(self):
        f = open('D://workspaces//plugin_demo//src//test.txt','w')
        #content = "AAAA"
        content = "A_"+str(self.A)+'\n'+"B_"+str(self.B)+"\n"
        f.write(content)
        f.close()

if __name__ == "__main__":
    demo = Test2222Plugin(1,2,3,4)
    demo.activate_plugin()
    demo.activate_plugin()
    demo.run_plugin()
    print demo.A,demo.B,demo.ARRAY
    demo.save_result()
        
        
    
        
    