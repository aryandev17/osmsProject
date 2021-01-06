from .models import UserProfilePicture

def user_image(request):
    if request.user.is_authenticated:
        image = UserProfilePicture.objects.get(user=request.user)
        return {
            "image":image,
        }
    else:
        return {
            "image":False,
        }