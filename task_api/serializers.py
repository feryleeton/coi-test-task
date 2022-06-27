from task_app.models import Category, Doctor
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'slug', 'categories', 'descr', 'birth_date', 'experience')