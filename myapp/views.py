from django.shortcuts import render
from datetime import datetime

comment_list = []
index_list = []

def comment_view(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        comment = request.POST.get('comment')
        timestamp = datetime.now()
        comment_list.insert(0, {'nickname': nickname, 'comment': comment, 'timestamp': timestamp})
    return render(request, 'comment.html', {'comment_list': comment_list})


def main_view(request):
    return render(request, 'main.html')
