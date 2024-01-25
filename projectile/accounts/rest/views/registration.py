from rest_framework.generics import CreateAPIView

from accounts.rest.serializers.registration import UserRegistrationSerializer


class UserRegistration(CreateAPIView):
    serializer_class = UserRegistrationSerializer