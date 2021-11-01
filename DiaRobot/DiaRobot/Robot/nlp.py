from enum import Enum
from DiaRobot.Robot.navigation import Navigation
from DiaRobot.Robot.query import Query
from DiaRobot.Robot.reserve import Reserve
from DiaRobot.Robot.recommend import Recommend

class Status(Enum):
    prepro = 1
    navi = 2
    que = 3
    reser = 4
    recom = 5

current = Status.prepro

#todo
#消息处理，返回语义树
#需要判断消息类型
#需要判断此时状态，如果是预处理则需要nlp，如果非预处理不需要nlp（不确定）
def MsgProcess():
    pass

#todo
#根据语义树选择分支功能
#需要正确处理分支功能不包含的功能
def DemandProcess():
    MsgProcess()
    #then select
    #Navigation() or Query() or Reserve() or Recommend() or else case
    #and change current
    pass

