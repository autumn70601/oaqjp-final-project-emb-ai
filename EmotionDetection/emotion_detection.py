import requests, json



def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = {}

    #if not text_to_analyze:
    #    emotions['dominant_emotion'] = None
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        emotions['dominant_emotion'] = None

    return emotions