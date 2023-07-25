from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer

class SchoolSignUp(APIView):
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentBulkCreate(APIView):
    def post(self, request, grade):
        students = []
        for data in request.data:
            student_data = {'name': data.get('name', ''), 'username': data['username'], 'password': data['password'], 'grade': grade}
            student_serializer = StudentSerializer(data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                students.append(student_serializer.data)
            else:
                return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(students, status=status.HTTP_201_CREATED)

class StudentFilter(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, grade):
        students = Student.objects.filter(grade=grade)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
