# 需要手动去https://qun.qq.com/登录，然后将cookie等信息做替换
import requests

# url = 'https://qun.qq.com/cgi-bin/qun_mgr/get_friend_list'    # 获取所有QQ好友信息
url = 'https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'       # 获取所有QQ群信息

headers = {'Host': 'qun.qq.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 '
                         'Safari/537.36',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Accept-Encoding': 'gzip, deflate, br',
           'Referer': 'https://qun.qq.com/member.html',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Content-Length': '14',
           'Origin': 'https://qun.qq.com',
           'Cookie': 'RK=E479sH/7P/; ptcz=7c5d1b78ec36d6197e41d1f4904b092a6dbbeeef4198e43cffbce531d53fcda0; '
                     'pgv_pvid=1832872632; o_cookie=513743281; ptui_loginuin=227851369; '
                     'fqm_pvqid=a1e2fddf-c196-4a76-9d02-4bee2856054a; euin=ow-lNe45oiCq; '
                     'psrf_access_token_expiresAt=1649126308; tmeLoginType=2; pgv_info=ssid=s7936518458; '
                     'p_uin=o0513264015; traceid=93a8e3cf48; uin=o0513264015; skey=@hSGd4FlNA; '
                     'pt4_token=0vNzXOLs6ySCVNlzsW221uFINZ8WwdshOJjKCRapB1w_; '
                     'p_skey=W2x1-AatXy6*8azAqu-QwrabLQmMf9emawJseevRPWQ_',
           'Connection': 'keep-alive',
           'TE': 'Trailers'
           }

data = {
    'bkn': '1790443456'  # 改成自己的bkn
}

html = requests.post(url, headers=headers, data=data)
# QQ好友信息保存
# result = html.json()["result"]

# for i in range(len(result)):
#     list_ = result[str(i)]['mems']
#     for i in list_:
#         name = i['name']
#         uin = i['uin']
#         with open('qqFriend.txt', 'a', encoding='utf-8') as f:
#             f.write(name + "," + str(uin) + '\n')

# QQ群信息保存 不能与上面的QQ好友信息同事保存
result = html.json()["join"]

for i in result:
    name = i['gc']
    uin = i['gn']
    with open('qqGroup.txt', 'a', encoding='utf-8') as f:
        f.write(str(uin) + "," + str(name) + '\n')
