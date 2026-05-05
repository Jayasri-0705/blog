from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random




class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args: Any, **options: Any):
        # delect existing data
        Post.objects.all().delete()

        titles = [
            "The Fashion Design1",
            "Sustainable Fashion: Designing for a Greener Future",
            "The Evolution of Fashion Through the Decades",
            "Minimalism in Fashion Design",
            "Streetwear Culture and Its Influence on Modern Fashion",
            "The Role of Technology in Fashion Design",
            "Traditional Textiles in Contemporary Fashion",
            "Fashion Illustration: Bringing Ideas to Life",
            "Gender-Neutral Fashion: Breaking Stereotypes",
            "Luxury Fashion vs Fast Fashion",
            "The Psychology of Colors in Fashion Design",
            "Fashion Branding and Identity",
            "The Impact of Social Media on Fashion Trends",
            "Seasonal Fashion Trends: Spring/Summer vs Fall/Winter",
            "Haute Couture: The Art of High Fashion",
            "Fashion and Cultural Identity",
            "Upcycling in Fashion Design",
            "Fashion Design Process: From Concept to Creation",
            "Accessories in Fashion: Completing the Look",
            "Digital Fashion and Virtual Clothing",
        ]

        contents = [
            "Fashion design is the art of creating clothing and accessories that reflect style, culture, and functionality. Designers combine creativity with technical skills to produce garments that meet consumer needs. This field involves sketching, fabric selection, pattern making, and production. Fashion design constantly evolves with trends, making it a dynamic and innovative industry.",
            "Sustainable fashion focuses on reducing environmental damage caused by clothing production. Designers use eco-friendly fabrics, recycling techniques, and ethical labor practices. This approach encourages long-lasting garments instead of disposable fashion. By promoting awareness and responsibility, sustainable fashion helps protect natural resources and supports a healthier planet for future generations.",
            "Fashion has changed significantly across different decades, reflecting social, political, and cultural shifts. From the elegance of the 1920s to the bold styles of the 1980s and modern minimalism, each era has unique characteristics. Designers draw inspiration from past trends while adapting them to current preferences, keeping fashion both nostalgic and innovative.",
            "Minimalism in fashion emphasizes simplicity, clean lines, and neutral colors. Designers focus on creating versatile and timeless pieces that avoid unnecessary details. This approach promotes sustainability by encouraging fewer but higher-quality purchases. Minimalist fashion appeals to individuals who prefer elegance, functionality, and a clutter-free wardrobe.",
            "Streetwear originated from urban youth culture and has become a major influence in global fashion. It combines comfort with bold designs, including graphic prints and oversized silhouettes. Today, even luxury brands incorporate streetwear elements, showing how cultural expression and everyday style have shaped modern fashion trends.",
            "Technology plays a crucial role in modern fashion design by improving efficiency and creativity. Tools like computer-aided design (CAD), 3D modeling, and virtual fitting allow designers to experiment easily. Technology also supports online shopping and personalized recommendations, enhancing customer experience and transforming the fashion industry.",
            "Traditional textiles are being reintroduced into modern fashion to preserve cultural heritage. Designers combine traditional fabrics with contemporary styles to create unique garments. This fusion not only promotes craftsmanship but also brings global recognition to local artisans, helping sustain traditional textile industries.",
            "Fashion illustration is an essential part of the design process, where designers sketch their ideas before production. These drawings help visualize garments, colors, and details. Illustrations allow designers to communicate concepts clearly and make changes easily, ensuring better execution of the final product.",
            "Gender-neutral fashion removes the distinction between men’s and women’s clothing. Designers create outfits that focus on comfort, style, and inclusivity rather than gender norms. This movement promotes equality and allows individuals to express themselves freely without societal restrictions.",
            "Luxury fashion focuses on quality, exclusivity, and craftsmanship, while fast fashion emphasizes quick production and affordability. Although fast fashion makes trends accessible, it raises concerns about sustainability and ethics. Designers must find a balance between innovation, quality, and responsible production practices.",
            "Colors influence emotions and perceptions in fashion. Designers use color psychology to create moods and attract attention. For example, bright colors may represent energy, while neutral tones convey sophistication. Understanding color effects helps designers create impactful and meaningful designs.",
            "Fashion branding is essential for creating a unique identity in a competitive market. Designers use logos, storytelling, and visual elements to build strong brand recognition. A well-defined brand helps connect with customers emotionally and ensures long-term success.",
            "Social media platforms have revolutionized the fashion industry by spreading trends quickly. Influencers and designers showcase styles to global audiences instantly. This digital exposure increases competition and pushes designers to innovate constantly to stay relevant.",
            "Fashion trends vary by season, influencing fabrics, colors, and designs. Spring and summer collections focus on light fabrics and bright colors, while fall and winter emphasize warmth and darker tones. Designers plan collections according to seasonal demands and consumer preferences.",
            "Haute couture represents the highest level of fashion design, featuring custom-made garments crafted with precision. Designers focus on intricate details, luxurious fabrics, and exclusivity. These designs showcase creativity and craftsmanship, setting standards for the fashion industry.",
            "Fashion reflects cultural identity by incorporating traditional styles, patterns, and symbols. Designers use fashion to celebrate heritage and express diversity. This connection between fashion and culture helps preserve traditions while adapting them to modern styles.",
            "The fashion design process includes idea development, sketching, fabric selection, pattern making, and final production. Designers follow a structured approach to turn concepts into finished garments. Each step is important to ensure quality, functionality, and style.",
            "Accessories such as jewelry, bags, and shoes play an important role in enhancing outfits. Designers use accessories to add personality and detail to fashion. They help complete a look and make it more attractive and expressive.",
            "Digital fashion is an emerging trend where clothing is designed and worn virtually. It is used in gaming, social media, and virtual environments. Designers create digital outfits that reduce physical waste while offering new creative possibilities in the fashion industry.",
            
        ]

        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400",
            
        ]

        categories = Category.objects.all()

        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))    