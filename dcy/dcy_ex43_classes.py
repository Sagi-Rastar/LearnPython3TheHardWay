"""
# 43.1.1 写或画出这个问题;
# 43.1.2 抽取关键概念并予以研究
# 43.1.3 为这些概念创建类的层级结构和对象地图
    ## 这一步个人觉得非常有用，思考一下这些名词的适用范围，
    ## 更大的范围的名词去替换其同义但更狭义的名词；
    ## 不准备开发的名词也可以预留出来接口；
#  43.1.4 编写类代码并通过测试来运行
"""
from inspect import _Object
import pstats


class Scene(object):
    
    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(slef):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass


class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()