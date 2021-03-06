from django.dispatch import Signal

#Often, one would like to perform some action (like sending a confirmation email)
#upon successful user registration.
registration_successful = Signal(providing_args = ['request', 'user'])
rpx_login = Signal(providing_args=['request', 'success'])
