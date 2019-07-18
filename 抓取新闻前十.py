import json
import urllib
import urllib2


first_time = 1563184232
pre_url = "http://piyao.sina.cn/api/list/group?len=1&ptime="
pre_like_url = "http://comment5.news.sina.com.cn/count/info?key=piyao_"
url = pre_url + str(first_time)

req = urllib2.Request(url)
#print(req)

res_data = urllib2.urlopen(req)

result_dic = {}
res = res_data.read()
while True:
	try:
		req = urllib2.Request(url)
		res_data = urllib2.urlopen(req)
		res = res_data.read()
	
		for key, value  in json.loads(res)["result"]["data"].items():
			title = value[0]["title"]
			ptime = value[0]["ptime"]
			article_id = value[0]["article_id"]
			like_url = pre_like_url + str(article_id)	
			req_like = urllib2.Request(like_url)
			res_like_data = urllib2.urlopen(req_like)
			res_like = res_like_data.read()
			like = json.loads(res_like)["result"]["data"]["sum"]
			result_dic[title]=int(like)
		url = pre_url + str(ptime)
	except:
		break

result_list = sorted(result_dic.items(), key = lambda item:item[1],reverse = True)

for i in range(10):
	print "Title :"+ result_list[i][0]+ " Like :"+str(result_list[i][1])
