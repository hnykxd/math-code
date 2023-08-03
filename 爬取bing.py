import requests
from bs4 import BeautifulSoup

def scrape_bing():
    try:
        # 要爬取的目标URL
        url = "https://cn.bing.com"

        # 发起GET请求获取网页内容
        response = requests.get(url)

        # 检查响应是否成功
        if response.status_code == 200:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # 在这里可以根据网页的结构提取所需的信息
            # 例如，提取搜索框的提示文字
            search_hint = soup.find('span', {'class': 'b_searchbox_hint'})
            if search_hint:
                print("搜索框提示文字:", search_hint.text)

            # 也可以提取其他内容，具体根据实际情况而定

        else:
            print(f"请求失败，状态码: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")

if __name__ == "__main__":
    # 调用爬虫函数
    scrape_bing()
