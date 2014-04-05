from django.conf.urls import patterns
from django.conf.urls import url
from views import HandicapView
from views import RecordView


urlpatterns = patterns("",
    url(r"^handicap/$", HandicapView.as_view(), name="handicap"),
    url(r"^record/(?P<score_id>\d)/$", RecordView.as_view(), name="record"),
)

