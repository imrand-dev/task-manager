from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password1, password2, **extra_fields):
        if not email:
            raise ValueError(_("Email address is required."))
        if not password1:
            raise ValueError(_("Password is required."))

        if password1 != password2:
            raise ValueError(_("Passwords don't match."))
        
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.first_name = first_name.title()
        user.last_name = last_name.title()
        user.set_password(password1)
        user.save(using=self._db)

        return user 
    
    def create_superuser(self, first_name, last_name, email, password1, password2, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(first_name, last_name, email, password1, password2, **extra_fields)
