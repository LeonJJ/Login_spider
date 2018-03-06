#豆瓣网的模拟登陆
# 主要运用requests分析网页，re获取所需信息，session与网页会话保持登陆状态
import requests,time,re

class Login_simulation():
    def __init__(self):
        self.headers = {"Referer": "http://www.mzitu.com/115882/2",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400"}
    def simulation(self):
        '''网页登陆方法 手动输入验证码'''
        response = requests.get("https://accounts.douban.com/login",headers = self.headers).text
        code_pic = re.findall(r'.*?<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>',response)
        if len(code_pic)>0:
            print("等待验证码输入...")
            down_pic = requests.get(code_pic[0]).content
            save_path = "D:/qqwwee"
            pic_name = code_pic[0][-18:-12]
            save_pic = save_path+pic_name
            with open(save_pic+".png","wb") as f:
                f.write(down_pic)
            x = input("输入验证码：")
            data1 = {
                "source":"None",
                "redir":"https: // www.douban.com /",
                "form_email":"weisuen007@163.com",
                "form_password":"weijc7789",
                "captcha - solution":x,
                "captcha - id":"F79ddvaAjEpd0Bb0sd7aiopT:en",
                "login":"登录"
                }
            self.sesson(data1)
        else:
            print("登陆中...")
            data2={
                "source": "None",
                "redir": "https: // www.douban.com /",
                "form_email": "weisuen007@163.com",
                "form_password": "weijc7789",
                "captcha - solution": "prose",
                "captcha - id": "F79ddvaAjEpd0Bb0sd7aiopT:en",
                "login": "登录"
            }
            self.sesson(data2)

    def sesson(self,data):
        '''爬虫与网页进行会话 以进一步获取信息'''
        session = requests.Session()
        session.post("https://accounts.douban.com/login", data,headers=self.headers)
        time.sleep(10)
        resp = session.get("https://www.douban.com/").text
        print(resp)

if __name__ == "__main__":
    LS = Login_simulation()
    LS.simulation()
