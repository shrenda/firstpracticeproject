
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db.models.deletion import CASCADE
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError("User must have Email")
        if not name:
            raise ValueError("User must have name")
        if not username:
            raise ValueError("User must have username")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, username, name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            name = name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user




class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class post(models.Model):
    title =  models.CharField(max_length=100)
    desc  = models.TextField()
    user = models.ForeignKey(Account, on_delete=CASCADE)
    def __str__(self):
        return self.title