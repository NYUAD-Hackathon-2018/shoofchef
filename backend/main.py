from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import json
from flask_jsonpify import jsonify
import scraping

app = Flask(__name__)
api = Api(app)


@app.route('/images', methods=['GET', 'POST'])
def api_image_description():
    if request.method == 'GET':
        plate = request.args.get('plate')
        image_url = scraping.imageSearch(plate)
        return str(image_url)
    elif request.method == 'POST':
        file = request.files.get('imagefile')
        print (file)
        file.save('image.png')
        response = scraping.ocr('image.png')
        i = 0
        finalResponse = []
        for result in response['responses'][0]['textAnnotations']:
            if i != 0:
                isDish = scraping.word_analysis(result['description'])
                if isDish:
                    finalResponse.append(result)
            i = i + 1
        print(finalResponse)
        print(response['responses'][0]['fullTextAnnotation']['pages'][0]['width'])
        print(response['responses'][0]['fullTextAnnotation']['pages'][0]['height'])

        return json.dumps({'response': finalResponse,
                    'width': response['responses'][0]['fullTextAnnotation']['pages'][0]['width'],
                    'height': response['responses'][0]['fullTextAnnotation']['pages'][0]['height']
                })


if __name__ == '__main__':
    app.debug = True
    app.run(port='5002')

