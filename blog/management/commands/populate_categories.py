from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand




class Command(BaseCommand):
    help = "this commands inserts category data"

    def handle(self, *args: Any, **options: Any):
        # delect existing data
        Category.objects.all().delete()

        categories = ['Design', 'Art', 'Daywear', 'Sheath', 'Wrap', 'Maxi', 'blazer', 'function']

        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))    