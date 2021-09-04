from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class User(models.Model):
    warden_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    warden_email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

    class Meta():
        db_table = "warden"


def valid_email(value):
    if "@thapar.edu" in value:
        return value
    else:
        raise ValidationError("Domain of email is not valid")


class CustomUser(models.Model):
    sex_choices = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    courses = (
        ('copc', 'COPC'),
        ('cose', 'COSE'),
        ('enc', 'ENC'),
        ('coe', 'COE'),
        ('ele', 'ELE'),
        ('ece', 'ECE'),
        ('mec', 'MEC'),
        ('che', 'CHE')
    )
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    roll_no = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, validators=[valid_email])
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=sex_choices)
    Course = models.CharField(max_length=255, choices=courses, default="COPC")
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    warden_id = models.ForeignKey(User, null=True, on_delete=CASCADE)
    last_login = models.DateTimeField(verbose_name="last-login", auto_now=True)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.id)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code{self.first_name}{self.last_name}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    class Meta():
        db_table = "STUDENT"


class UserOTP(models.Model):
    user = models.ForeignKey(CustomUser, default=1, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.PositiveIntegerField(default=0)


class record(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=20)
    phone = models.CharField(max_length=255)
    student_email = models.EmailField(max_length=255)
    date_of_entry = models.DateField(auto_now_add=False)
    time_of_entry = models.TimeField(auto_now_add=False)
    warden_name = models.CharField(max_length=256)
    warden_email = models.CharField(max_length=50)

    class Meta():
        db_table = "Record_Table"
