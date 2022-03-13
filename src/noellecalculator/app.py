"""
A simple calculator
"""
import toga
from toga.style import Pack
from toga.style.pack import *
from include.weapon_data import weapons_list
from include.Relic_data import Relics_list
from include.other_buff import other_buff_list
from include.main_func import Noelle
from sys import exit

version = 3.0
title = "诺艾尔期望计算器"+str(version)

data_name = [["ATK","攻击力"],
            ["DEF","防御力"],
            ["Noelle_num","命座数"],
            ["A_Magn","普攻等级"],
            ["Q_Magn","大招等级"],
            ["Crit_rate","暴击率"],
            ["Crit_dmg","暴击伤害"],
            ["Weapon","武器"],
            ["Weapon_num","武器精炼度"],
            ["Relic","圣遗物套装"]]
data_type = ["int",
             "int",
             "int",
             "int",
             "int",
             "float",
             "float",
             "choose",
             "int",
             "choose"]
data_range = [[0,5000],
              [0,5000],
              [0,6],
              [1,11],
              [1,13],
              [0.05,1],
              [0.5,5],
              weapons_list,
              [1,5],
              Relics_list]

class NoelleCalculator(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        button_box = toga.Box(style=Pack(direction=ROW,padding=5))
        button1 = toga.Button('返回',style=Pack(padding=5),on_press=self.last)
        empty = toga.Box(style=Pack(height=5,flex=1))
        self.enter = toga.Button('确定',style=Pack(padding=5),on_press=self.next,enabled=False)
        button_box.add(button1)
        button_box.add(empty)
        button_box.add(self.enter)
        self.main_box.add(button_box)
        
        self.data = {}
        self.var = []
        self.box_list = []
        self.index = 0
        self.other_buff = []


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

        self.build_boxs()

    def build_boxs(self):
        width = self.main_window.size[1]
        msg = '''欢迎来到女仆诺艾尔的尾刀期望计算器v%s版本\n
by-bilibili夜雪千沫\n\n
计算以90级诺艾尔对虚弱的93级急冻树伤害为准\n\n
珍爱生命，远离PVP\n\n'''%(version)
        Label1 = toga.MultilineTextInput(readonly=True,style=Pack(flex=1,
        width=width,text_align=CENTER,alignment=CENTER,padding=(0,10),font_size=15))
        Label1.value = msg
        self.agree = toga.Switch('我已经阅读上述事项',style=Pack(width = width,flex=1,
            alignment=CENTER,text_align=CENTER,font_size=15,padding=15),on_toggle=self.decide)
        box0 = toga.Box(style=Pack(direction = COLUMN,flex=1))
        box0.add(Label1)
        box0.add(self.agree)

        self.main_box.add(box0)
        self.box_list.append(box0)

        box1 = toga.Box(style=Pack(direction = COLUMN,flex=1))
        for i in range(len(data_type)):
            named = data_name[i]
            typed = data_type[i]
            ranged = data_range[i]
            label = toga.Label(named[1]+'：',style=Pack(width=100))
            if typed == 'choose':
                self.var.append(toga.Selection(style=Pack(flex=1),items=ranged.keys()))
            elif typed == 'int':
                self.var.append(toga.NumberInput(style=Pack(flex=1),step='1',default = ranged[0],min_value=ranged[0],max_value=ranged[1],on_change=self.limit))
            elif typed == 'float':
                self.var.append(toga.NumberInput(style=Pack(flex=1),step='0.001',default = ranged[0],min_value=ranged[0],max_value=ranged[1]))
            var_box = toga.Box(style=Pack(direction=ROW,flex=1,padding=10))
            var_box.add(label)
            var_box.add(self.var[-1])
            box1.add(var_box)
        self.box_list.append(box1)

        box2 = toga.Box(style=Pack(direction = COLUMN,width = width,flex=1))
        for k,v in other_buff_list.items():
            switch = toga.Switch(k,style=Pack(width = width,flex=1,
            alignment=CENTER,text_align=CENTER,font_size=15,padding=15),is_on = (v<2))
            self.other_buff.append(switch)
            box2.add(switch)
        self.box_list.append(box2)

        box3 = toga.Box(style=Pack(direction = COLUMN,flex=1))
        self.output = toga.MultilineTextInput(readonly=True,style=Pack(flex=1,width=width,text_align=CENTER,alignment=CENTER,font_size=15,padding=10))
        box3.add(self.output)
        self.box_list.append(box3)

        msg = '''欢迎来到女仆诺艾尔的尾刀期望计算器v%s版本\n
by-bilibili夜雪千沫\n\n
感谢您的使用'''%(version)
        box4 = toga.Box(style=Pack(direction = COLUMN,flex=1))
        label = toga.MultilineTextInput(readonly=True,style=Pack(flex=1,width=width,text_align=CENTER,alignment=CENTER,font_size=15,padding=10))
        label.value = msg
        box4.add(label)
        self.box_list.append(box4)


    def limit(self, num_box:toga.NumberInput):
        if num_box.value >num_box.max_value:
            num_box.value=num_box.max_value.quantize(num_box.step)
        if num_box.value <num_box.min_value:
            num_box.value=num_box.min_value.quantize(num_box.step)

    def decide(self,widget):
        self.enter.enabled = self.agree.is_on


    def last(self, widget):
        if(self.index==0):
            self.main_window.info_dialog(''," 你必须读！")
        else:
            self.main_box.remove(self.box_list[self.index])
            self.index-=1
            self.main_box.add(self.box_list[self.index])

        if self.index<(len(self.box_list)-1):
            self.enter.label = '确定'
            
            
    def next(self, widget):
        
        if self.index==(len(self.box_list)-1):
            self.exit()
            exit(0)
            # return
        if self.index == 1:
            for i in range(len(data_type)):
                typed = data_type[i]
                named = data_name[i][0]
                if typed != 'choose':
                    self.var[i].value = self.var[i].value.quantize(self.var[i].step)
                    if typed == 'float':
                        self.limit(self.var[i])
                value = self.var[i].value
                
                if typed == 'choose':
                    self.data.update({named:data_range[i][value]}) 
                elif typed == 'int':
                    self.data.update({named:int(value)})
                elif typed == 'float':
                    self.data.update({named:round(float(value),3)})

        elif self.index == 2:
            self.data["Other_buff"]=()
            for i in range(len(self.other_buff)):
                if self.other_buff[i].is_on:
                    self.data["Other_buff"] += (i,)
            self.wife = Noelle(self.data)
            self.output.value = str(self.wife)

        elif self.index == 3:
            
            msg = self.wife.inspect()
            self.main_window.info_dialog('',msg)
            


        self.main_box.remove(self.box_list[self.index])
        self.index += 1
        self.main_box.add(self.box_list[self.index])

        if self.index==(len(self.box_list)-1):
            self.enter.label = '退出'
            
        
            


def main():
    return NoelleCalculator()
