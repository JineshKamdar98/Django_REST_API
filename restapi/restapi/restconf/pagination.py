from rest_framework import pagination

#pagination class
class CFEAPIPagination(pagination.LimitOffsetPagination): #PageNumberPagination):
    page_size=5
    max_limit=2
    defualt_limit=4
