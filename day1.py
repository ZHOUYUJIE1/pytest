import pytest
import requests
import jsonpath


@pytest.mark.skip
def test_abc():
    assert 1==1



def test_baidu():
    resp = requests.request(  #发送请求获得响应
        method='get',  #HTTP请求方法
        url='https://www.baidu.com',  #接口地址
        data={"a":1,"b":2} ,  #接口参数
        #json={},#接口参数
        #files={},#接口参数
        #headers={}#接口参数
    )
    print(resp.status_code) #整数
    print(resp.headers)  #字典
    print(resp.text)  #字符串
    print(resp.json)  #json

    assert resp.status_code == 200
    assert 'baidu' in resp.text



def test_api_form(): #表单主要用在web项目中
    data = {         #当data参数是字典时，会自动识别为表单，并自动为其添加请求头
        "username":"sanmu",
        "password":"123456"
    }

    resp = requests.request(
        method = 'post',
        url='http://api.fbi.com:9225/rest-v1/login/with_form',
        data = data
        ''' 
        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        '''
    )

    assert resp.status_code == 200



def test_api_json(): #JSON主要用在各类项目中
    data = {"username":"sanmu","password":"123456"}
    resp = requests.request(
        method = 'post',
        url='http://api.fbi.com:9225/rest-v1/login/with_json',
        data = data  #json方式传参
    )

    assert resp.status_code == 200



def test_file_upload():
    path = r"C:\Users\jie\Desktop\test.txt" #字符串
    f = open(path,'r')  #文件对象

    resp = requests.request(
        method = 'post',
        url = 'http://api.fbi.com:9225/rest-v1/upload/one_file',
        files = {"file": f}
    )

    assert resp.status_code == 200



def test_token():
    data = {  # 当data参数是字典时，会自动识别为表单，并自动为其添加请求头
        "username": "sanmu",
        "password": "123456"
    }

    resp = requests.request(
        method='post',
        url='http://api.fbi.com:9225/rest-v1/login/with_form',
        data=data
    )

    print(resp.text)#返回token

    token = jsonpath.jsonpath(resp.json(), expr:'$token') [0]

    resp1 = requests.request(
        method='get',
        url='http://api.fbi.com:9225/rest-v1/auth/token_with_header',
        header = {"token":token}
    )

    assert resp1.status_code == 200




#日志、报告：yaml、allure

