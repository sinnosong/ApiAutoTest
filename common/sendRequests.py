import os,sys,json
import configparser
from config import setting

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class SendRequests():
    """发送请求数据"""
    def sendRequests(self,session,apiData):
            # 读取config中的测试host，port
            con = configparser.ConfigParser()
            con.read(setting.TEST_CONFIG, encoding="utf-8")
            test_host = con.get("test_host","host")
            test_port = con.get("test_host","port")
            # 读取表格内容获取响应参数
            try:
                method = apiData["method"]
                url = "http://" + test_host +":"+ test_port + apiData["url"]
                if  apiData["params"] == "":
                    par = None
                else:
                    par =eval(apiData["params"])
                if apiData["headers"] == "":
                    h = None
                else:
                    h = eval(apiData["headers"])
                if apiData["body"] == "":
                    body_data = None
                else:
                    body_data = eval(apiData["body"])
                type = apiData["type"]
                v = False
                if type == "data":
                    body = body_data
                elif type == "json":
                    body = json.dumps(body_data)
                else:
                    body = body_data

                re = session.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
                return re
            except Exception as e:
                print(e)