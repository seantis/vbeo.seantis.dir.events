from five import grok
from zope.interface import Interface

from seantis.dir.events.interfaces import IEventsDirectory
from seantis.dir.events.sources.guidle import IGuidleConfig


class GuidleConfig(grok.MultiAdapter):
    grok.adapts(IEventsDirectory, Interface)
    grok.implements(IGuidleConfig)

    url = ("http://www.guidle.com/dpAccess.jsf"
           "?id=193352638&language=de&dateOption=NA&primaryTreeId=196238674"
           "&tagIds=196238674&where=38421957&sorting=ungrouped"
           "&locationTreeId=13181&template=xml2")

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def on_event(self, root, offer, event):
        pass
