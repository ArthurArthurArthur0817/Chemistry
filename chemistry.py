def get_ph_and_color(ph, indicator):
    # 根據不同指示劑及 pH 決定顏色
    color = "#FFFFFF"  # 預設顏色

    if indicator == "溴瑞香草酚藍":
        if ph <= 2.1:
            color = "#F9F900"  # 黃色
        elif 2.1 < ph <= 6.4:
            color = "#FFE66F"  # 淡黃綠色
        elif 6.4 < ph <= 6.7:
            color = "#E1E100"  # 茶綠色
        elif 6.7 < ph <= 6.9:
            color = "#73BF00"  # 茉綠色
        elif 6.9 < ph <= 7.0:
            color = "#01814A"  # 綠色
        elif 7.0 < ph <= 7.4:
            color = "#005AB5"  # 暗藍色
        elif 7.4 < ph <= 8.1:
            color = "#00FF00"  # 藍色
        else:
            color = "#0080FF"  # 天藍色
    elif indicator == "甲基紅":
        if ph < 4.2:
            color = "#FF0000"  # 紅色
        elif 4.2 <= ph <= 6.3:
            color = "#FFFF00"  # 黃色
        else:
            color = "#FFFFFF"  # 透明
    elif indicator == "溴百里酚藍":
        if ph < 6.0:
            color = "#FFFF00"  # 黃色
        elif 6.0 <= ph <= 7.6:
            color = "#00FF00"  # 綠色
        else:
            color = "#0000FF"  # 藍色
    elif indicator == "百里酚藍":
        if ph < 1.2:
            color = "#FF0000"  # 紅色
        elif 1.2 <= ph <= 2.8:
            color = "#FFFF00"  # 黃色
        elif 8.0 <= ph <= 9.6:
            color = "#00FF00"  # 綠色
        else:
            color = "#0000FF"  # 藍色
    elif indicator == "酚酞":
        color = "#FFFFFF" if ph < 7.0 else "#FF00FF"  # 酸性透明，鹼性粉紅

    return ph, color
