from django.urls import path

from .views import PostsList, PostDetail, PostSearch, PostAdd, PostEdit, PostDelete

urlpatterns = [
    path('', PostsList.as_view(), name='home'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view(), name='post_search'),
    path('add', PostAdd.as_view(), name='post_add'),
    path('<int:pk>/edit', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
]
