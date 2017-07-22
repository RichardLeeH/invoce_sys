# coding=utf-8
from rest_framework import viewsets, status
from rest_framework.response import Response

from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer, InvoiceCreateSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    发票记录
    """
    queryset = Invoice.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return InvoiceCreateSerializer
        return InvoiceSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        figure_file = request_data.get("figure_file")
        if figure_file:
            # 支持文件上传
            request_data["figure"] = figure_file
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
