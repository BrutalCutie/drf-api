from rest_framework.pagination import PageNumberPagination


class LessonPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "limit"
    max_page_size = 20


class CoursePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "limit"
    max_page_size = 20
