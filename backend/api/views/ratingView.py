from api.models import Hostel, UserRating
from rest_framework.response import Response
from rest_framework import generics, status
from api.serializers import HostelRatingSerializer, UserRatingSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404


class HostelRating(generics.RetrieveUpdateAPIView):
    queryset=Hostel.objects.all()
    serializer_class=HostelRatingSerializer


class UserRatingAPIView(generics.ListCreateAPIView):
    queryset=UserRating.objects.all()
    serializer_class = UserRatingSerializer
    
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        hostel_id = request.data.get('hostel_id')
        
        if user_id is not None and hostel_id is not None:
            existing_rating = self.queryset.filter(user_id=user_id, hostel_id=hostel_id).first()
            if existing_rating:
                serializer = self.get_serializer(existing_rating)
                return Response(serializer.data)
        
        return super().create(request, *args, **kwargs)


class UserNewRating(generics.RetrieveUpdateAPIView):
    queryset=UserRating.objects.all()
    serializer_class=UserRatingSerializer

  