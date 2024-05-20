from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
from io import BytesIO
import base64

def gen(image):
    img = Image.open(image)
    img_resized = img.resize((img.width // 2, img.height // 2), Image.LANCZOS)
    return img_resized

def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        image_description = request.POST['description']

        img_resized = gen(image)

        img_buffer = BytesIO()
        img_resized.save(img_buffer, format='JPEG')
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return JsonResponse({'image': img_str})

    return render(request, 'upload_image.html')