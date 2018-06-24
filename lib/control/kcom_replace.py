# coding=utf-8

position_replace = {
    '腹部': '腹', '肚子': '腹',
    '胸部': '胸', '胸口': '胸',
    '肩胛骨': '背', '背部': '背',
    '臉部': '臉', '臉頰': '臉', '鼻子': '臉', '耳朵': '臉', '唇': '臉', '眼': '臉', '嘴唇': '臉', '額頭': '臉',
    '脖子': '頸', '頸部': '頸', '後頸': '頸',
    '嘴巴': '嘴', '牙齦': '嘴', '口腔': '嘴', '唇': '嘴',
}

sym_replace = {
    '疼痛': '痛', '疼': '痛', '痠痛': '痛', '脹痛': '痛', '腫痛': '痛', '絞痛': '痛', '悶痛': '痛',
    '嘔吐': '吐', '想吐': '吐',
    '心跳快': '心悸',
    '麻木': '麻',
    '發冷': '畏寒',
    '疹子': '紅疹',
}

f_replace = {
    '左邊': '',
    '右邊': '',
    '左': '',
    '右': '',
    '左方': '',
    '右方': '',
    '雙': '',
}


def replace_w(string, replace_dict):
    fin = 0

    while fin == 0:
        match = list()

        for d in replace_dict:
            if d in string:
                match.append(d)

        if len(match) == 0:
            fin = 1
        else:
            max_seg = ''
            for m in match:
                if len(m) > len(max_seg):
                    max_seg = m

            string = string.replace(max_seg, replace_dict[max_seg])
    return string

# 將字串根據輸入的dictionary來取代同義字


def kcom_replace(p):

    p = replace_w(p, position_replace)
    p = replace_w(p, f_replace)
    p = replace_w(p, sym_replace)
    return p
