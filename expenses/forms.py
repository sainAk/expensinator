from django import forms
from django.forms import widgets
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from categories.models import Category
from expenses.models import Expense


class AddExpenseForm(forms.ModelForm):

    error_css_class = "is-invalid"
    user = None

    created_at = forms.SplitDateTimeField(
        widget=widgets.SplitDateTimeWidget(
            date_attrs={"class": "form-control", "type": "date"},
            time_attrs={"class": "form-control", "type": "time"},
            time_format="%H:%M",
        ),
        initial=now,
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        category_field = self.fields["category"]
        category_field.queryset = Category.objects.filter(owner=self.user)
        category_field.widget.attrs["class"] = "form-select"
        category_field.empty_label = ""
        category_field.required = False

    class Meta:
        model = Expense
        fields = (
            "name",
            "amount",
            "category",
            "created_at",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
        }
