from rest_framework import serializers
from .models import Destinations, Guide

class DestinationSerializer(serializers.ModelSerializer):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Destinations
        fields = '__all__'

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'
