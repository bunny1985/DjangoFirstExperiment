import sys
from typing import Dict, List
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route

from .models import News
from .serializers import GroupSerializer, NewsSerializer, UserSerializer


def hello(request):
    """just hello templte"""
    return render(request, "main/home.html", {'message': 'Hello You'})


def manage(request):
    pass

"""
Pusblishes selected news
"""
@api_view(['POST'])
def publish_news(request, pk=None):
    """Publishes selected news with current timestamp"""
    news = News.objects.get(pk=pk)
    news.publishedAt = timezone.now()
    news.isPublished = True
    news.save()
    return HttpResponse(status=200)


@api_view(['POST'])
def unpublish_news(request, pk=None):
    """Unpublishes selected news """
    news = News.objects.get(pk=pk)
    news.publishedAt = None
    news.isPublished = False
    news.save()
    return HttpResponse(status=200)


@api_view(['GET'])
def latestNews(request, pk=None):
    """Latest 3 news in descending publishing order """
    news: List[News] = News.objects.filter(
        isPublished=True).order_by('-publishedAt')[0:3]
    serializer = NewsSerializer(news, many=True)
    return JsonResponse(serializer.data, safe=False)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def publishNews(self, request, pk=None):
        news = News.objects.get(pk=pk)
        news.publishedAt = timezone.now()
        news.isPublished = True
        news.save()
        return HttpResponse(status=200)

    def unpublishNews(self, request, pk=None):
        news = News.objects.get(pk=pk)
        news.publishedAt = None
        news.isPublished = False
        news.save()
        return HttpResponse(status=200)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
