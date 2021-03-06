from django import forms
from django.forms import ModelForm, Select
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.files.images import get_image_dimensions
from .models import User, Report
import datetime

class signUp(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    company = forms.CharField(label="Company", required=False)
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="E-mail")
    OPTIONS = (
        ('Investor',"Investor"),
        ('Company',"Company"),
        )
    user_type = forms.ChoiceField(choices=OPTIONS)
    password = forms.CharField(label="Password")


class CreateReportForm(forms.Form):
    report_name = forms.CharField(label="Report Name")
    company_name = forms.CharField()
    company_phone = forms.CharField()
    company_location = forms.CharField()
    company_country = forms.CharField()
    company_sector = forms.CharField()
    company_industry = forms.CharField()
    current_projects = forms.CharField(widget=forms.Textarea)
    info = forms.CharField(widget=forms.Textarea)
    filename = forms.FileField(label="Select a file", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    OPTIONS = (
        ('Private',"Private"),
        ('Public',"Public"),
        )
    privacy_setting = forms.ChoiceField(choices=OPTIONS)
    owner = forms.CharField(label = "Owner (enter your username)")

class CreateCommentForm(forms.Form):
    author = forms.CharField(label = "Author (enter your own username)")
    text = forms.CharField()

class EditReportForm(forms.Form):
    company_name = forms.CharField(required=False)
    company_phone = forms.CharField(required=False)
    company_location = forms.CharField(required=False)
    company_country = forms.CharField(required=False)
    company_sector = forms.CharField(required=False)
    company_industry = forms.CharField(required=False)
    current_projects = forms.CharField(required=False, widget=forms.Textarea)
    info = forms.CharField(required=False, widget=forms.Textarea)
    filename = forms.FileField(label="Add files", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

class CreateMessageForm(forms.Form):
    recipient = forms.CharField()
    sender = forms.CharField()
    message_body = forms.CharField(widget=forms.Textarea)
    OPTIONS = (
        ('Private',"Private"),
        ('Public',"Public"),
        )
    privacy = forms.ChoiceField(choices=OPTIONS)
    OPTIONS = (
        ('Encrypted',"Encrypted  (only if private message)"),
        ('Unencrypted',"Unencrypted"),
        )
    encryption = forms.ChoiceField(choices=OPTIONS)

class DownloadMessageForm(forms.Form):
    private_key = forms.CharField(widget=forms.Textarea)

class CreateGroupForm(forms.Form):
    # public_reports = Report.objects.filter(privacy_setting = "Public")
    # users_reports = Report.objects.filter(owner = uname)
    group_name = forms.CharField()
    users = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all())
    # group_reports = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=self.merge)

    def __init__(self, *args, **kwargs):
        uname = kwargs.pop('uname')
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        public_reports = Report.objects.filter(privacy_setting = "Public")
        users_reports = Report.objects.filter(owner = uname)
        merge = public_reports | users_reports
        self.fields['group_reports'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=merge)




class AddUserForm(forms.Form):
    user = forms.CharField()

class user_privileges(forms.Form):
    CHOICES = (
        ('False', "False"),
        ('True', "True"),
        )
    has_manager_privileges = forms.ChoiceField(CHOICES)

class searchForm(forms.Form):
    search = forms.CharField()

class searchMessageForm(forms.Form):
    search = forms.CharField()

class addFiles(forms.Form):
    filename = forms.FileField(label="Select files", widget=forms.ClearableFileInput(attrs={'multiple': True}))
