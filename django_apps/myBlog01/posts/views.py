from django.shortcuts import get_object_or_404, redirect, render

from .models import Post

def home(request):
	posts = Post.objects.order_by('id')
	return render(request, 'posts/home.html', { 'posts': posts })

def sort(request, sort_by):
	try:
		order = {
			'mr': '-created_date',
			'of': 'created_date',
			'mp': '-views_total',
			'lp': 'views_total',
		}
		posts = Post.objects.order_by(order[sort_by])
		return render(request, 'posts/home.html', { 'sort_by': sort_by, 'posts': posts })
	except KeyError:
		return redirect('home')

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.views_total += 1
	post.save()
	return render(request, 'posts/post_detail.html', {'post': post})
