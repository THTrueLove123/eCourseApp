from django.contrib import admin
from django.utils.html import mark_safe
from course.models import Category, Course, Lesson, Tag

admin.site.register(Category)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe('<img src="/static/{url}" width="120" />'\
                             .format(url=obj.image.name))

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    js = ('/static/js/script.js',)

admin.site.register(Course, CourseAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject','created_date', 'course']
    list_filter = ['subject', 'created_date']
    search_fields = ['subject', 'course__subject']

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    js = ('/static/js/script.js',)

admin.site.register(Lesson, LessonAdmin)

admin.site.register(Tag)
