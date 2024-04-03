from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Blog, Version


class ProductListView(ListView):
    """
    Отображает все продукты на главной странице сайта
    """
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        """
        Отображает только активные версии продукта
        """
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_active=True)
            if active_versions:
                product.active_version = active_versions.last().name
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data

    def get_queryset(self, *args, **kwargs):
        """
        Возвращает только опубликованные блоги
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publish=True)
        return queryset


class ProductDetailView(DetailView):
    """
    Отображает всю информацию о конкретном продукте
    """
    model = Product
    template_name = 'catalog/show_product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Создает новый продукт
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    login_url = 'users:login'

    def form_valid(self, form):
        """
        Привязывает продукт к создателю публикации
        """
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Реализует возможность редактирования продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    login_url = 'users:login'

    def form_valid(self, form):
        """
        Привязывает изменения к пользвателю
        """
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        """
        Вводит ограничение на изменения продукта
        """
        self.object = super().get_object(queryset)
        if (
                self.object.creator == self.request.user
                or self.request.user.is_superuser is True
                or self.request.user.groups.filter(name="moderator").exists() is True
        ):
            return self.object
        raise Http404

    def get_form_class(self):
        """
        Возвращает форму в зависимости от авторизованного на данный момент пользователя
        """
        user = self.request.user
        if user.is_superuser or self.object.creator == user:
            return ProductForm
        elif user.groups.filter(name="moderator").exists() is True:
            return ProductModeratorForm


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Реализует возможность удаления блога
    """
    model = Product
    success_url = reverse_lazy('product_list')
    login_url = 'users:login'


class ContactsTemplateView(TemplateView):
    """
    Отображает шаблон 'Контакты' при переводе на соответствующую страницу
    """
    template_name = 'catalog/contacts.html'


class BlogListView(ListView):
    """Отображает все блоги"""
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """
        Возвращает только опубликованные блоги
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset


class BlogDetailView(DetailView):
    """
    Отображает подробную информацию о конкретном блоге
    """
    model = Blog

    def get_object(self, queryset=None):
        """
        Считает количество просмотров определенного блога
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save(update_fields=['views_count'])
        return self.object


class BlogCreateView(CreateView):
    """
    Создает новый блог
    """
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        """
        Определяет человекочитаемый url
        """
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """
    Реализует возможность редактирования блога
    """
    model = Blog
    fields = ('title', 'content', 'preview',)

    def get_success_url(self):
        """
        Возвращает пользователя после редактирования блога на странцу просмотра блога
        """
        return reverse('blog_view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """
    Реализует возможность удаления блога
    """
    model = Blog
    success_url = reverse_lazy('blog_list')
