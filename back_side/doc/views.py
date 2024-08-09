from django.http import JsonResponse
from .models import *
from .serializers import *
from django.http import HttpResponse, Http404

# vue pour récupéré les documents
def get_user_documents(request):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    return JsonResponse(serializer.data, safe=False)

# vue pour télécharger un document
def download_document(request, document_id):
    try:
        document = Document.objects.get(id=document_id)
        response = HttpResponse(document.file_path.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{Document.name}.pdf"'
        return response
    except Document.DoesNotExist:
        raise Http404("Document not found")