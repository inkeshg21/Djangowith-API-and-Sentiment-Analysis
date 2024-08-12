from rest_framework.decorators import api_view
from transformers import pipeline
from django.http import JsonResponse
from setfit import SetFitModel


@api_view(['POST'])
def sentiment_analysis(request):
    text = request.data.get('text')
    # classifier = pipeline('sentiment-analysis', model='StatsGary/setfit-ft-sentinent-eval')
    classifier = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    preds = classifier(text)
    json_data = preds[0]['label']
    response_data = {'sentiment': json_data}
    return JsonResponse(data=response_data, safe=False)
