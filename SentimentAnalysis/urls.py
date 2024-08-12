from django.contrib import admin
from django.urls import path
from SentimentAnalysisAPI.views import sentiment_analysis

urlpatterns = [
    path("admin/", admin.site.urls),
    path('analyze/', sentiment_analysis, name='sentiment_analysis'),
]
