import json
import time

import urllib.parse

try:
    # 代理的http请求都会经过response
    def response(flow):
        if "api/sns/v10/search/notes" in flow.request.url:
            print(f"srart at {time.strftime('%X')}")
            ## 从http链接提取关键词keyword
            keywordStr = urllib.parse.parse_qs(urllib.parse.urlparse(flow.request.url).query)
            keyword = keywordStr["keyword"][0]

            content = json.loads(flow.response.text)
            for i in range(len(content["data"]["items"])):
                model_type = content["data"]["items"][i]['model_type']
                if model_type == "ads" and 'note' in content["data"]["items"][i]['ads']:
                    note = content["data"]["items"][i]['ads']['note']
                elif model_type == 'note' and 'note' in content["data"]["items"][i]:
                    note = content["data"]["items"][i]['note']
                else:
                    print("类型未知" + model_type + "，跳过")
                    continue

                print("笔记内容：")
                print(note)

            print(f"finish at {time.strftime('%X')}")

except:
    pass