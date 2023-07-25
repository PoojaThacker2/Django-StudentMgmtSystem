from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render

# class SchoolSignUp(APIView):
#     def post(self, request):
#         serializer = SchoolSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentBulkCreate(APIView):
#     def post(self, request, grade):
#         students = []
#         for data in request.data:
#             student_data = {'name': data.get('name', ''), 'username': data['username'], 'password': data['password'], 'grade': grade}
#             student_serializer = StudentSerializer(data=student_data)
#             if student_serializer.is_valid():
#                 student_serializer.save()
#                 students.append(student_serializer.data)
#             else:
#                 return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(students, status=status.HTTP_201_CREATED)

# class StudentFilter(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, grade):
#         students = Student.objects.filter(grade=grade)
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class SchoolSignUp(TemplateView):
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin_code')
        password = request.POST.get('password')
        if name and email and city and pin_code and password:
            school = School.objects.create(name=name, email=email, city=city, pin_code=pin_code, password=password)
            return redirect('school_detail', pk=school.pk)
        return self.render_to_response(self.get_context_data())

class SchoolDetail(TemplateView):
    template_name = 'school_detail.html'

    def get_context_data(self, **kwargs):
        school = get_object_or_404(School, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['school'] = school
        return context

class StudentBulkCreate(TemplateView):
    template_name = 'bulk_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schools'] = School.objects.all()
        context['grades'] = list(range(1, 13))
        context['selected_grade'] = int(self.request.POST.get('grade', 1))  # Default to grade 1
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        school_id = data.get('school_id')
        grade = int(data.get('grade'))
        student_data = []
        for i in range(1, 13):
            key_name = f'students_grade_{i}'
            students_str = data.get(key_name, '')
            students_list = students_str.split(',')

            for student in students_list:
                if student.strip():
                    student_data.append({'name': student.strip(), 'username': f'{i}_{student.strip()}', 'grade': i})

        school = get_object_or_404(School, id=school_id)
        created_students = []
        for student in student_data:
            name = student['name']
            username = student['username']
            grade = student['grade']
            password = ''  # For simplicity, we are not using the password in this example
            student_obj = Student.objects.create(name=name, username=username, grade=grade, password=password)
            school.students.add(student_obj)
            created_students.append(student_obj)

        return redirect('bulk_create')

class StudentFilter(TemplateView):
    template_name = 'filter_students.html'

    def get_context_data(self, **kwargs):
        schools = School.objects.all()
        grades = list(range(1, 13))
        context = super().get_context_data(**kwargs)
        context['schools'] = schools
        context['grades'] = grades
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        school_id = data.get('school_id')
        grade = int(data.get('grade'))

        school = get_object_or_404(School, id=school_id)
        students = school.students.filter(grade=grade)
        return render(request, 'filtered_students.html', {'students': students})