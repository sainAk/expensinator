from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django_filters.views import FilterView

from expenses.models import Category, Expense

from ..filters import ExpenseFilter
from ..forms import AddExpenseForm


class ExpenseListView(LoginRequiredMixin, FilterView):

    filterset_class = ExpenseFilter

    login_url = reverse_lazy("login")
    template_name = "expenses/expense_list.html"
    paginate_by = 20
    context_object_name = "expenses_list"
    page_name = "Expenses"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
        "currency": "₹",
    }

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)


class ExpenseCreateView(LoginRequiredMixin, CreateView):

    template_name = "expenses/expense_create.html"
    form_class = AddExpenseForm

    next_page = reverse_lazy("expenses-list")
    page_name = "Login"
    page_name = "New Expense"
    extra_context = {
        "title": page_name,
        "activeNavId": "navItemExpenses",
        "currency": "₹",
    }


class CategoriesListView(LoginRequiredMixin, ListView):

    login_url = reverse_lazy("login")
    template_name = "expenses/categories_list.html"
    paginate_by = 20
    context_object_name = "categories_list"
    page_name = "Categories"
    extra_context = {
        "title": page_name,
        "activeNavId": f"navItem{page_name}",
    }

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
