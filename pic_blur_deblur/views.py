import os

import cv2

from django.shortcuts import render
from pic_blur_deblur.models import IMG
from pic_blur_deblur.function import blur, cus_filter2D
# Create your views here.

from django.http import HttpResponse


def upload(request):
    if request.method == 'POST':
        new_img = IMG(img=request.FILES.get('upimg'))
        new_img.save()

        m11 = request.POST['m11']
        m12 = request.POST['m12']
        m13 = request.POST['m13']
        m21 = request.POST['m21']
        m22 = request.POST['m22']
        m23 = request.POST['m23']
        m31 = request.POST['m31']
        m32 = request.POST['m32']
        m33 = request.POST['m33']

        print(m11)


        print(new_img.img.path)
        img_name = str(new_img.img.name).split('/')[1].split('.')[0]
        if not os.path.isdir("media/" + img_name):
            os.mkdir("media/" + img_name)

        cvimg = cv2.imread(new_img.img.path, 0)
        img_blur, img_B, img_C = blur(cvimg, 100, 1 / 4, 1 / 2, 1 / 4)

        img_deblur = cus_filter2D(cvimg)

        cv2.imwrite("media/" + img_name + "/source.jpg", cvimg)
        cv2.imwrite("media/" + img_name + "/blur.jpg", img_blur)
        cv2.imwrite("media/" + img_name + "/blur_B.jpg", img_B)
        cv2.imwrite("media/" + img_name + "/blur_C.jpg", img_C)
        cv2.imwrite("media/" + img_name + "/img_deblur.jpg", img_deblur)

        content = {
            'aaa': new_img,
            'sourse': "/media/" + img_name + "/source.jpg",
            'blur': "/media/" + img_name + "/blur.jpg",
            'blur_B': "/media/" + img_name + "/blur_B.jpg",
            'blur_C': "/media/" + img_name + "/blur_C.jpg",
            'img_deblur': "/media/" + img_name + "/img_deblur.jpg",

        }
        return render(request, 'index.html', content)


    return render(request, 'index.html')
def show(request):

    new_img = IMG(img=request.FILES.get('img'))
    new_img.save()
    print(new_img.img.path)
    img_name = str(new_img.img.name).split('/')[1].split('.')[0]
    if not os.path.isdir("media/"+img_name):
        os.mkdir("media/"+img_name)


    cvimg = cv2.imread(new_img.img.path, 0)
    img_blur, img_B, img_C = blur(cvimg, 100, 1/4, 1/2, 1/4)
    img_deblur = cus_filter2D(cvimg)



    cv2.imwrite("media/"+img_name+"/source.jpg", cvimg)
    cv2.imwrite("media/"+img_name+"/blur.jpg", img_blur)
    cv2.imwrite("media/"+img_name+"/blur_B.jpg", img_B)
    cv2.imwrite("media/"+img_name+"/blur_C.jpg", img_C)
    cv2.imwrite("media/"+img_name+"/img_deblur.jpg", img_deblur)





    content = {
        'aaa': new_img,
        'sourse' : "/media/"+img_name+"/source.jpg",
        'blur' : "/media/"+img_name+"/blur.jpg",
        'blur_B' : "/media/"+img_name+"/blur_B.jpg",
        'blur_C' : "/media/"+img_name+"/blur_C.jpg",
        'img_deblur' : "/media/"+img_name+"/img_deblur.jpg",

    }
    return render(request, 'index.html', content)