import urllib.request

# 封装一个通用的抓取函数
def fetch_and_save(url, js_var_name, file_name):
    try:
        # 伪装浏览器请求
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        txt_data = response.read().decode('utf-8')
        
        # 包装成 JS 变量
        js_content = f"window.{js_var_name} = `{txt_data}`;"
        
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(js_content)
            
        print(f"✅ [{file_name}] 数据抓取并转换成功！")
    except Exception as e:
        print(f"❌ [{file_name}] 抓取失败: {e}")

# 1. 抓取双色球数据
fetch_and_save("https://data.17500.cn/ssq_asc.txt", "SSQ_ONLINE_DATA", "ssq_data.js")

# 2. 抓取大乐透数据
fetch_and_save("https://data.17500.cn/dlt_asc.txt", "DLT_ONLINE_DATA", "dlt_data.js")
