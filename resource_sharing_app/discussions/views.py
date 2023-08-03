from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Discussion, Resource
from .forms import CommentForm, CreateDiscussionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

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

    return render(request, 'discussions/discussion_detail.html', {'discussion': discussion, 'comments': comments, 'form': form})


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        # Only allow the author of the comment or a superuser to delete it
        if comment.author == request.user or request.user.is_superuser:
            comment.delete()
            messages.success(request, 'Comment deleted successfully.')
            return redirect('discussion_detail', pk=comment.discussion.pk)
        else:
            try:
                # Attempt to delete the comment to trigger the PermissionDenied exception
                comment.delete()
            except PermissionDenied:
                messages.error(request, 'You do not have permission to delete this comment.')

    return render(request, 'discussions/delete_comment.html', {'comment': comment})

def resource_detail(request):
    resource = get_object_or_404(Resource)
    discussions = Discussion.objects.filter(resource=resource)
    return render(request, 'discussions/resource_detail.html', {'resource': resource, 'discussions': discussions})

def create_discussion(request):
    if request.method == 'POST':
        form = CreateDiscussionForm(request.POST)
        if form.is_valid():
            discussion_id = form.cleaned_data['discussion_id']

            # Check if the discussion ID already exists in the database
            if Discussion.objects.filter(discussion_id=discussion_id).exists():
                messages.error(request, f"A discussion with ID '{discussion_id}' already exists.")
            else:
                title = form.cleaned_data['title']
                discussion = Discussion.objects.create(discussion_id=discussion_id, title=title)

                # Redirect to the discussion list page after creating the discussion
                return redirect('discussion_list')
        else:
            # If the form is not valid, redisplay the form with errors
            form = CreateDiscussionForm(request.POST)
    else:
        form = CreateDiscussionForm()

    return render(request, 'discussions/create_discussion.html', {'form': form,'messages': messages.get_messages(request)})

def delete_discussion(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)

    if request.method == 'POST':
        # Only allow the author of the discussion to delete it
        if discussion.author == request.user:
            discussion.delete()
            messages.success(request, 'Discussion deleted successfully.')
            return redirect('discussion_list')
        else:
            messages.error(request, 'You do not have permission to delete this discussion.')

    return render(request, 'discussions/delete_discussion.html', {'discussion': discussion})


def discussion_detail(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    comments = Comment.objects.filter(discussion=discussion, parent=None)
    return render(request, 'discussions/discussion_detail.html', {'discussion': discussion, 'comments': comments})

def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, 'discussions/discussion_list.html', {'discussions': discussions})
