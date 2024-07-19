from rest_framework import serializers
from django.contrib.auth.models import User
from .models import NormalUser, Street, Patient, HealthFacility, Deceased, Recovered

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'street_name', 'num_grown_up_females', 'num_grown_up_males', 'num_children', 'total_population', 'km_square', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NormalUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    street = serializers.PrimaryKeyRelatedField(queryset=Street.objects.all())

    class Meta:
        model = NormalUser
        fields = ['id', 'user', 'full_name', 'street', 'phone_number', 'nida_id', 'created_at', 'updated_at']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        normal_user = NormalUser.objects.create(user=user, **validated_data)
        return normal_user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'age', 'gender', 'nida_id', 'phone_number', 'address', 'condition', 'date_reported', 'time_reported', 'health_facility', 'created_at', 'updated_at']

class HealthFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = ['id', 'name', 'location', 'created_at', 'updated_at']

class DeceasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deceased
        fields = ['id', 'patient', 'date_of_death', 'time_of_death', 'created_at', 'updated_at']

class RecoveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recovered
        fields = ['id', 'patient', 'date_of_recovery', 'time_of_recovery', 'created_at', 'updated_at']
