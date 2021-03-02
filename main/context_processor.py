from .models import Category

def get_categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    # categories = Category.objects.all()
    return {'categories': categories}