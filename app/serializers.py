from rest_framework import serializers
from .models import *

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = activity
        fields = ['start_time', 'end_time']

class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = member
        fields = ['id', 'real_name', 'tz', 'activity_periods']
