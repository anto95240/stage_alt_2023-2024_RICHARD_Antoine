from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Note, User
from django.db.models import Avg

# vue pour récupérer les notes d'un étudiant
def get_student_notes(request):
    student_id = request.GET.get('student_id')
    
    if not student_id:
        return JsonResponse({'error': 'ID de l\'utilisateur manquant'}, status=400)
    
    user = get_object_or_404(User, id=student_id)
    
    notes = Note.objects.filter(student=user)
    
    average_per_subject = notes.values('subject').annotate(average=Avg('note'))
    overall_average = notes.aggregate(overall_avg=Avg('note'))
    
    notes_data = []
    for note in notes:
        notes_data.append({
            'id': note.id,
            'subject': note.subject,
            'note': note.note,
            'total_score': note.total_score,
            'coefficient': note.coefficient,
            'teacher': note.get_teacher_name(),
            'label': note.label,
        })
    
    return JsonResponse({
        'notes': notes_data,
        'average_per_subject': list(average_per_subject),
        'overall_average': overall_average['overall_avg']
    })
