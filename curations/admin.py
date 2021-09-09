from django.contrib import admin
from curations import models as CurationsModels
# Register your models here.

admin.site.register(CurationsModels.Curation)

admin.site.register(CurationsModels.Subject)
admin.site.register(CurationsModels.SubTopic)
admin.site.register(CurationsModels.Topic)
admin.site.register(CurationsModels.Link)
admin.site.register(CurationsModels.SubTopicLink)
