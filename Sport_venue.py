# 臺北市政府體育局場地租借相關資訊
import requests
import json    

url = "https://sports.tms.gov.tw/opendata/sports_tms.json"
response = requests.get(url)
response_text = json.loads(response.text)
search = input("請輸入台北行政區:")
n = 0
with open("Sport_venue.txt","a") as txt:
    for i in response_text:
        if search == i["Area"]:
            print(i["Area"],i["Name"],i["Address"],i["OpenTime"],"~",i["CloseTime"])
            txt.write(i["Area"] + " " + i["Name"] + " " + i["Address"] + " " + i["OpenTime"] + "~" + i["CloseTime"] + "\n")
            n += 1
    if n == 0:
        print("There is no Sport venue in this district.")
        txt.write("There is no Sport venue in this district.\n")
    print(f"總共有{n}個{search}的運動中心")
    txt.write(f"總共有{n}個[{search}]的運動中心\n\n")