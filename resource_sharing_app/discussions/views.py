from django.shortcuts import render, redirect,get_object_or_404
from discussions.models import Comment, Discussion
from discussions.forms import CommentForm

def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            discussion_id = request.POST.get('discussion_id')
            discussion = get_object_or_404(Discussion, pk=discussion_id)
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.author = request.user
            comment.save()
            return redirect('resource_detail', resource_id=discussion.resource.id)
    else:
        form = CommentForm()

    return render({'form': form})
