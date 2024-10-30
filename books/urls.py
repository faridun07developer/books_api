from django.urls import path
from .views import AuthorDetail, AuthorListAPI, BookListAPI, BookDetail
# from .views import ( BookListAPI, BookDetailAPI, BookUpdateAPI,
#                     BookCreateAPI, BookDeleteAPI,
#                      BookRetrieveUpdateAPI, BookDeleteRetrieveAPI)
# from .views import BookListCreateAPI, BookDetailUpdateDeleteAPI, AuthorListCreateAPI, AuthorDetailUpdateDeleteAPI


urlpatterns = [
    path('author_list/', AuthorListAPI.as_view()),
    path('author_detail/<int:pk>', AuthorDetail.as_view()),
    path('book_list/', BookListAPI.as_view()),
    path('book_detail/<int:pk>', BookDetail.as_view()),

    # path('list-create/', BookListCreateAPI.as_view()),
    # path('<int:pk>/delete-edit-detail', BookDetailUpdateDeleteAPI.as_view()),
    # path('author/list-create/', AuthorListCreateAPI.as_view()),
    # path('author/<int:pk>/delete-edit-detail', AuthorDetailUpdateDeleteAPI.as_view()),

    # path('detail-update/<int:pk>', BookRetrieveUpdateAPI.as_view()),
    # path('<int:pk>/delete-retrieve', BookDeleteRetrieveAPI.as_view()),

    # path("list/", BookListAPI.as_view()),
    # path("detail/<int:pk>/", BookDetailAPI.as_view()),
    # path('edit/<int:pk>/', BookUpdateAPI.as_view()),
    # path("create/", BookCreateAPI.as_view()),
    # path('delete/<int:pk>/', BookDeleteAPI.as_view())
]

