import random

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, make_response, jsonify, render_template
import gensim
from random import *
from .models import Hobby, Room

loaded_model = gensim.models.KeyedVectors.load("my_word2vec_model_new")

app = Flask(__name__)

app.secret_key="this is a secret key"
app.config['JSON_AS_ASCII'] = False
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:1111@localhost:3306/board" #config 파일 필요없음
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1111@172.20.22.75:3306/board" #
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# 모델 로드 확인
@app.route("/main", methods=['GET', 'POST'])
def main() :
    result = loaded_model.most_similar("뜨개질")
    return result[0][0]


# db 연동 확인
@app.route("/db", methods=['GET','POST'])
def home() :
    allHobbyArray = []
    for row in Hobby.query.all():
        allHobbyArray.append(row.hobby_name)
    test = Hobby.query.first()
    hobby1 = allHobbyArray[random.randrange(0, len(allHobbyArray))]
    return 'Hello {0}'.format(hobby1)

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    allHobbyArray = []
    for row in Hobby.query.all() :
        allHobbyArray.append(row.hobby_name)

    req = request.get_json(force=True)
    intent_name = req['queryResult']['intent']['displayName']

    action = req['queryResult']['action']  # 1 dialogflow에서 설정한 action값

    if intent_name == 'Default Welcome Intent':
        test_session_name = req['session']
        return {'fulfillmentText': '안녕하세요!',
                "source": 'webhook'}

    # 취미를 제시하고 그와 비슷한 취미를 추천해달라고 했을 경우
    elif intent_name == 'recommend_similar':
        get_hobby_name = req['queryResult']['parameters']['hobby']  # 2 해당 action 안에 파라미터로 지정한 값
        if loaded_model.most_similar(get_hobby_name) :
            result = loaded_model.most_similar(get_hobby_name)
            hobby1 = result[0][0]
            hobby2 = result[1][0]
            return {
                'fulfillmentText': hobby1 + ", " + hobby2 + " 같은 취미는 어떠세요?",
                'source': 'webhook'
            }

        else :
            return {'fulfillmentText': "아직 잘 모르는 취미예요."}

    # 다른 취미를 추천해달라고 했을 경우
    elif intent_name == 'recommend_similar - custom':
        #pprint.pprint(req)
        get_hobby_name = req['queryResult']['outputContexts'][0]['parameters']['hobby']
        # 2 해당 action 안에 파라미터로 지정한 값

        if loaded_model.most_similar(get_hobby_name):
            result = loaded_model.most_similar(get_hobby_name)
            hobby3 = result[2][0]
            hobby4 = result[3][0]

        return {'fulfillmentText': "마음에 안 드셨나요? 그렇다면 " + hobby3 + ", " + hobby4 + "같은 취미는 어떠세요?"}

    # 이건 전체 취미 테이블에서 가져올 것
    # 랜덤한 취미를 추천해 줌
    elif intent_name == 'recommend':
        # https://planbs.tistory.com/entry/query-%EA%B0%9D%EC%B2%B4%EA%B0%80-%EC%8B%A4%EC%A0%9C%EB%A1%9C-%EC%BF%BC%EB%A6%AC%EB%A5%BC-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EC%8B%9C%EA%B8%B0
        # 여기 참고
        randomInt = randint(0, len(allHobbyArray)-1)
        hobby1 = allHobbyArray[randomInt]
        return {
            'fulfillmentText': hobby1 + " 취미를 추천드려요.",
            'source': 'webhook'
        }

# 사용자가 지정한 태그를 단 모임방을 추천해주는 기능
    elif intent_name == 'recommend_room':
        parameter = req['queryResult']['parameters']['room']
        result_roomid = set()
        result_string = ""
        webhook_keyword = parameter# webhook에서 오는 'room' parameter 값들 ["조용히"] , ["조용히", "이야기해요"] list형식

        if len(webhook_keyword) == 1:
            for row in Room.query.all() :
                db_keyword = row.room_keyword.split() #['#조용히', '#만들어요']
                for d in db_keyword :
                    d.replace("#", "")
                    for w in webhook_keyword :
                        if w in d :
                            result_roomid.add(row.room_id)

        else :
            for row in Room.query.all() :
                db_keyword = row.room_keyword.split()
                db_keyword[0].replace("#", "")
                db_keyword[1].replace("#", "")

                if webhook_keyword[0] in db_keyword[0] and webhook_keyword[1] in db_keyword[1] :
                    result_roomid.add(row.room_id)


        result_roomid_list = list(result_roomid)

        for r in result_roomid_list :
            s = str(r)
            result_string += s + ","

        if result_string != "" :
            return {
                'fulfillmentText': "이런 방을 추천드려요. 메시지를 클릭해 보세요!@" + result_string,
                'source': 'webhook'
            }

        else :
            return {
                'fulfillmentText': "방이 아직 존재하지 않습니다. 메세지를 클릭해서 새 방을 만들어 보세요!@",
                'source': 'webhook'
            }

    else:
        return {'어떤 질문인지 모르겠어요'}