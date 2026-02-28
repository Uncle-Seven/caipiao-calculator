import urllib.request
import os

# 官方 txt 数据源地址
url = "https://data.17500.cn/ssq_asc.txt"

try:
    # 伪装成浏览器去访问，防止被拦截
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    
    # 读取返回的 txt 内容并解码
    txt_data = response.read().decode('utf-8')
    
    # 🌟 核心：把 txt 包装成合法的 JS 代码
    js_content = f"window.SSQ_ONLINE_DATA = `{txt_data}`;"
    
    # 写入到同目录下的 ssq_data.js 文件中
    with open('ssq_data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print("✅ 数据抓取并转换成功！")
    
except Exception as e:
    print(f"❌ 抓取失败: {e}")
