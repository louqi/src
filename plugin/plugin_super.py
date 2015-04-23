# -*- coding:utf-8 -*-

'''
Created on 2015-4-22

@author: Administrator
'''
class ComputePlugin(object):
    use_able = False
    
    def activate_plugin(self):
        if self.use_able == False:
            self.use_able =True
        else:
            print "插件已经激活"
        
    def close_plugin(self):
        if self.use_able == True:
            self.use_able =False
        else:
            return "插件已经关闭"
    
    def run_plugin(self):
        if self.use_able == True:
            pass
        else:
            return "插件尚未激活，请先激活"
        
    
    def stop_plugin(self):
        pass
    
    def save_result(self):
        pass
        
        
        