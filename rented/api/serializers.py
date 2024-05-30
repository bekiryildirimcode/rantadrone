from rest_framework import serializers

from rented.models import RentedModel


class RentedSerializer(serializers.ModelSerializer):
    drone_image = serializers.SerializerMethodField()

    class Meta:
        model = RentedModel
        fields = ('id', 'drone', 'drone_image', 'start_date', 'start_time', 'end_date', 'end_time')

    def get_drone_image(self, rented):
        return rented.drone.image.url if rented.drone.image else ''

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret[
            'image'] = f'<img src="{instance.drone.image.url}" alt="{instance.drone.name}" style="height: 50px;">{instance.drone.name}',
        ret['start_date_and_time'] = instance.start_date.strftime('%Y-%m-%d') + '/' + instance.start_time.strftime('%H:%M'),
        ret['end_date_and_time'] = instance.end_date.strftime('%Y-%m-%d') + '/' + instance.end_time.strftime('%H:%M'),
        ret['start_time'] = instance.start_time.strftime('%H:%M')
        ret['end_time'] = instance.end_time.strftime('%H:%M')
        ret['action'] = (f'<button class="edit-btn m-2 px-3 py-2 text-xs font-medium text-center " '
                         f'data-id="{instance.id}">Edit</button><button class="delete-btn text-black m-2 px-3 py-2 text-xs '
                         f'font-medium text-center " data-id="{instance.id}">Delete</button>')

        return ret
