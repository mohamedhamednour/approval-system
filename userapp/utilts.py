from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class CustomSocialLoginView(SocialLoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Check if authentication was successful
        if response.status_code == 200 and self.user:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(self.user)

            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user': {
                    'id': self.user.id,
                    'email': self.user.email,
                    'username': self.user.username,
                    'avatar': self.user.avatar.url if hasattr(self.user, 'avatar') and self.user.avatar else None,
                    'company': getattr(self.user, 'compony', None),
                    'phone_number': getattr(self.user, 'phone_number', ''),
                }
            }, status=status.HTTP_200_OK)

        return response