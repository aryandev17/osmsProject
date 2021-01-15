from .models import UserProfilePicture

def user_image(request):
    if request.user.is_authenticated:
        image = UserProfilePicture.objects.filter(user=request.user).first()
        if image:
            return {
                "image":image,
            }
        else:
            return {
                "image":False,
            }
    else:
        return {
            "image":False,
        }