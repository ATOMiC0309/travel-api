from rest_framework import serializers
from .models import Hotel, Klass, Travel


class TravelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    comment = serializers.CharField()
    lifetime = serializers.IntegerField()
    price = serializers.FloatField()
    klass_id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.lifetime = validated_data.get('lifetime', instance.lifetime)
        instance.klass_id = validated_data.get('klass_id', instance.klass_id)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.price = validated_data.get('price', instance.price)
        instance.created = validated_data.get('created', instance.created)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.save()
        return instance


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    stars = serializers.IntegerField(default=0)
    price = serializers.FloatField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.price = validated_data.get('price', instance.price)
        instance.created = validated_data.get('created', instance.created)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance


class KlassSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    price = serializers.FloatField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Klass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.created = validated_data.get('created', instance.created)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance
