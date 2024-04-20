import json
from collections import Counter
import os


# 環境変数からファイルパスを取得
file_path = os.getenv("file_path")


def detect_duplicate_channel_ids(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    #Channel ID重複チェック
    
    channel_ids = set()
    duplicate_channel_ids = set()
    
    # channelRules配下のchannelIdを取得
    channel_rules = data.get("channelRules", [])
    for rule in channel_rules:
        channel_id = rule.get("channelId")
        if channel_id in channel_ids:
            duplicate_channel_ids.add(channel_id)
        else:
            channel_ids.add(channel_id)
    
    if duplicate_channel_ids:
        print("重複しているchannelIdがあります:", duplicate_channel_ids)
        raise ValueError("重複しているchannelIdがあります")
    else:
        print("重複しているchannelIdはありません")

detect_duplicate_channel_ids(file_path)



def detect_duplicate_ids(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    ids = set()
    duplicate_ids = set()

    #channelRules配下のidを取得
    channel_rules = data.get("channelRules", [])
    for rule in channel_rules:
        id = rule.get("id")
        if id in ids:
          duplicate_ids.add(id)
        else:
          ids.add(id)

    if duplicate_ids:
        print("重複しているidがあります:", duplicate_ids)
        raise ValueError("重複しているidがあります")
    else:
        print("重複しているidはありません")

detect_duplicate_ids(file_path)
