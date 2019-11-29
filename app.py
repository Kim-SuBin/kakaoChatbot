from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods =["GET"])
def main():
    return "Hi! If you wanna get response about Skill server, Go to /skill"


@app.route("/test", methods =["GET"])
def test():
    data = jsonify(
        version = 1.0,
        value_list=[
            "abc",
            "def"
        ]
    )
    return data

@app.route("/skill", methods =["POST"])
def skill():
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "카드의 제목",
                        "description": "상세 설명",
                        "thumbnail": {
                            "imageUrl":
                                "https://cf.festa.io/img/2019-11-14/791369de-e762-4cc1-a341-68ce8c4a467f.png"
                        },
                        "buttons": [
                            {
                                "label": "첫번째 버튼",
                                "action": "message",
                                "messageText": "첫번쨰 버튼을 눌렀습니다."
                            }
                        ]
                    }
                    # "simpleImage":{
                    #     "imageUrl":
                    #         "https://cf.festa.io/img/2019-11-14/791369de-e762-4cc1-a341-68ce8c4a467f.png",
                    #     "altText": "Python 라이브러리 Scrapy를 이용한 Crawling 배워보기"
                    # }
                    # "simpleText": {
                    #     "text": "간단한 텍스트 요소입니다."
                    # }
                }
            ]
        }
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
