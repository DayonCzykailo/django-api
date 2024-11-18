from django.http import JsonResponse 


def students(request):
    if request.method == 'GET':
        return JsonResponse({'students': ['Alice', 'Bob', 'Charlie']})