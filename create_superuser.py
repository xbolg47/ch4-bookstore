# create_superuser.py
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="bolg").exists():
    User.objects.create_superuser("bolg", "bolg@rabine.com", "bolgpass123")
