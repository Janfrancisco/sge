import random
from datetime import datetime, timedelta

from django.utils.timezone import make_aware

from brands.models import Brand
from categories.models import Category
from inflows.models import Inflow
from outflows.models import Outflow
from products.models import Product
from suppliers.models import Supplier

# Categorias fictícias
categories = [
    "Bebidas",
    "Alimentos",
    "Higiene",
    "Limpeza",
    "Eletrônicos",
    "Roupas",
    "Brinquedos",
    "Papelaria",
    "Automotivo",
    "Móveis",
]

# Marcas reais de produtos no mercado brasileiro
brands = [
    "Nestlé",
    "Ambev",
    "Coca-Cola",
    "Unilever",
    "Procter & Gamble",
    "Pepsico",
    "Danone",
    "Colgate-Palmolive",
    "Kimberly-Clark",
    "Heineken",
]

# Fornecedores fictícios
suppliers = [
    "Distribuidora São Paulo",
    "Fornecedor Minas Gerais",
    "Atacadista Rio de Janeiro",
    "Distribuidora Sul",
    "Fornecedor Nordeste",
    "Atacadista Centro-Oeste",
    "Distribuidora Norte",
    "Fornecedor Internacional",
    "Atacadista Local",
    "Distribuidora Nacional",
]

# Produtos fictícios com base em marcas reais
products = [
    {
        "title": "Leite Ninho",
        "cost_price": 4.50,
        "selling_price": 6.00,
        "brand": "Nestlé",
        "category": "Alimentos",
    },
    {
        "title": "Guaraná Antarctica",
        "cost_price": 2.00,
        "selling_price": 3.50,
        "brand": "Ambev",
        "category": "Bebidas",
    },
    {
        "title": "Coca-Cola Lata",
        "cost_price": 2.50,
        "selling_price": 4.00,
        "brand": "Coca-Cola",
        "category": "Bebidas",
    },
    {
        "title": "Omo Multiação",
        "cost_price": 10.00,
        "selling_price": 15.00,
        "brand": "Unilever",
        "category": "Limpeza",
    },
    {
        "title": "Pampers Confort",
        "cost_price": 25.00,
        "selling_price": 35.00,
        "brand": "Procter & Gamble",
        "category": "Higiene",
    },
    {
        "title": "Doritos Queijo",
        "cost_price": 5.00,
        "selling_price": 8.00,
        "brand": "Pepsico",
        "category": "Alimentos",
    },
    {
        "title": "Danone Activia",
        "cost_price": 3.00,
        "selling_price": 5.00,
        "brand": "Danone",
        "category": "Alimentos",
    },
    {
        "title": "Colgate Total 12",
        "cost_price": 4.00,
        "selling_price": 6.50,
        "brand": "Colgate-Palmolive",
        "category": "Higiene",
    },
    {
        "title": "Neve Supreme",
        "cost_price": 8.00,
        "selling_price": 12.00,
        "brand": "Kimberly-Clark",
        "category": "Higiene",
    },
    {
        "title": "Heineken Long Neck",
        "cost_price": 3.50,
        "selling_price": 6.00,
        "brand": "Heineken",
        "category": "Bebidas",
    },
]


# Função para gerar datas aleatórias
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)  # egundos em um dia
    naive_datetime = start_date + timedelta(days=random_days, seconds=random_seconds)
    return make_aware(naive_datetime)


# Criar categorias no banco de dados
def create_categories():
    for category_name in categories:
        Category.objects.get_or_create(
            name=category_name, description=f"Categoria {category_name}"
        )


# Criar marcas no banco de dados
def create_brands():
    for brand_name in brands:
        Brand.objects.get_or_create(name=brand_name, description=f"Marca {brand_name}")


# Criar fornecedores no banco de dados
def create_suppliers():
    for supplier_name in suppliers:
        Supplier.objects.get_or_create(
            name=supplier_name, description=f"Fornecedor {supplier_name}"
        )


# Criar produtos no banco de dados
def create_products():
    for product in products:
        brand = Brand.objects.get(name=product["brand"])
        category = Category.objects.get(name=product["category"])
        Product.objects.get_or_create(
            title=product["title"],
            cost_price=product["cost_price"],
            selling_price=product["selling_price"],
            brand=brand,
            category=category,
            quantity=random.randint(10, 100),  # Quantidade aleatória
        )


# Criar entradas (Inflows) no banco de dados
def create_inflows():
    all_products = Product.objects.all()
    all_suppliers = Supplier.objects.all()
    for _ in range(50):  # Criar 50 entradas aleatórias
        product = random.choice(all_products)
        supplier = random.choice(all_suppliers)
        inflow = Inflow.objects.create(
            product=product,
            supplier=supplier,
            quantity=random.randint(5, 20),  # Quantidade aleatória
            description="Entrada de estoque",
        )
        inflow.created_at = random_date(datetime(2023, 1, 1), datetime(2025, 5, 1))
        inflow.save()


# Criar saídas (Outflows) no banco de dados
def create_outflows():
    all_products = Product.objects.all()
    for _ in range(50):  # Criar 50 saídas aleatórias
        product = random.choice(all_products)
        outflow = Outflow.objects.create(
            product=product,
            quantity=random.randint(1, 10),  # Quantidade aleatória
            description="Venda de produto",
        )
        outflow.created_at = random_date(datetime(2023, 1, 1), datetime(2025, 5, 1))
        outflow.save()


# Executar o script
def run():
    print("Criando categorias...")
    create_categories()
    print("Criando marcas...")
    create_brands()
    print("Criando fornecedores...")
    create_suppliers()
    print("Criando produtos...")
    create_products()
    print("Criando entradas (Inflows)...")
    create_inflows()
    print("Criando saídas (Outflows)...")
    create_outflows()
    print("Banco de dados populado com sucesso!")
