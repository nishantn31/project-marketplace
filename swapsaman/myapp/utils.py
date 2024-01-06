from django.utils.text import slugify
import uuid

def generate_slug(title:str) -> str:

    """
        A function to generate slug for Product model return str
    """

    from .models import Product
    title = slugify(title)

    while (Product.objects.filter(slug = title).exists()):
        title = f"{slugify(title)}-{str(uuid.uuid4())[:4]}"

    return title