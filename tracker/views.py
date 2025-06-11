from django.shortcuts import get_object_or_404, render, redirect

from tracker.models import Branch, Commit, Repository
from .forms import RepositoryForm
from django.contrib.auth.decorators import login_required
from .forms import BranchForm

@login_required
def create_repository(request):
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            repo = form.save(commit=False)
            repo.owner = request.user
            repo.save()
            return redirect('repository_list')  # We'll create this URL/view later
    else:
        form = RepositoryForm()
    
    return render(request, 'tracker/create_repository.html', {'form': form})

@login_required
def repository_list(request):
    repos = Repository.objects.filter(owner=request.user)
    return render(request, 'tracker/repository_list.html', {'repositories': repos})

@login_required
def branch_list(request, repo_id):
    repository = get_object_or_404(Repository, id=repo_id, owner=request.user)
    branches = Branch.objects.filter(repository=repository)
    return render(request, 'tracker/branch_list.html', {
        'repository': repository,
        'branches': branches
    })




@login_required
def create_branch(request, repo_id):
    repository = get_object_or_404(Repository, id=repo_id, owner=request.user)

    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.repository = repository
            branch.save()
            return redirect('branch_list', repo_id=repository.id)
    else:
        form = BranchForm()

    return render(request, 'tracker/create_branch.html', {
        'form': form,
        'repository': repository
    })

@login_required
def commit_list(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id, repository__owner=request.user)
    commits = Commit.objects.filter(branch=branch).order_by('-timestamp')
    return render(request, 'tracker/commit_list.html', {
        'branch': branch,
        'commits': commits
    })