
from include import weapon_data as wp
from include import Relic_data as re
from include import buff
from include import skill_data
from include import other_buff
from include import calc
class Noelle():
    def __init__(self,data):
        '''
        初始化数据
        basic_data_list={
            "ATK":"攻击力"
            "DEF":"防御力"
            "Noelle_num":"命座数"
            "A_Magn":"普攻等级"
            "Q_Magn":"大招等级"
            "Crit_rate":"暴击率"
            "Crit_dmg":"暴击伤害"
            "Weapon":"武器"
            "Weapon_num":"武器精炼度"
            "Relic":"圣遗物套装"
            "basic_ATK":"攻击力白板"
            "basic_DEF":"防御力白板"
        }
        '''
##        data = {'ATK': 1308, 'DEF': 2011, 'Noelle_num': 6,
##                'A_Magn': 10, 'Q_Magn': 13, 'Crit_rate': 0.591, 'Crit_dmg': 2.587,
##                'Weapon': 1, 'Weapon_num': 2, 'Relic': 1}#测试数据
        self.basic_data = data
        self.basic_data.update({'basic_ATK':191+wp.basic_ATK[data['Weapon']],'basic_DEF':799})
        self.A_Magn ={}
        for k,v in skill_data.A_Magn.items():
            self.A_Magn[k]= v[data["A_Magn"]]
        self.DEF2ATK = skill_data.Q_Magn[data["Q_Magn"]]
        if(data["Noelle_num"]==6):
            self.DEF2ATK += 0.5
        self.buff = wp.get_buff(data["Weapon"],data["Weapon_num"])+re.get_buff(data["Relic"])+other_buff.get_buff(data["Other_buff"])
        self.output = ''
        self.calc()

    def calc(self):
        self.hit,self.calc_ATK,self.expect = calc.calc(self.basic_data,self.buff,self.A_Magn,self.DEF2ATK)

    def __str__(self):
        if self.output:
            return self.output
        s = ''
        s = s+'女仆暴击率为：{:.1f}%，暴击伤害为：{:.1f}%\n'.format(self.basic_data['Crit_rate']*100,self.basic_data['Crit_dmg']*100)
        s = s+'\n女仆吃满被动时的开大攻击力为：{:.2f}'.format(self.calc_ATK[buff.on])+'\n'
        for i in range(1,5):
            s = s+'女仆开大第{:d}刀暴击的伤害为：{:.2f}'.format(i,self.hit[buff.on][i])+'\n'
        s = s+'\n女仆无被动时的开大攻击力为：{:.2f}'.format(self.calc_ATK[buff.off])+'\n'
        for i in range(1,5):
            s = s+'女仆开大第{:d}刀暴击的伤害为：{:.2f}'.format(i,self.hit[buff.off][i])+'\n'
        s = s+'\n该女仆开大尾刀的最大输出期望值为：{:.2f}'.format(self.expect[buff.on])+'\n'
        s = s+'该女仆开大尾刀的最小输出期望值为：{:.2f}'.format(self.expect[buff.off])
        self.output = s
        return s

    __repr__ = __str__

    def inspect(self):
        '''
        练度检查
        '''
        
        s = ''
        if self.basic_data["A_Magn"]<9:
            s += '你的普攻等级过低！\n'
        if self.basic_data["Q_Magn"]<12:
            s += '你的大招等级过低！\n'
        if self.basic_data["A_Magn"]<self.basic_data["Q_Magn"]-3:
            s += '先拉普攻！！哼啊啊啊啊啊啊啊啊！\n'
        expect = self.expect[buff.on]
        if expect < 18000:
            s += '你的女仆DPS不及格！\n'
        elif 18000 < expect < 22000:
            s += '你的女仆处于及格水平\n'
        elif 22000 < expect < 24000:
            s += '你的女仆处于小毕业水平\n'
        elif 24000 < expect:
            s += '你的女仆已经毕业啦！\n'
        return(s)
    

if __name__ =='__main__':
    n = Noelle()
    print(n.basic_data)
    
