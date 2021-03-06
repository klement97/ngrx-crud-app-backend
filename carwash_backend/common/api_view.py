from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response


class SCAPIViewListCreate(ListCreateAPIView):
    # ToDO - Make Exceptions!
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
