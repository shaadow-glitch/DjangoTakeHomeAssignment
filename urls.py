from django.urls import path
from .. import views

urlpatterns = [
    path("tables/", views.table_dashboard),
    path("order/<int:table_id>/<int:menu_id>/<int:qty>/", views.create_order),
    path("bill/<int:table_id>/", views.generate_bill),
    path("pay/<int:table_id>/", views.pay_bill),
]
