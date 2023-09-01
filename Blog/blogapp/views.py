from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import Mypermission


class Blog(ViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def create(self,request):
        ser=BlogSerializer(data=request.data,context={'request':request})
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data created"},status=status.HTTP_201_CREATED)
        return Response({"msg":"Invalid Request"},status=status.HTTP_400_BAD_REQUEST)
        
    def list(self,request):
        blog=BlogPost.objects.all()
        ser=BlogSerializer(blog,many=True)
        return Response(ser.data,status=status.HTTP_202_ACCEPTED)
    
    def retrieve(self,request,pk):
        if BlogPost.objects.filter(id=pk).exists():   #first check whether the requested id is present or not
            blog=BlogPost.objects.get(id=pk)
            ser=BlogSerializer(blog)
            return Response(ser.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"msg":"Data not found"},status=status.HTTP_204_NO_CONTENT)
        
    def update(self,request,pk):
        if BlogPost.objects.filter(id=pk).exists():
            ins=BlogPost.objects.get(id=pk)
            ser=BlogSerializer(ins,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"msg":"Data updated"},status=status.HTTP_202_ACCEPTED)
            return Response({"msg":"Data not updated"},status=status.HTTP_304_NOT_MODIFIED)
        else:
            return Response({"msg":"Invalid request"},status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):
        if BlogPost.objects.filter(id=pk).exists():
            ins=BlogPost.objects.get(id=pk)
            ser=BlogSerializer(ins,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"msg":"Data updated"},status=status.HTTP_202_ACCEPTED)
            return Response({"msg":"Data not updated"},status=status.HTTP_304_NOT_MODIFIED)
        else:
            return Response({"msg":"Invalid request"},status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        if BlogPost.objects.filter(id=pk).exists():
            blog=BlogPost.objects.get(id=pk)
            blog.delete()
            return Response({"msg":"Data removed"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"msg":"Invalid request"},status=status.HTTP_400_BAD_REQUEST)

        
class GetAll(ViewSet):
    permission_classes=[Mypermission]
    def list(self,request):
        blog=BlogPost.objects.all()
        ser=BlogSerializer(blog,many=True)
        return Response(ser.data,status=status.HTTP_202_ACCEPTED)
    
    def retrieve(self,request,pk):
        if BlogPost.objects.filter(id=pk).exists():
            blog=BlogPost.objects.get(id=pk)
            ser=BlogSerializer(blog)
            return Response(ser.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"msg":"Data not found"},status=status.HTTP_204_NO_CONTENT)