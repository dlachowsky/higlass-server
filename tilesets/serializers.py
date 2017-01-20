from rest_framework import serializers
from tilesets.models import Tileset, Viewprint
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    tilesets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tileset.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username')

class ViewPrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewPrint
        fields = ('uid', 'viewprint')


class TilesetSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Tileset
        fields = ('uuid', 'datafile', 'filetype', 'datatype', 'private', 'name')

class UserFacingTilesetSerializer(TilesetSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Tileset
        fields = ('uuid', 'filetype', 'datatype', 'private', 'name')
