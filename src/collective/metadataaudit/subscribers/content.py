################################################################
# collective.metadataaudit
################################################################

# Subscriber for modify/created event for logging all metadata changes
# through zopyx.plone.persistentlogger


import zope.component
from plone.app.textfield.value import RichTextValue
from plone.dexterity.interfaces import IDexterityFTI
from plone.behavior.interfaces import IBehaviorAssignable
from plone.dexterity.interfaces import IDexterityContent

from zopyx.plone.persistentlogger.logger import IPersistentLogger


def get_all_fields(context):
    """ Return all fields (including behavior fields) of a context object
        as dict fieldname -> field.
    """

    schema = zope.component.getUtility(
        IDexterityFTI, name=context.portal_type
    ).lookupSchema()
    fields = dict((fieldname, schema[fieldname]) for fieldname in schema)

    assignable = IBehaviorAssignable(context)
    for behavior in assignable.enumerateBehaviors():
        behavior_schema = behavior.interface
        fields.update((name, behavior_schema[name]) for name in behavior_schema)

    return fields


def modified(event):
    """ get new/updated metadata"""

    obj = event.object
    if not IDexterityContent.providedBy(obj):
        return

    fields = get_all_fields(obj)
    data = dict()
    for f in fields:
        v = getattr(obj, f, None)
        if callable(v):
            v = v()
        if isinstance(v, RichTextValue):
            v = v.raw
        data[f] = v
    IPersistentLogger(obj).log("Metadata changed", details=data)


created = modified
