from centrointernet.models import NetworkConnection
from centrointernet.models import Service
from centrointernet.models import ClientStatus

from centrointernet.models import Client

from centrointernet.models import TypeProblem 
from centrointernet.models import ProblemStatus

from centrointernet.models import Problem

from centrointernet.models import MethodPayment
from centrointernet.models import TypeHistorical

from centrointernet.models import Historical

from django.contrib import admin

admin.site.register(NetworkConnection)
admin.site.register(Service)
admin.site.register(ClientStatus)
admin.site.register(Client)
admin.site.register(TypeProblem)
admin.site.register(Problem)
admin.site.register(ProblemStatus)
admin.site.register(MethodPayment)
admin.site.register(TypeHistorical)
admin.site.register(Historical)
