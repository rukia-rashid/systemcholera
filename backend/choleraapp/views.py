from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import NormalUser, Street, Patient, HealthFacility, Deceased, Recovered
from .serializers import NormalUserSerializer, StreetSerializer, PatientSerializer, HealthFacilitySerializer, DeceasedSerializer, RecoveredSerializer, UserSerializer

@api_view(['POST'])
@permission_classes([IsAdminUser])
def register_normal_user(request):
    serializer = NormalUserSerializer(data=request.data)
    if serializer.is_valid():
        normal_user = serializer.save()
        return Response({
            'message': 'Normal user created successfully',
            'normal_user': NormalUserSerializer(normal_user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def normal_user_list(request):
    normal_users = NormalUser.objects.all()
    serializer = NormalUserSerializer(normal_users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_superuser': user.is_superuser,
    })
 
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def street_list_create(request):
    if request.method == 'GET':
        streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StreetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def street_detail(request, pk):
    try:
        street = Street.objects.get(pk=pk)
    except Street.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StreetSerializer(street)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StreetSerializer(street, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        street.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def patient_list_create(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if not user.is_superuser:
            normal_user_data = request.data.get('normal_user', {})
            normal_user_data['user'] = user.id
            normal_user_serializer = NormalUserSerializer(data=normal_user_data)
            if normal_user_serializer.is_valid():
                normal_user_serializer.save()
            else:
                user.delete()
                return Response(normal_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def health_facility_list_create(request):
    if request.method == 'GET':
        health_facilities = HealthFacility.objects.all()
        serializer = HealthFacilitySerializer(health_facilities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HealthFacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def health_facility_detail(request, pk):
    try:
        health_facility = HealthFacility.objects.get(pk=pk)
    except HealthFacility.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HealthFacilitySerializer(health_facility)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HealthFacilitySerializer(health_facility, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        health_facility.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def deceased_list_create(request):
    if request.method == 'GET':
        deceased = Deceased.objects.all()
        serializer = DeceasedSerializer(deceased, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeceasedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def deceased_detail(request, pk):
    try:
        deceased = Deceased.objects.get(pk=pk)
    except Deceased.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeceasedSerializer(deceased)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DeceasedSerializer(deceased, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        deceased.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def recovered_list_create(request):
    if request.method == 'GET':
        recovered = Recovered.objects.all()
        serializer = RecoveredSerializer(recovered, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecoveredSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def recovered_detail(request, pk):
    try:
        recovered = Recovered.objects.get(pk=pk)
    except Recovered.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecoveredSerializer(recovered)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RecoveredSerializer(recovered, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recovered.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_count(request):
    count = Patient.objects.count()
    return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recovered_patient_count(request):
    count = Recovered.objects.count()
    return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deceased_patient_count(request):
    count = Deceased.objects.count()
    return Response({'count': count})
