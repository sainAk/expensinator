from django.urls import path

from ..views import StatisticsDataView, StatisticsView


urlpatterns = [
    path("statistics/", StatisticsView.as_view(), name="statistics-list"),
    path(
        "statistics/data",
        StatisticsDataView.as_view(),
        name="statistics-data",
    ),
]
