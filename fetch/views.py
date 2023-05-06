from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .utils import fetch_nodes

# Create your views here.
class GetMovies(APIView):
    def get(self, request):
        fetch_info = {
            'node_type': request.GET.get('t', 'Movie'),
            'page':request.GET.get('p', 1),
        }
        print(fetch_info)
        try:
            # print('=====GETTING NODES NOW======')
            nodes = fetch_nodes(fetch_info)
            
            # print(nodes)
            data = {
                'response':{
                    'status': '200',
                    'rows': len(nodes),
                    'data': nodes,
                }
            }
        except Exception as error:
            print(error)
            data = {
                'response':{
                    'status': '403',
                }
            }
        
        return Response(data)