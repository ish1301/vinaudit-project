from rest_framework.serializers import (
    CharField,
    IntegerField,
    ModelSerializer,
    Serializer,
)
from vehicles.models import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class VehicleSearchSerializer(Serializer):
    year = IntegerField()
    make = CharField()
    model = CharField()
    mileage = CharField(required=False)


class VehicleSnippitSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ["name", "price", "mileage", "location"]


class VehicleReportSerializer(Serializer):
    market_value = CharField()
    results = VehicleSnippitSerializer(many=True)
