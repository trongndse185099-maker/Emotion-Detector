import json
import requests

def emotion_detector(text_to_analyze):
    """
    Sends input text to Watson NLP API, parses the response,
    and returns a structured dictionary containing all emotion scores
    along with the dominant emotion.
    """
    # URL of the Watson NLP Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers specifying the model ID required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # JSON payload structure enclosing the text to analyze
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending the POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extracting the emotion predictions block
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Isolate individual score attributes
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Determine the dominant emotion with the highest score value
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Formatting the final required output structure
    output_result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output_result