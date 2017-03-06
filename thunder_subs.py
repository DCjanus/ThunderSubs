import os
import json
import hashlib
import requests


def cid_hash_file(path: str):
    '''
    计算文件名为cid的hash值，算法来源：https://github.com/iambus/xunlei-lixian
    :param path: 需要计算的本地文件路径
    :return: 所给路径对应文件的cid值
    '''
    h = hashlib.sha1()
    size = os.path.getsize(path)
    with open(path, 'rb') as stream:
        if size < 0xF000:
            h.update(stream.read())
        else:
            h.update(stream.read(0x5000))
            stream.seek(size // 3)
            h.update(stream.read(0x5000))
            stream.seek(size - 0x5000)
            h.update(stream.read(0x5000))
    return h.hexdigest().upper()


def get_sub_info_list(cid: str, max_retry_times: int = 0):
    '''
    获取迅雷字幕库中字幕信息列表
    :param cid: 本地电影文件的cid值
    :param max_retry_times: 最大重试次数，非正数时会无限次重试直到获得正确结果
    :return: 字幕信息列表，超过最大重试次数还未获得正确结果时会返回None。
    '''
    url = "http://sub.xmp.sandai.net:8000/subxl/{cid}.json".format(cid=cid)
    result = None
    if max_retry_times <= 0:
        while True:
            response = requests.get(url)
            if response.status_code == 200:
                result = json.loads(response.text)["sublist"]
                break
    else:
        for i in range(max_retry_times):
            response = requests.get(url)
            if response.status_code == 200:
                result_dict = json.loads(response.text)
                result = result_dict["sublist"]
                break
    return [i for i in result if i]
