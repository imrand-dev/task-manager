from PIL import Image

from accounts.models import User 


class UserService:
    def create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password1: str,
        password2: str,
        avatar: Image.Image = None,
        is_active: bool = True,
        is_staff: bool = False,
        is_verified: bool = True,
    ) -> User:
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            password1=password1,
            password2=password2,
            email=email,
            avatar=avatar,
            is_active=is_active,
            is_staff=is_staff,
            is_verified=is_verified,
        )

    def create_superuser(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password1: str,
        password2: str,
        avatar: Image.Image = None,
        is_active: bool = True,
        is_staff: bool = True,
        is_verified: bool = True,
        is_superuser: bool = True,
    ) -> User:
        return User.objects.create_superuser(
            first_name=first_name,
            last_name=last_name,
            password1=password1,
            password2=password2,
            email=email,
            avatar=avatar,
            is_active=is_active,
            is_staff=is_staff,
            is_verified=is_verified,
            is_superuser=is_superuser,
        )

    def get_user_by_email(self, email: str) -> User:
        return User.objects.get(email=email)
    
    def get_user_by_uid(self, uid: str) -> User:
        return User.objects.get(uid=uid)