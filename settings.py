# 検査陽性者の状況
MAIN_SUMMARY_URL = "http://www.pref.saitama.lg.jp/a0701/shingatacoronavirus.html"

# 陽性患者数
JOKYO_URL = "https://opendata.pref.saitama.lg.jp/data/dataset/covid19-jokyo"
JOKYO_TITLE = "^埼玉県内の新型コロナウイルス感染症の発生状況"

# 検査数
KENSA_URL = "https://opendata.pref.saitama.lg.jp/data/dataset/covid19-kensa"
KENSA_TITLE = "^埼玉県が実施した新型コロナウイルス疑い例検査数"

# directory
DOWNLOAD_DIR = "download"
DATA_DIR = "data"

#request headers
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
REQUEST_HEADERS = {"User-Agent": USER_AGENT}

# 最新のお知らせ
NEWS_URL = "https://www.pref.saitama.lg.jp/news/index.html"
NEWS_LIST = {
    "newsItems": [
    {
      "date": "2020/05/19",
      "url": "https://www.pref.saitama.lg.jp/a0704/netsuchusyo/netsu-3sonae.html",
      "text": "新型コロナウイルス感染症流行期における「熱中症予防3つの備え」"
    },
    {
      "date": "2020/03/24",
      "url": "https://www.pref.saitama.lg.jp/a0701/covid19/line_saitama-official-account.html",
      "text": "LINE公式アカウント「埼玉県-新型コロナ対策パーソナルサポート-」を開設"
    }
  ]
}
