from django.shortcuts import redirect
from django.contrib import messages

def permission_denied(request):
    messages.warning(request, '權限不足')
    return redirect('root')