import include.buff as buff
other_buff_list = {"双岩":0,"岩伤杯":1,"钟离":2}

def get_buff(others = (0,1)):
    b = buff.Buff()
    for o_buff in others:
        b_add = buff.Buff()
        if o_buff == 0:
            b_add.set(buff.on,"Dmg_Inc",0.15)
            b_add.set(buff.off,"Dmg_Inc",0.15)
            b_add.set(buff.on,"Rock_RES_Dec",0.2)
            b_add.set(buff.off,"Rock_RES_Dec",0.2)
        elif o_buff == 1:
            b_add.set(buff.on,"Rock_Dmg_Inc",0.466)
            b_add.set(buff.off,"Rock_Dmg_Inc",0.466)
        elif o_buff == 2:
            b_add.set(buff.on,"Rock_RES_Dec",0.2)
            b_add.set(buff.off,"Rock_RES_Dec",0.2)
            b_add.set(buff.on,"Phy_RES_Dec",0.2)
            b_add.set(buff.off,"Phy_RES_Dec",0.2)
        b += b_add
    return b

if __name__=='__main__':
    print(get_buff())
