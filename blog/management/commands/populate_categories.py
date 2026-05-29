from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help = "this commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # delect existing data
        Category.objects.all().delete()

        categories = [
            "Fashion Design",
            "Sustainable Fashion",
            "Vintage Fashion",
            "Minimalist Fashion",
            "Streetwear Fashion",
            "Technology Fashion",
            "Textile Fashion",
            "Fashion Illustration",
            "Gender Neutral Fashion",
            "Luxury Fashion",
            "Color Psychology Fashion",
            "Fashion Branding",
            "Social Media Fashion",
            "Seasonal Fashion",
            "Haute Couture",
            "Cultural Fashion",
            "Upcycling Fashion",
            "Fashion Studio",
            "Fashion Accessories",
            "Digital Fashion",
            ]

        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))    