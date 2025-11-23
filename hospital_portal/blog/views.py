from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost, Category

# Doctor creates blog
@login_required
def create_blog(request):
    if request.user.role != "doctor":
        return redirect("home")

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.doctor = request.user
            blog.save()
            return redirect("blog:doctor_my_blogs")
    else:
        form = BlogPostForm()

    return render(request, "blog/create_blog.html", {"form": form})


# Doctor manages their blog
@login_required
def doctor_my_blogs(request):
    posts = BlogPost.objects.filter(doctor=request.user)
    return render(request, "blog/doctor_blogs.html", {"posts": posts})


# To view all the blogs
@login_required
def view_blogs(request):
    selected_category = request.GET.get("category")  # Get category from dropdown

    if selected_category:
        posts = BlogPost.objects.filter(category_id=selected_category, is_draft=False)
    else:
        posts = BlogPost.objects.filter(is_draft=False)

    # for group category
    data = {}
    for post in posts:
        cat_name = post.category.name if post.category else "Uncategorized"
        if cat_name not in data:
            data[cat_name] = []
        data[cat_name].append(post)

    categories = Category.objects.all()  # For dropdown

    return render(request, "blog/view_blogs.html", {
        "data": data,
        "categories": categories,
        "selected_category": selected_category
    })
@login_required
def edit_blog(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, doctor=request.user)

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:doctor_my_blogs")
    else:
        form = BlogPostForm(instance=post)

    return render(request, "blog/edit_blog.html", {"form": form, "post": post})

@login_required
def delete_blog(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id, doctor=request.user)
    post.delete()
    return redirect("blog:doctor_my_blogs")


def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    return render(request, "blog/blog_detail.html", {"blog": blog})
