import numpy as np
#case1 攻击范围内有敌方士兵,集中最少火力杀死,造成最大伤害 输入map,blood

enemyAttack = {} #记录能攻击到的地方,key：id,value：id
ownAttack = {}
AttckAction = {}  #key:ownid value:enemyid



selfmap =np.array([
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,4,9,7,9,9,9,9,9,9,9,9,9],
[9,9,4,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,7,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,7,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9],
[9,9,9,9,9,9,9,9,9,9,9,9,9]
])

bloodmap =np.array([
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,3,0,1,0,0,0,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,3,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,3,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0]
])
#距离目的地远近，给solider farmer 增加一个属性 目的地


#总体攻击策略，对视野范围内的士兵和敌人进行统计，考虑能攻击的链接，先拿走不能攻击（暂时保留 去攻击农民）和仅能攻击1个人的，释放，重复操作，直到剩下的都是超过2的
#看和攻击到的和血量的比较，如果能攻击的自己士兵大于血量，选择自己的士兵中能攻击的人最少的血量数士兵，释放，重复操作
#直接遍历，从敌人遍历，靠近自己大本营的先攻击
#攻击完士兵后，不能走的攻击农民，策略一致，如果达到目的地，那么超视野范围内的农民移动一步，或者超攻击后没有死亡的的农民移动一步
#
ownSoliderCordLst = np.argwhere(selfmap==4)
enemySoliderCordLst = np.argwhere(selfmap==7)
for solider in ownSoliderCordLst:
    # 计算solider的攻击范围
    ownAttack[soliderID] = []
    for enemy in enemySoliderCordLst:
        enemyAttack[enemyid] = [soliderID]
        if abs(solider[0]-enemy[0])<=3 or abs(solider[1]-enemy[1])<=3:
            ownAttack[soliderID].append(enemyid)
#把只能攻击一个敌人的链接释放，重复操作
changeFlag = True
while(changeFlag ==True):
    changeFlag = False
    for ownsoliderid in ownAttack.keys():
        if len(ownAttack[ownsoliderid]) == 1:
            changeFlag = True
            #ownsoliderid attack ownsoliderid[0]
            #对应缓冲血量减1
            #删除enemyAttack中的key
            #删除ownAttack的key
        if len(ownAttack[ownsoliderid]) == 0:
            #超目标走下一步

for enemyid in enemyAttack.keys():
    #如果能攻击人大于血量，排序己方能攻击的人的最少，选取血量N个，
    #N个自己的士兵进行攻击，删除字典
    #上述重复
#剩下的都是本轮砍不死的，直接遍历，能看多少砍多少





    # 获取攻击范围内的敌人id
    # 更新

import pip
from pip._internal.utils.misc import get_installed_distributions
for dist in pip._internal.utils.misc.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)