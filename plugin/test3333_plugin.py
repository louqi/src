# -*- coding:utf-8 -*-
'''
Created on 2015-4-23

@author: Administrator
'''
from plugin_super import ComputePlugin
class Test3333Plugin(ComputePlugin):
    def __init__(self,temp):
        self.temp = temp 
        self.ARRAY =[[1,2],[3,4]]
        
    def run_plugin(self):
        if self.use_able == True:
            import test3333
            self.D = test3333.sum(self.A,self.B,self.temp,self.ARRAY)
        
    def save_result(self):
        f = open('D://workspaces//plugin_demo//src//test3333.txt','w')
        #content = "AAAA"
        content = "D_"+str(self.D)+'\n'
        f.write(content)
        f.close()
        
    def get_input(self):
        f = open("D://workspaces//plugin_demo//src//test.txt",'r')
        try:
            all_the_text = f.readlines( )
        finally:
            f.close( )
        
        input_list = []
        for line in all_the_text:
            input_list.append(line.strip('\n').split('_')[1])
        self.A = input_list[0]
        self.B = input_list[1]

if __name__ == "__main__":
    demo = Test3333Plugin(8600)
    demo.activate_plugin()
    demo.activate_plugin()
    demo.get_input()
    demo.run_plugin()
    print demo.D
    demo.save_result()
    
        
        
    
        
    