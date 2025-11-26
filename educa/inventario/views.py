from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Hardware, Falla, Mantenimiento

# -------------------------------
#     CRUD HARDWARE
# -------------------------------
class HardwareListView(ListView):
    model = Hardware
    template_name = "inventario/hardware_list.html"


class HardwareCreateView(CreateView):
    model = Hardware
    fields = "__all__"
    template_name = "inventario/hardware_form.html"
    success_url = reverse_lazy("hardware_list")


class HardwareUpdateView(UpdateView):
    model = Hardware
    fields = "__all__"
    template_name = "inventario/hardware_form.html"
    success_url = reverse_lazy("hardware_list")


class HardwareDeleteView(DeleteView):
    model = Hardware
    template_name = "inventario/hardware_delete.html"
    success_url = reverse_lazy("hardware_list")


class HardwareDetailView(DetailView):
    model = Hardware
    template_name = "inventario/hardware_detail.html"


# -------------------------------
#     CRUD FALLA
# -------------------------------
class FallaListView(ListView):
    model = Falla
    template_name = "inventario/falla_list.html"


class FallaCreateView(CreateView):
    model = Falla
    fields = "__all__"
    template_name = "inventario/falla_form.html"
    success_url = reverse_lazy("falla_list")


class FallaUpdateView(UpdateView):
    model = Falla
    fields = "__all__"
    template_name = "inventario/falla_form.html"
    success_url = reverse_lazy("falla_list")


class FallaDeleteView(DeleteView):
    model = Falla
    template_name = "inventario/falla_delete.html"
    success_url = reverse_lazy("falla_list")


class FallaDetailView(DetailView):
    model = Falla
    template_name = "inventario/falla_detail.html"


# -------------------------------
#     CRUD MANTENIMIENTO
# -------------------------------
class MantenimientoListView(ListView):
    model = Mantenimiento
    template_name = "inventario/mantenimiento_list.html"


class MantenimientoCreateView(CreateView):
    model = Mantenimiento
    fields = "__all__"
    template_name = "inventario/mantenimiento_form.html"
    success_url = reverse_lazy("mantenimiento_list")


class MantenimientoUpdateView(UpdateView):
    model = Mantenimiento
    fields = "__all__"
    template_name = "inventario/mantenimiento_form.html"
    success_url = reverse_lazy("mantenimiento_list")


class MantenimientoDeleteView(DeleteView):
    model = Mantenimiento
    template_name = "inventario/mantenimiento_delete.html"
    success_url = reverse_lazy("mantenimiento_list")


class MantenimientoDetailView(DetailView):
    model = Mantenimiento
    template_name = "inventario/mantenimiento_detail.html"
