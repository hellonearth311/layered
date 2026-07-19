from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

from ...models import Project, Ship
from ..helpers import check_perms

@staff_member_required
@check_perms(["layered_site.organizer", "layered_site.fulfillment", "layered_site.t1_review", "layered_site.t2_review", "layered_site.t3_review", "layered_site.printer"])
def admin_dash(request):
    return render(request, "root/home.html")