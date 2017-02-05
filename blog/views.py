from django.shortcuts import render
import os
import numpy as np
import cv2
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils import timezone
from .models import Post

def post_list(request):
    img = cv2.imread(r'C:\Django\mysite\blog\static\blog\misdyxcgAo4.jpg', 0)
    cv2.imwrite(r'C:\Django\mysite\blog\static\blog\messigray.png', img)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})