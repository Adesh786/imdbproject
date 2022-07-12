from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListAV, WatchDetailAV, WatchListGV, StreamPlatformAV, StreamPlatformDetailsAV, ReviewCreate, ReviewList, ReviewDetail,UserReview

# router = DefaultRouter()
# router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # For filtering directly from URL
    # path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),

    # For Filtering URL parameters 
    path('reviews/', UserReview.as_view(), name='user-review-detail'),

    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name='stream-details'),

    path('list2/', WatchListGV.as_view(), name='watch-list'),
]


    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details')