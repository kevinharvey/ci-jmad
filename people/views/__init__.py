from django.core.urlresolvers import reverse_lazy

from authtools.views import LoginView

class JmadLoginView(LoginView):
    success_url = reverse_lazy("index")
