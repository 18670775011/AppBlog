from django import forms


class GroupForm(forms.Form):
    """博客分组"""
    g_name = forms.CharField(required=True)
