from django.contrib.auth import decorators

"""
This alias decorator was added because django does not have an anonymous user decorator
check https://docs.djangoproject.com/en/4.1/topics/auth/default/
"""
anonymous_user_required = decorators.user_passes_test(
    lambda user: not user.is_authenticated, login_url="/", redirect_field_name=None
)
