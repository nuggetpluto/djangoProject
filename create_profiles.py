from django.contrib.auth.models import User
from account.models import Profile

users_without_profiles = User.objects.filter(profile__isnull=True)

for user in users_without_profiles:
    Profile.objects.create(user=user)

print(f"Created profiles for {users_without_profiles.count()} users.")
