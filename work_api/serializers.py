from rest_framework import serializers
from work_api.models import Label, Work


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = '__all__'
        read_only_fields = ['start_time', 'end_time', 'is_completed']

    def to_representation(self, instance):
        data = super(WorkSerializer, self).to_representation(instance)
        if not data['end_time']:
            data['end_time'] = 'ongoing'
        return data


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']
