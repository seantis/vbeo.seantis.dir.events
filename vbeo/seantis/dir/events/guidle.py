from five import grok
from zope.interface import Interface

from seantis.dir.events.interfaces import IEventsDirectory
from seantis.dir.events.sources.guidle import IGuidleConfig

from vbeo.seantis.dir.events import _


class GuidleConfig(grok.MultiAdapter):
    grok.adapts(IEventsDirectory, Interface)
    grok.implements(IGuidleConfig)

    url = ("http://www.guidle.com/dpAccess.jsf"
           "?id=193352638&language=de&dateOption=NA&primaryTreeId=196238674"
           "&tagIds=196238674&where=38421957&sorting=ungrouped"
           "&locationTreeId=13181&template=xml2")

    classification = "Veranstaltungskalender MySwitzerland"

    tags = {
        'A': _(u"Concerts"),
        'B': _(u"Theatres"),
        'C': _(u"Art"),
        'D': _(u"Fair"),
        'E': _(u"Customs, Market"),
        'F': _(u"Festival, Festivities"),
        'G': _(u"Congress, Course"),
        'H': _(u"Sports"),
        'I': _(u"Excursions for guests"),
        'J': _(u"Meetings, Animation"),
        'K': _(u"Gastronomy"),
    }

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def on_event(self, root, offer, event):
        pass
