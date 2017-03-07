import thunder_subs

# 获取一个本地电影文件名为cid的hash值
cid = thunder_subs.cid_hash_file(
    r"E:\电影\神秘博士 第6季\Doctor.Who.2005.Christmas.Special.2011.The.Doctor.The.Widow.And.The.Wardrobe.720p.HDTV.x264-FoV.mkv")

info_list = thunder_subs.get_sub_info_list(cid, 1000)
if info_list is None:
    print("超过最大重试次数后仍然未能获得正确结果")
else:
    for i in info_list:
        print(i)
'''
本次输出结果：
    {'scid': '86AE53FC9D5A2E41E5E9CAB7C1A3794A1B7206B9', 'sname': '神秘博士2011圣诞篇The.Doctor.The.Widow.And.The.Wardrobe.ass', 'language': '简体', 'rate': '4', 'surl': 'http://subtitle.v.geilijiasu.com/86/AE/86AE53FC9D5A2E41E5E9CAB7C1A3794A1B7206B9.ass', 'svote': 545, 'roffset': 4114797192}
    {'scid': '6D314FF209BCDF94390429D5826314B7DC4CFF4C', 'sname': 'doctor_who_2005.christmas_special_2011.the_doctor_the_widow_and_the_wardrobe.720p_hdtv_x264-fov.srt', 'language': '简体&英语', 'rate': '3', 'surl': 'http://subtitle.v.geilijiasu.com/6D/31/6D314FF209BCDF94390429D5826314B7DC4CFF4C.srt', 'svote': 120, 'roffset': 4114797192}
    {'scid': '833D79CD8D9C97190DFC6DED38603D0F1AB13989', 'sname': '第六季doctor_who_2005.christmas_special_2011.the_doctor_the_widow_and_the_wardrobe.720p_hdtv_x264-fov.eng1.srt', 'language': '英语', 'rate': '3', 'surl': 'http://subtitle.v.geilijiasu.com/83/3D/833D79CD8D9C97190DFC6DED38603D0F1AB13989.srt', 'svote': 97, 'roffset': 4114797192}
    {'scid': '49D8C936BE2920D1F5BA9FCD499689FBF0AC6706', 'sname': '', 'language': '简体', 'rate': '3', 'surl': 'http://subtitle.v.geilijiasu.com/49/D8/49D8C936BE2920D1F5BA9FCD499689FBF0AC6706.srt', 'svote': 56, 'roffset': 4114797192}
    {'scid': 'C8BE7928FCB62A0E49F1702D7DADDB90D98F02B4', 'sname': 'Doctor.Who.2005.Christmas.Special.2011.The.Doctor.The.Widow.And.The.Wardrobe.720p.HDTV.x264-FoV.srt', 'language': '英语', 'rate': '1', 'surl': 'http://subtitle.v.geilijiasu.com/C8/BE/C8BE7928FCB62A0E49F1702D7DADDB90D98F02B4.srt', 'svote': 7, 'roffset': 4114797192}
    {'scid': '8F6572265A069E77EDA4EB1AED88EA616F232809', 'sname': 'DW博士之时 上半部 - 副本.CHS&EN.ass', 'language': '简体&英语', 'rate': '0', 'surl': 'http://subtitle.v.geilijiasu.com/8F/65/8F6572265A069E77EDA4EB1AED88EA616F232809.ass', 'svote': 1, 'roffset': 4114797192}
    {'scid': '8F94F0C457A2E87AB344C00239F5FB229E650481', 'sname': 'Downton Abbey / 唐顿庄园@@Downton Abbey - 02x10 - Christmas Specia1.srt', 'language': '简体&英语', 'rate': '0', 'surl': 'http://subtitle.v.geilijiasu.com/8F/94/8F94F0C457A2E87AB344C00239F5FB229E650481.srt', 'svote': 1, 'roffset': 4114797192}
    {'scid': 'E0B4E327DC1AEE5408A6ACDABE3B7998D94A15D0', 'sname': 'Doctor.Who.2005.S07E07.The.Rings.Of.Akhaten.720p.HDTV.x264-FoV.srt', 'language': '简体&英语', 'rate': '0', 'surl': 'http://subtitle.v.geilijiasu.com/E0/B4/E0B4E327DC1AEE5408A6ACDABE3B7998D94A15D0.srt', 'svote': 1, 'roffset': 4114797192}
    {'scid': 'FAFDF91FF46183E342EE8FF7D43FB99FC5511A54', 'sname': '', 'language': '简体', 'rate': '0', 'surl': 'http://subtitle.v.geilijiasu.com/FA/FD/FAFDF91FF46183E342EE8FF7D43FB99FC5511A54.ass', 'svote': 2, 'roffset': 4114797192}
    {'scid': '8DEFC8CE8396B455810B694F3204D5C95EC930B3', 'sname': 'Doctor.Who.2005.S05.Special.A.Christmas.Carol.2010.Special.BDRip.XviD-HAGGiS.srt', 'language': '英语', 'rate': '0', 'surl': 'http://subtitle.v.geilijiasu.com/8D/EF/8DEFC8CE8396B455810B694F3204D5C95EC930B3.srt', 'svote': 4, 'roffset': 4114797192}

格式化其中一个结果如下：
    {
        'scid': '86AE53FC9D5A2E41E5E9CAB7C1A3794A1B7206B9',
        'sname': '神秘博士2011圣诞篇The.Doctor.The.Widow.And.The.Wardrobe.ass',
        'language': '简体',
        'rate': '4',
        'surl': 'http://subtitle.v.geilijiasu.com/86/AE/86AE53FC9D5A2E41E5E9CAB7C1A3794A1B7206B9.ass',
        'svote': 545,
        'roffset': 4114797192
    }

每项中需要注意的数据有：
    scid: 猜测为字幕文件的scid
    sname: 字幕文件的原始文件名
    language: 字幕语言
    surl: 字幕下载地址
'''
