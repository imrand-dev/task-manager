from rest_framework import serializers

from accounts.models import User 
from accounts.services.users import UserService

user_service = UserService()

