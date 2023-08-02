from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Discussion, Resource
from .forms import CommentForm, CreateDiscussionForm
from django.contrib.auth.decorators import login_required

def create_comment(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    comments = Comment.objects.filter(discussion=discussion)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.author = request.user
            comment.save()
            # After saving the new comment, retrieve all comments for the discussion
            comments = Comment.objects.filter(discussion=discussion)
            form = CommentForm()  # Reset the form

    else:
        form = CommentForm()

    return render(request, 'discussion_detail.html', {'discussion': discussion, 'comments': comments, 'form': form})

def resource_detail(request):
    resource = get_object_or_404(Resource)
    discussions = Discussion.objects.filter(resource=resource)
    return render(request, 'resource_detail.html', {'resource': resource, 'discussions': discussions})

def create_discussion(request):
    if request.method == 'POST':
        form = CreateDiscussionForm(request.POST)
        if form.is_valid():
            # Save the new discussion to the database
            discussion_id = form.cleaned_data['discussion_id']
            title = form.cleaned_data['title']
            discussion = Discussion.objects.create(discussion_id=discussion_id, title=title)

            # Redirect to the discussion detail page after creating the discussion
            return redirect('discussion_detail', pk=discussion.pk)
    else:
        form = CreateDiscussionForm()

    return render(request, 'create_discussion.html', {'form': form})

def discussion_detail(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    comments = Comment.objects.filter(discussion=discussion, parent=None)
    return render(request, 'discussion_detail.html', {'discussion': discussion, 'comments': comments})

def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, 'discussion_list.html', {'discussions': discussions})
