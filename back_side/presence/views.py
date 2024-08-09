from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Presence
from .serializers import PresenceSerializer

@api_view(['GET'])
def get_presences(request):
    student_id = request.GET.get('student_id')
    if student_id:
        presences = Presence.objects.filter(students__id=student_id)
    else:
        presences = Presence.objects.all()
    serializer = PresenceSerializer(presences, many=True)
    return Response(serializer.data)