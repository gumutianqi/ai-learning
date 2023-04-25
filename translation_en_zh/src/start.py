# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask import Flask
from transformers import pipeline

model_en_zh = "/model/opus-mt-en-zh"
en2zh = pipeline("translation", model=model_en_zh)

# build a Flask HTTP-Server
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# 英文翻译成中文
@app.route("/transfer_zh", methods=['POST'])
def transfer_zh():
    doc = request.get_json()["text"]
    new_doc = en2zh(doc)

    return_result = {
        "sourceText": doc,
        "translated": new_doc[0]["translation_text"]
    }
    return jsonify(return_result)


if __name__ == '__main__':
    app.run(debug=True)
