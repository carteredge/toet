import re
from django.shortcuts import render, reverse
from django.urls import path
from django.views import generic
from django.views.generic.edit import DeleteView
from .models import *

def index(request):
    return render(request, 'rpgcore/index.html')

def url_to_title(url):
    return ' '.join([f'{_[0].upper()}{_[1:]}' for _ in url.split('-')])

class BaseViews:
    breadcrumbs = []
    endpoints = ['create', 'delete', 'detail', 'list', 'update']
    fields = '__all__'
    model = None
    url_str = ''

    def get_any_success_url(self, view):
        if 'detail' in self.endpoints:
            return reverse(
                f'{self.url_str}-detail',
                kwargs={'pk': view.object.id})
        else:
            return reverse(f'{self.url_str}-list')

    def get_list_success_url(self):
            return reverse(f'{self.url_str}-list')

    def __init__(self):
        self.urls = []
        breadcrumbs = [{
            'url': f'{crumb}-list',
            'text': url_to_title(crumb)
            } for crumb in self.breadcrumbs] + \
                [{'url': f'{self.url_str}-list', 'text': url_to_title(self.url_str)}]
        if 'create' in self.endpoints:
            self.urls.append({
                'url': f'{self.url_str}/new/',
                'view': self.get_create_view_class(),
                'name': f'{self.url_str}-create',
                'extra_context': {
                    'breadcrumbs': breadcrumbs,
                    'title': f'New {self.get_title()}',
                },
            })

        if 'delete' in self.endpoints:
            self.urls.append({
                'url': f'{self.url_str}/<pk>/delete/',
                'view': self.get_delete_view_class(),
                'name': f'{self.url_str}-delete',
                'extra_context': {
                    'breadcrumbs': breadcrumbs,
                },
            })
        
        if 'detail' in self.endpoints:
            self.urls.append({
                'url': f'{self.url_str}/<pk>/',
                'view': self.get_detail_view_class(),
                'name': f'{self.url_str}-detail',
                'extra_context': {
                    'breadcrumbs': breadcrumbs,
                },
            })
        
        if 'list' in self.endpoints:
            self.urls.append({
                'url': f'{self.url_str}/',
                'view': self.get_list_view_class(),
                'name': f'{self.url_str}-list',
                'extra_context': {
                    'title': f'{self.get_title()}',
                    'breadcrumbs': breadcrumbs[:-1],
                    'create_url': f'{self.url_str}-create',
                    'delete_url': f'{self.url_str}-delete',
                    'detail_url': f'{self.url_str}-detail',
                    'update_url': f'{self.url_str}-update',
                },
            })
        
        if 'update' in self.endpoints:
            self.urls.append({
                'url': f'{self.url_str}/<pk>/edit/',
                'view': self.get_update_view_class(),
                'name': f'{self.url_str}-update',
                'extra_context': {
                    'breadcrumbs': breadcrumbs,
                },
            })
    
    def get_create_view_class(self):
        class CreateView(generic.CreateView):
            fields = self.fields
            endpoints = self.endpoints
            model = self.model
            template_name = 'rpgcore/generic_form.html'

            # # How to dynamically overload an inherited method in a class factory
            # # (which it turned out I didn't need):
            # def get_form(child, *args, **kwargs):
            #     get_form = getattr(self, 'get_form', None)
            #     if callable(get_form):
            #         return get_form(child, *args, **kwargs)
            #     else:
            #         return super(CreateView, child).get_form(*args, **kwargs)

            def get_initial(self):
                return self.request.GET
            
            def get_success_url(child):
                return self.get_any_success_url(child)

        return CreateView

    def get_delete_view_class(self):
        class DeleteView(generic.DeleteView):
            endpoints = self.endpoints
            model = self.model

            def get_success_url(child):
                return self.get_list_success_url()

        return DeleteView

    def get_detail_view_class(self):
        class DetailView(generic.DetailView):
            model = self.model
        return DetailView

    def get_extra_context(self, url_object):
        return {'title': url_object.get('title')}
    
    def get_list_view_class(self):
        class ListView(generic.ListView):
            model = self.model
            template_name = 'rpgcore/generic_list_with_links.html' \
                if 'detail' in self.endpoints else \
                    'rpgcore/generic_list.html'
        return ListView

    def get_paths(self):
        return [path(
            _.get('url'),
            _.get('view').as_view(
                extra_context=_.get('extra_context')),
            name=_.get('name')) for _ in self.urls]

    def get_title(self):
        title = re.sub('([a-z])([A-Z])', r'\1 \2', self.model.__name__)
        return f'{title[0].upper()}{title[1:]}'
    
    def get_update_view_class(self):
        class UpdateView(generic.UpdateView):
            endpoints = self.endpoints
            fields = self.fields
            model = self.model
            template_name = 'rpgcore/generic_form.html'
    
            def get_success_url(child):
                return self.get_any_success_url(child)

        return UpdateView

class ItemEffectViews(BaseViews):
    model = ItemEffect
    # default item via link?
    endpoints = ['create', 'delete', 'update']
    url_str = 'item-effects'


class ItemEffectTypeViews(BaseViews):
    breadcrumbs = ['items']
    model = ItemEffectType
    endpoints = ['create', 'delete', 'list', 'update']
    url_str = 'item-effect-types'


class ItemInstanceViews(BaseViews):
    breadcrumbs = ['items']
    model = ItemInstance
    url_str = 'item-instances'


class ItemPropertyViews(BaseViews):
    breadcrumbs = ['items']
    model = ItemProperty
    url_str = 'item-properties'


class ItemSpecialPropertyViews(BaseViews):
    breadcrumbs = ['items']
    model = ItemSpecialProperty
    url_str = 'item-special-properties'


class ItemTypeViews(BaseViews):
    breadcrumbs = ['items']
    model = ItemType
    endpoints = ['create', 'delete', 'list', 'update']
    url_str = 'item-types'


class ItemViews(BaseViews):
    model = Item
    fields = [
        'name',
        'type',
        'subtype',
        'is_equippable',
        'properties',
        'description']
    url_str = 'items'

