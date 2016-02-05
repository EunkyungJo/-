from django.contrib import admin
from blog.models import Post, Member, Company, About_us, Comment, Tag


'''여기서 조건을 달리 설정하면서 포스팅 페이지의 커스텀이 가능'''


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_title_length']
    list_display_links = ['title']

    def get_title_length(self, post):
        return len(post.title)


admin.site.register(Post, PostAdmin)


class MembersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_name_length']
    list_display_links = ['name']

    def get_name_length(self, member):
        return len(member.name)


admin.site.register(Member, MembersAdmin)


class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_name_length']
    list_display_links = ['name']

    def get_name_length(self, company):
        return len(company.name)


admin.site.register(Company, CompaniesAdmin)


class About_us_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_name_length']
    list_display_links = ['name']

    def get_name_length(self, we):
        return len(we.name)

admin.site.register(About_us, About_us_Admin)


admin.site.register(Comment)


admin.site.register(Tag)
