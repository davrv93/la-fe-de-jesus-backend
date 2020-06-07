from django.conf.urls import url, include
from session.models.session import Session
from rest_framework import routers, serializers, viewsets, views, status
from session.models.section import Section
from session.models.item import Item
from session.models.verse import Verse
from session.models.choice import Choice
from rest_framework.response import Response
from rest_framework import mixins, viewsets

class VerseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verse
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    verse = VerseSerializer(read_only=True, many=True)
    choice_item_set = ChoiceSerializer(read_only=True, many=True)
    class Meta:
        model = Item
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    item_section_set = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Section
        fields = ['item_section_set','session','name','order','type']

class SessionSerializer(serializers.ModelSerializer):
    section_session_set = SectionSerializer(read_only=True,many=True)

    class Meta:
        model=Session
        fields = '__all__'


class ContentViewSet(viewsets.views.APIView):
    queryset =  None
    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request):
        code = self.request.query_params.get('code', None)
        print('test', code)
        try:
            instance = Session.objects.get(code=code)

            data = SessionSerializer(instance).data

            return Response(data, status=status.HTTP_200_OK)



        except Exception as e:
            print(e)
            data=dict(
                msg='Error'
            )

            return Response(data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

