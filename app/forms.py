from django import forms


class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100)
    sage=forms.IntegerField()
    surl=forms.URLField()
    semail=forms.EmailField()
    
