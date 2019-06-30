def authentication():
    from requests_oauthlib import OAuth1Session
    import csv

    input_file = open('auth.csv', 'r', encoding="utf-8")
    reader = csv.DictReader(input_file)
    keys = [row for row in reader]
    input_file.close()

    return OAuth1Session(keys[0]["API_key"], keys[0]["API_secret"], keys[0]["Access_token"], keys[0]["Access_secret"])

def getListofList():
    url = "https://api.twitter.com/1.1/lists/list.json"
    return twitter.get(url)

def getTweets(lastId=0):
    url = "https://api.twitter.com/1.1/lists/statuses.json"

    if lastId == 0:
        params = {'list_id':1144937680683147267, 'count':200}
    else:
        params = {'list_id':1144937680683147267, 'count':200, 'since_id':lastId}
    return twitter.get(url, params=params)

def searchUser(keyword, page):
    url = "https://api.twitter.com/1.1/users/search.json"
    params = {"q":keyword, "page":page}
    result = twitter.get(url, params=params)
    return json.loads(result.text)

def addListMember(screen_names):
    url = "https://api.twitter.com/1.1/lists/members/create_all.json"
    params = {"list_id":1144937680683147267, 'screen_name':','.join(screen_names)}
    res = twitter.post(url,params=params)
    print(res)



def adddata(users):
    result = []
    for user in users:
        tmp = [user["screen_name"], user["followers_count"], user["friends_count"], user["statuses_count"]]
        result.append(tmp)
    return result

def makeCSV():
    friends_data = []
    for i in range(1, 50) :
        users = searchUser("けもフレ", i)
        newdata = adddata(users)
        for user in newdata:
            if user[0] in [i[0] for i in friends_data]:
                print("duplicate!")
            else:
                friends_data.append(user)
        print(i)
        time.sleep(6)
    return friends_data


if __name__ == "__main__":
    # キーワード検索してcsvファイルを作るまで
    twitter = authentication()
    import csv
    import json
    import time
    # lists = getListofList()
    # timelines = getTweets()
    #friends_data = makeCSV()

    #f_out = open("kemofure_data.csv", "w", encoding="utf-8", newline='')
    #writer = csv.writer(f_out)
    #writer.writerows(friends_data)
    #f_out.close()

    print("making csv file in succeeded!")

    # 作ってRで処理したcsvファイルからリスト作成！
    f_in = open("kemofure_wo_ghost.csv", 'r', encoding="utf-8")
    reader = csv.reader(f_in, delimiter=' ')
    friends_wo_dummy = [row[1] for row in reader]
    addListMember(friends_wo_dummy[0:100])
    addListMember(friends_wo_dummy[100:200])
    addListMember(friends_wo_dummy[200:300])
    addListMember(friends_wo_dummy[300:])

    print("終わりました")


