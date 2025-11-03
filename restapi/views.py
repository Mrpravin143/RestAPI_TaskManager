from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi.models import Employee,Course,Student
from restapi.Serelizers.model_serializer import StudentSerializers
from restapi.Serelizers.normal_serializer import StudentSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    data = [
    {
        "id":101,
        "Status":"200 Ok",
        "message":"djnago rest framework"
    },
    {
        "id":102,
        "Status":"200 Ok",
        "message":"djnago rest framework"
    },
    {
        "id":103,
        "Status":"200 Ok",
        "message":"djnago rest framework"
    },
    
    ]
    return Response(data)


@api_view(['POST'])
def create_records(request):
    
    if request.method == "POST":
        data = request.data
        Employee.objects.create(**data) 
        return Response({
            "id":1001,
            "Status":True,
            "data":"record created",
            "api": data
        })


@api_view(['GET'])
def fetchdata(request):
    employee = [
        {   "id":employee.id, 
            "name": employee.name,
            "email": employee.email,
            "work_ex": employee.work_ex,
            "dob": employee.dob
        }
        for employee in Employee.objects.all()

    ]
    return Response({
        'Status':True,
        "Data": employee
    })


@api_view(['DELETE'])
def deleteRecords(request,id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response({
            "Message":"Record Deleted"
        })
    except Exception as e:
        return Response(
            {"Message":"Invalid ID"}
        )
    

@api_view(['POST','PUT'])
def update(request,id):
    try:
        employee = Employee.objects.get(id=id)
        data = request.data
        employee.data = update_or_create(employee)
        employee.save()
        return Response({
            "Message":"Record Updated",
            "data": data
        })
    except Exception as e:
        return Response({
            "Message":"invalid ID"
        })

    


# Practice Purpose
@api_view(['POST'])
def Pcreate(request):
    if request.method == "POST":
        data = request.data
        course = Course.objects.create(**data)

        return Response({
            "Message":"Data Created",
            "API": data
        })



@api_view(['GET'])
def Pget(request):
    courses = [
        {   
            "id":course.id,
            "name": course.name,
            "duration" : course.duration
        }

        for course in Course.objects.all()
    ]
    return Response({
        "Status":"Fecth All Data From DB",
        "API": courses
    })


@api_view(['DELETE'])
def Pdelete(request,id):
    try:
        course = Course.objects.get(id=id).delete()
        return Response({
            "Status":True,
            "Message":"Data Deleted Successful",
            
        })
    except Exception as e:
        return Response({
            "Status":False,
            "Message":"Invalid ID",
        })



@api_view(['PUT', 'PATCH'])
def Pupdate(request, id):
    try:
        course = Course.objects.get(id=id)
        data = request.data  
        getdataatr = data.get("name",course.name) 
        print(getdataatr)

        course.name = data.get("name", course.name)  
        course.duration = data.get("duration", course.duration)
        course.save()

        return Response({
            "Status": True,
            "Message": "Data Updated Successfully",
            "Updated Data": {
                "id": course.id,
                "name": course.name,
                "duration": course.duration
            }
        })
    except Course.DoesNotExist:
        return Response({
            "Status": False,
            "Message": "Invalid ID",
        })
    except Exception as e:
        return Response({
            "Status": False,
            "Message": str(e),
        })
    

# Student model Get data


@api_view(['GET'])
def Statusget(request):

    students = [
        {   
            "id":student.id,
            "name":student.name,
            "email":student.email,
            "age":student.age,
            "address":student.address,
            "created_at":student.created_at
        }

        for student in Student.objects.all()
    ]
    return Response({
        "Status":"Fecth All Data From DB",
        "API": students
    })


# -------------------------------- Serializers - (Model Serialzers) --------------------------------------------------

@api_view(['GET'])
def get_data(request):
    queryset = Student.objects.all()
    serializer = StudentSerializers(queryset , many=True)
    return Response(serializer.data)


@api_view(['POST'])
def generateRecords(request):
    data = request.data
    print(data)
    serializer = StudentSerializers( data = data )

    if not serializer.is_valid():
        return Response({"Erros": serializer.errors})

    serializer.save()
    return Response(serializer.data)


@api_view(['PUT','PATCH'])
def update_data(request):
    data = request.data

    if data.get('id') is None:
        return Response({
            "error":"ID is Required",
            "Status": False
        })
    
    student_object = Student.objects.get( id = data.get('id'))
    print(student_object)

    serializer = StudentSerializers(student_object , data = data , partial = True)

    if not serializer.is_valid():
        return Response({'error': serializer.errors})

    serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_data(request):
    data = request.data

    if data.get('id') is None:
        return Response({"Message":"ID is Required"})

    try:
        student_object = Student.objects.get( id = data.get('id'))
    except Student.DoesNotExist:
        return Response({
            "status":"Student Not Found"
        })
    
    student_object.delete()

    return Response({
        "message": "Student deleted successfully!",
        "status": True
    })


    
# -------------------------------- Serializers - (Normal Serialzers) --------------------------------------------------

@api_view(['POST'])
def data_create(request):
    data = request.data
    serializer = StudentSerializer(data=data)

    if not serializer.is_valid():
        return Response({
            "Status":False,
            "Message": serializer.errors
        })
    serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def get_data_of_normal(request):
    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['PUT','PATCH'])
def update_student(request):
    student_id = request.data.get('id') 
    if not student_id:
        return Response({"error": "ID is required"}, status=400)

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)

    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})
    student.delete()
    return Response({"message": "Student deleted successfully"})



# API Views In DRF

from rest_framework.views import APIView

class StudentAPIView(APIView):

    def get(self , request):
        return Response({
            'Status':'200 Ok',
            'message':"Fetch All Records SucessFully !"
        })
    
    def post(self , request):
        return Response({
            'Status':'200 Ok',
            'message':"Post Record SucessFully !"
        })

    def patch(self , request):
        return Response({
            'Status':'200 Ok',
            'message':"Record Updated SucessFully !"
        })

    def delete(self , request):
        return Response({
            'Status':'200 Ok',
            'message':"Record deleted SucessFully !"
        })



# Mixins In DRF

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView


class StudentMixins(ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


    # GET request handle function
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # handle post reuqest

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # Retrive data
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # PUT request (संपूर्ण डेटा बदलण्यासाठी)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # PATCH request (अर्धा डेटा बदलण्यासाठी)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # DELETE request handle करणारी method
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# Concreate View Class => Generics Classes



