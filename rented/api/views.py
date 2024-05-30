from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RentedSerializer
from ..models import RentedModel
from django.shortcuts import get_object_or_404


class RentedList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        draw = int(request.GET.get('draw'))
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length'))

        search_value = request.GET.get('search[value]')
        order_column = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')

        # Column list for ordering
        column_list = ['id', 'drone', 'user', 'start_date', 'start_date_time', 'end_date', 'end_date_time']

        # Sorting
        order_column = column_list[int(order_column)]
        if order_dir == 'desc':
            order_column = '-' + order_column

        queryset = RentedModel.objects.filter(user_id=request.user)

        # Filtering
        if search_value:
            queryset = queryset.filter(drone__name__in=search_value)

        total = queryset.count()

        # Pagination
        queryset = queryset.order_by(order_column)[start:start + length]

        serializer = RentedSerializer(queryset, many=True)

        response = {
            'draw': draw,
            'recordsTotal': total,
            'recordsFiltered': total,
            'data': serializer.data,
        }

        return Response(response)


class RentedAction(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        return get_object_or_404(RentedModel, pk=pk)

    def get(self, request, pk):
        rented = self.get_object(pk)
        serializer = RentedSerializer(rented)
        return Response(serializer.data)


    def put(self, request, pk):
        rented = self.get_object(pk)
        serializer = RentedSerializer(rented, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rented = get_object_or_404(RentedModel, id=id)
        rented.delete()
        return Response({'message': 'Rezervasyon silindi'}, status=204)
