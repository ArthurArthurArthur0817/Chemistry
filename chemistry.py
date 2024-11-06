def get_ph_and_color(substance, indicator):
    # 根據物質決定pH值
    if substance == "HCl":
        ph = 2.0
    elif substance == "NaOH":
        ph = 12.0
    else:
        ph = 7.0

    # 根據指示劑決定顏色
    if indicator == "bromothymol_blue":
        color = "#FFFF00" if ph < 6.0 else "#0000FF" if ph > 7.6 else "#00FF00"  # 黃-藍-綠
    elif indicator == "phenolphthalein":
        color = "#FFFFFF" if ph < 7.0 else "#FF00FF"  # 酸性透明，鹼性粉紅
    else:
        color = "#FFFFFF"

    return ph, color
