"""
    Module for detecting emotions from text
    using the Watson NLP library
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Sends a POST request to the Watson NLP Emotion Predict service
    to analyze the emotions present in the provided text.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )

    headers = {
        "grpc-metadata-mm-model-id": (
            "emotion_aggregated-workflow_lang_en_stock"
        )
    }

    myobj = { "raw_document": { "text": text_to_analyze }}

    response = requests.post(url, json=myobj, headers=headers, timeout=10)

    """
    added error handling
"""

    if response.status_code == 400:
        
        return {
            'anger' : None,
            'disgust' : None,
            'fear' : None,
            'joy' : None,
            'sadness' : None,
            'dominant_emotion' : None
        }

    # converting response into json format
    formatted_response = json.loads(response.text)

    # extracting emotions and scores
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']

    # formatting the output
    output_dict = {
        'anger' : anger_score,
        'disgust' : disgust_score,
        'fear' : fear_score,
        'joy' : joy_score,
        'sadness' : sadness_score,
    }

    # finding the dominant emotion
    dominant_emotion = max(output_dict, key=output_dict.get)

    # adding dominant emotion to the output
    output_dict['dominant_emotion'] = dominant_emotion

    return output_dict
 