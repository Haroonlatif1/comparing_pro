from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ComparisonTable
from .forms import ComparisonTableForm

def home(request):
    return render(request, 'home.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comparison_tables = ComparisonTable.objects.filter(products=product)
    return render(request, 'product_detail.html', {'product': product, 'comparison_tables': comparison_tables})

def create_comparison_table(request):
    if request.method == 'POST':
        form = ComparisonTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=1)  # Redirect to a sample product for simplicity
    else:
        form = ComparisonTableForm()
    return render(request, 'create_comparison_table.html', {'form': form})
