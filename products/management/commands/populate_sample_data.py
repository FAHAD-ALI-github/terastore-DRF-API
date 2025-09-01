# products/management/commands/populate_sample_data.py
from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Populate database with comprehensive electronics sample data'
    
    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            'electronics', 'mobile', 'laptop', 'audio', 'gaming',
            'tv', 'camera', 'tablet', 'smartwatch', 'accessories',
            'headphones', 'speakers', 'keyboard', 'mouse', 'monitor'
        ]
        
        categories = []
        for cat_name in categories_data:
            category, created = Category.objects.get_or_create(name=cat_name)
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {cat_name}')
        
        # Comprehensive products data
        sample_products = [
            # Mobile Phones
            {
                'title': 'iPhone 15 Pro Max 256GB',
                'price': 1199.99,
                'description': 'The most advanced iPhone with titanium design, A17 Pro chip, and professional camera system.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=500',
                'brand': 'Apple',
                'model': 'iPhone 15 Pro Max',
                'discount': 10
            },
            {
                'title': 'Samsung Galaxy S24 Ultra 512GB',
                'price': 1299.99,
                'description': 'Premium Android smartphone with S Pen, advanced AI features, and stunning camera capabilities.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=500',
                'brand': 'Samsung',
                'model': 'Galaxy S24 Ultra',
                'discount': 15
            },
            {
                'title': 'Google Pixel 8 Pro',
                'price': 999.99,
                'description': 'AI-powered smartphone with advanced computational photography and pure Android experience.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500',
                'brand': 'Google',
                'model': 'Pixel 8 Pro',
                'discount': 18
            },
            {
                'title': 'OnePlus 12 5G',
                'price': 799.99,
                'description': 'Flagship killer with Snapdragon 8 Gen 3, fast charging, and premium build quality.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?w=500',
                'brand': 'OnePlus',
                'model': 'OnePlus 12',
                'discount': 12
            },
            {
                'title': 'Xiaomi 14 Ultra',
                'price': 899.99,
                'description': 'Photography-focused smartphone with Leica cameras and flagship performance.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1601972599720-ad7cb6a938c0?w=500',
                'brand': 'Xiaomi',
                'model': 'Mi 14 Ultra',
                'discount': 20
            },
            
            # Laptops
            {
                'title': 'MacBook Pro 16-inch M3 Max',
                'price': 2499.99,
                'description': 'Powerful laptop with M3 Max chip, perfect for professional work and creative tasks.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500',
                'brand': 'Apple',
                'model': 'MacBook Pro 16',
                'discount': 8
            },
            {
                'title': 'Dell XPS 13 Intel i7',
                'price': 1399.99,
                'description': 'Ultra-portable laptop with stunning InfinityEdge display and premium build quality.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500',
                'brand': 'Dell',
                'model': 'XPS 13',
                'discount': 12
            },
            {
                'title': 'HP Spectre x360 14',
                'price': 1299.99,
                'description': '2-in-1 laptop with OLED display, premium design, and excellent battery life.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1484788984921-03950022c9ef?w=500',
                'brand': 'HP',
                'model': 'Spectre x360',
                'discount': 15
            },
            {
                'title': 'ASUS ROG Zephyrus G16',
                'price': 1899.99,
                'description': 'Gaming laptop with RTX 4080, Intel i9 processor, and 240Hz display.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'ASUS',
                'model': 'ROG Zephyrus G16',
                'discount': 10
            },
            {
                'title': 'Lenovo ThinkPad X1 Carbon',
                'price': 1599.99,
                'description': 'Business laptop with military-grade durability, excellent keyboard, and long battery life.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'brand': 'Lenovo',
                'model': 'ThinkPad X1',
                'discount': 8
            },
            {
                'title': 'Microsoft Surface Laptop Studio 2',
                'price': 1999.99,
                'description': 'Versatile laptop with unique hinge design, touchscreen, and Surface Pen support.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1629131726692-1accd0c53ce0?w=500',
                'brand': 'Microsoft',
                'model': 'Surface Studio 2',
                'discount': 12
            },
            
            # Audio Equipment
            {
                'title': 'Sony WH-1000XM5 Headphones',
                'price': 399.99,
                'description': 'Industry-leading noise canceling wireless headphones with premium sound quality.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500',
                'brand': 'Sony',
                'model': 'WH-1000XM5',
                'discount': 20
            },
            {
                'title': 'Bose QuietComfort Ultra',
                'price': 429.99,
                'description': 'Premium noise-canceling headphones with spatial audio and all-day comfort.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'Bose',
                'model': 'QC Ultra',
                'discount': 15
            },
            {
                'title': 'AirPods Pro 2nd Generation',
                'price': 249.99,
                'description': 'Advanced wireless earbuds with adaptive transparency and personalized spatial audio.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=500',
                'brand': 'Apple',
                'model': 'AirPods Pro 2',
                'discount': 10
            },
            {
                'title': 'JBL Charge 5 Portable Speaker',
                'price': 179.99,
                'description': 'Waterproof portable speaker with powerful bass and 20-hour battery life.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'JBL',
                'model': 'Charge 5',
                'discount': 25
            },
            {
                'title': 'Sonos Era 100 Smart Speaker',
                'price': 249.99,
                'description': 'Compact smart speaker with room-filling sound and voice control.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500',
                'brand': 'Sonos',
                'model': 'Era 100',
                'discount': 8
            },
            
            # Gaming
            {
                'title': 'PlayStation 5 Console',
                'price': 499.99,
                'description': 'Next-generation gaming console with ultra-high speed SSD and ray tracing.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500',
                'brand': 'Sony',
                'model': 'PlayStation 5',
                'discount': 5
            },
            {
                'title': 'Xbox Series X',
                'price': 499.99,
                'description': 'Powerful gaming console with 4K gaming, Quick Resume, and Game Pass.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=500',
                'brand': 'Microsoft',
                'model': 'Series X',
                'discount': 8
            },
            {
                'title': 'Nintendo Switch OLED',
                'price': 349.99,
                'description': 'Portable gaming console with vibrant OLED screen and versatile gameplay.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=500',
                'brand': 'Nintendo',
                'model': 'Switch OLED',
                'discount': 12
            },
            {
                'title': 'Steam Deck 512GB',
                'price': 649.99,
                'description': 'Handheld gaming PC with access to your entire Steam library.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500',
                'brand': 'Valve',
                'model': 'Steam Deck',
                'discount': 10
            },
            
            # Tablets
            {
                'title': 'iPad Pro 12.9-inch M2',
                'price': 1099.99,
                'description': 'Most advanced iPad with M2 chip, Liquid Retina XDR display, and Apple Pencil support.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'Apple',
                'model': 'iPad Pro 12.9',
                'discount': 7
            },
            {
                'title': 'Samsung Galaxy Tab S9 Ultra',
                'price': 1199.99,
                'description': 'Premium Android tablet with S Pen, large display, and productivity features.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=500',
                'brand': 'Samsung',
                'model': 'Tab S9 Ultra',
                'discount': 15
            },
            {
                'title': 'Microsoft Surface Pro 9',
                'price': 999.99,
                'description': '2-in-1 tablet with laptop performance, detachable keyboard, and Surface Pen.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'Microsoft',
                'model': 'Surface Pro 9',
                'discount': 12
            },
            
            # TVs
            {
                'title': 'Samsung 65" QLED 4K Smart TV',
                'price': 1799.99,
                'description': 'Premium QLED TV with quantum processor, HDR support, and smart TV features.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'Samsung',
                'model': 'QN65Q80C',
                'discount': 25
            },
            {
                'title': 'LG 77" OLED C3 4K TV',
                'price': 2499.99,
                'description': 'OLED TV with perfect blacks, Dolby Vision, and gaming features.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'LG',
                'model': 'OLED77C3',
                'discount': 20
            },
            {
                'title': 'Sony 65" Bravia XR A95L OLED',
                'price': 2799.99,
                'description': 'QD-OLED TV with cognitive processor and perfect for PlayStation 5.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'Sony',
                'model': 'XR-65A95L',
                'discount': 18
            },
            
            # Cameras
            {
                'title': 'Canon EOS R5 Mirrorless Camera',
                'price': 3899.99,
                'description': 'Professional mirrorless camera with 45MP sensor and 8K video recording.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Canon',
                'model': 'EOS R5',
                'discount': 10
            },
            {
                'title': 'Sony Alpha a7R V',
                'price': 3899.99,
                'description': 'High-resolution mirrorless camera with 61MP sensor and advanced autofocus.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Sony',
                'model': 'Alpha a7R V',
                'discount': 12
            },
            {
                'title': 'Nikon Z9 Professional Camera',
                'price': 5499.99,
                'description': 'Professional mirrorless camera with 45.7MP sensor and 8K video.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Nikon',
                'model': 'Z9',
                'discount': 8
            },
            
            # Smartwatches
            {
                'title': 'Apple Watch Series 9 GPS',
                'price': 399.99,
                'description': 'Advanced smartwatch with health monitoring, fitness tracking, and cellular connectivity.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Apple',
                'model': 'Watch Series 9',
                'discount': 12
            },
            {
                'title': 'Samsung Galaxy Watch 6 Classic',
                'price': 429.99,
                'description': 'Premium smartwatch with rotating bezel, health sensors, and Wear OS.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Samsung',
                'model': 'Galaxy Watch 6',
                'discount': 15
            },
            {
                'title': 'Garmin Fenix 7X Sapphire Solar',
                'price': 799.99,
                'description': 'Rugged GPS smartwatch with solar charging and adventure-ready features.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Garmin',
                'model': 'Fenix 7X',
                'discount': 10
            },
            
            # Keyboards & Mice
            {
                'title': 'Logitech MX Master 3S Wireless Mouse',
                'price': 99.99,
                'description': 'Advanced wireless mouse with precision scrolling and customizable buttons.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'Logitech',
                'model': 'MX Master 3S',
                'discount': 20
            },
            {
                'title': 'Corsair K95 RGB Platinum XT',
                'price': 199.99,
                'description': 'Premium mechanical gaming keyboard with Cherry MX switches and RGB lighting.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Corsair',
                'model': 'K95 RGB XT',
                'discount': 15
            },
            {
                'title': 'Razer DeathAdder V3 Pro',
                'price': 149.99,
                'description': 'Wireless gaming mouse with Focus Pro 30K sensor and 90-hour battery.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'Razer',
                'model': 'DeathAdder V3 Pro',
                'discount': 18
            },
            
            # Monitors
            {
                'title': 'LG 27" 4K UltraFine Monitor',
                'price': 699.99,
                'description': '4K IPS monitor with USB-C connectivity and color-accurate display.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'LG',
                'model': '27UP850',
                'discount': 22
            },
            {
                'title': 'Dell Alienware AW3423DWF 34" OLED',
                'price': 1099.99,
                'description': 'Curved OLED gaming monitor with 175Hz refresh rate and G-Sync Compatible.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'Dell',
                'model': 'AW3423DWF',
                'discount': 12
            },
            
            # Additional Mobile Phones (20 more)
            {
                'title': 'iPhone 14 Pro 128GB',
                'price': 999.99,
                'description': 'Powerful iPhone with A16 Bionic chip, Dynamic Island, and Pro camera system.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=500',
                'brand': 'Apple',
                'model': 'iPhone 14 Pro',
                'discount': 15
            },
            {
                'title': 'Samsung Galaxy Z Fold 5',
                'price': 1799.99,
                'description': 'Foldable smartphone with large inner display and multitasking capabilities.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=500',
                'brand': 'Samsung',
                'model': 'Galaxy Z Fold 5',
                'discount': 20
            },
            {
                'title': 'Nothing Phone 2',
                'price': 599.99,
                'description': 'Unique transparent design with Glyph interface and clean Android experience.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500',
                'brand': 'Nothing',
                'model': 'Phone 2',
                'discount': 22
            },
            {
                'title': 'Huawei Mate 60 Pro',
                'price': 1199.99,
                'description': 'Premium smartphone with advanced photography and satellite communication.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?w=500',
                'brand': 'Huawei',
                'model': 'Mate 60 Pro',
                'discount': 18
            },
            {
                'title': 'Realme GT 3 240W',
                'price': 649.99,
                'description': 'Fast-charging smartphone with Snapdragon 8+ Gen 1 and 240W charging.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1601972599720-ad7cb6a938c0?w=500',
                'brand': 'Realme',
                'model': 'GT 3',
                'discount': 25
            },
            {
                'title': 'OPPO Find X6 Pro',
                'price': 1099.99,
                'description': 'Flagship smartphone with Hasselblad cameras and premium design.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500',
                'brand': 'OPPO',
                'model': 'Find X6 Pro',
                'discount': 16
            },
            {
                'title': 'Vivo X90 Pro Plus',
                'price': 999.99,
                'description': 'Photography-focused smartphone with Zeiss optics and fast performance.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?w=500',
                'brand': 'Vivo',
                'model': 'X90 Pro+',
                'discount': 20
            },
            {
                'title': 'Honor Magic 5 Pro',
                'price': 899.99,
                'description': 'Premium smartphone with advanced AI features and flagship performance.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1601972599720-ad7cb6a938c0?w=500',
                'brand': 'Honor',
                'model': 'Magic 5 Pro',
                'discount': 18
            },
            {
                'title': 'Motorola Edge 40 Pro',
                'price': 699.99,
                'description': 'Edge-to-edge display smartphone with clean Android and fast charging.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500',
                'brand': 'Motorola',
                'model': 'Edge 40 Pro',
                'discount': 22
            },
            {
                'title': 'Asus ROG Phone 7 Ultimate',
                'price': 1399.99,
                'description': 'Gaming smartphone with Snapdragon 8 Gen 2, advanced cooling, and 165Hz display.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?w=500',
                'brand': 'ASUS',
                'model': 'ROG Phone 7',
                'discount': 12
            },
            
            # More Laptops (15 more)
            {
                'title': 'MacBook Air 15-inch M2',
                'price': 1299.99,
                'description': 'Larger MacBook Air with M2 chip, all-day battery, and fanless design.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500',
                'brand': 'Apple',
                'model': 'MacBook Air 15',
                'discount': 10
            },
            {
                'title': 'Framework Laptop 13',
                'price': 1099.99,
                'description': 'Modular laptop with upgradeable ports, repairable design, and sustainable approach.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500',
                'brand': 'Framework',
                'model': 'Laptop 13',
                'discount': 8
            },
            {
                'title': 'Acer Predator Helios 16',
                'price': 1599.99,
                'description': 'Gaming laptop with RTX 4070, Intel i7, and advanced cooling system.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'Acer',
                'model': 'Predator Helios 16',
                'discount': 15
            },
            {
                'title': 'MSI Creator Z17 HX Studio',
                'price': 2199.99,
                'description': 'Creator laptop with RTX 4080, color-accurate display, and professional features.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'brand': 'MSI',
                'model': 'Creator Z17 HX',
                'discount': 12
            },
            {
                'title': 'Alienware x17 R2',
                'price': 2999.99,
                'description': 'High-performance gaming laptop with RTX 4090 and premium build quality.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'Alienware',
                'model': 'x17 R2',
                'discount': 10
            },
            {
                'title': 'ASUS ZenBook Pro 16X OLED',
                'price': 1999.99,
                'description': 'Creator laptop with OLED touchscreen, RTX 4060, and professional features.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'brand': 'ASUS',
                'model': 'ZenBook Pro 16X',
                'discount': 14
            },
            {
                'title': 'Razer Blade 15 Advanced',
                'price': 2399.99,
                'description': 'Premium gaming laptop with RTX 4070, QHD 240Hz display, and sleek design.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'Razer',
                'model': 'Blade 15',
                'discount': 16
            },
            {
                'title': 'System76 Oryx Pro',
                'price': 1899.99,
                'description': 'Linux laptop with open-source firmware, powerful specs, and privacy focus.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500',
                'brand': 'System76',
                'model': 'Oryx Pro',
                'discount': 12
            },
            
            # Audio Equipment (25 more)
            {
                'title': 'Sennheiser HD 800 S',
                'price': 1699.99,
                'description': 'Reference-class open-back headphones for audiophiles and professionals.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500',
                'brand': 'Sennheiser',
                'model': 'HD 800 S',
                'discount': 8
            },
            {
                'title': 'Focal Stellia Closed-Back',
                'price': 2999.99,
                'description': 'Luxury closed-back headphones with beryllium drivers and premium materials.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'Focal',
                'model': 'Stellia',
                'discount': 10
            },
            {
                'title': 'Audio-Technica ATH-M50xBT2',
                'price': 199.99,
                'description': 'Professional wireless headphones with studio-quality sound and 50-hour battery.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'Audio-Technica',
                'model': 'ATH-M50xBT2',
                'discount': 25
            },
            {
                'title': 'Marshall Acton III Bluetooth Speaker',
                'price': 279.99,
                'description': 'Iconic rock-inspired speaker with Marshall signature sound and vintage design.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'Marshall',
                'model': 'Acton III',
                'discount': 20
            },
            {
                'title': 'Bang & Olufsen Beoplay HX',
                'price': 499.99,
                'description': 'Luxury wireless headphones with adaptive ANC and premium materials.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'Bang & Olufsen',
                'model': 'Beoplay HX',
                'discount': 12
            },
            {
                'title': 'KEF LS50 Meta Bookshelf Speakers',
                'price': 1599.99,
                'description': 'Award-winning bookshelf speakers with Metamaterial Absorption Technology.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'KEF',
                'model': 'LS50 Meta',
                'discount': 15
            },
            {
                'title': 'Beats Studio Pro',
                'price': 349.99,
                'description': 'Wireless noise-canceling headphones with personalized spatial audio.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500',
                'brand': 'Beats',
                'model': 'Studio Pro',
                'discount': 18
            },
            {
                'title': 'SteelSeries Arctis Nova Pro Wireless',
                'price': 349.99,
                'description': 'Premium gaming headset with dual wireless connectivity and Hi-Res audio.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'SteelSeries',
                'model': 'Arctis Nova Pro',
                'discount': 20
            },
            
            # Gaming Accessories & Consoles (15 more)
            {
                'title': 'Xbox Wireless Controller Elite Series 2',
                'price': 179.99,
                'description': 'Professional gaming controller with adjustable tension thumbsticks and paddle customization.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500',
                'brand': 'Microsoft',
                'model': 'Elite Series 2',
                'discount': 15
            },
            {
                'title': 'NVIDIA RTX 4090 Graphics Card',
                'price': 1599.99,
                'description': 'Flagship graphics card with 4th Gen RT Cores and 3rd Gen RT Cores for ultimate gaming.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500',
                'brand': 'NVIDIA',
                'model': 'RTX 4090',
                'discount': 8
            },
            {
                'title': 'AMD Radeon RX 7900 XTX',
                'price': 999.99,
                'description': 'High-performance graphics card with RDNA 3 architecture and 24GB VRAM.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500',
                'brand': 'AMD',
                'model': 'RX 7900 XTX',
                'discount': 12
            },
            {
                'title': 'Logitech G Pro X Superlight 2',
                'price': 159.99,
                'description': 'Ultra-lightweight gaming mouse with HERO 25K sensor and 95-hour battery.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'Logitech',
                'model': 'G Pro X Superlight 2',
                'discount': 20
            },
            {
                'title': 'Razer Huntsman V3 Pro TKL',
                'price': 249.99,
                'description': 'Tenkeyless gaming keyboard with analog optical switches and 8000Hz polling.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Razer',
                'model': 'Huntsman V3 Pro',
                'discount': 18
            },
            
            # Monitors (15 more)
            {
                'title': 'Samsung Odyssey OLED G9 49"',
                'price': 1799.99,
                'description': 'Ultra-wide curved OLED gaming monitor with 240Hz refresh rate and HDR.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'Samsung',
                'model': 'Odyssey OLED G9',
                'discount': 22
            },
            {
                'title': 'ASUS ProArt Display PA278CV',
                'price': 329.99,
                'description': '27-inch 4K monitor with 100% sRGB, USB-C connectivity, and factory calibration.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'ASUS',
                'model': 'ProArt PA278CV',
                'discount': 25
            },
            {
                'title': 'BenQ SW321C PhotoVue 32"',
                'price': 1999.99,
                'description': 'Professional 4K monitor for photographers with hardware calibration and wide color gamut.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'BenQ',
                'model': 'SW321C',
                'discount': 10
            },
            {
                'title': 'LG UltraGear 27GP950-B',
                'price': 799.99,
                'description': '4K gaming monitor with 160Hz, HDMI 2.1, and G-Sync Compatible.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'LG',
                'model': '27GP950-B',
                'discount': 18
            },
            {
                'title': 'Apple Studio Display 27"',
                'price': 1599.99,
                'description': '5K Retina display with A13 Bionic chip, Center Stage camera, and spatial audio.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'Apple',
                'model': 'Studio Display',
                'discount': 5
            },
            
            # Tablets & E-readers (10 more)
            {
                'title': 'iPad Air 5th Generation',
                'price': 599.99,
                'description': 'Versatile iPad with M1 chip, 10.9-inch display, and Apple Pencil support.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'Apple',
                'model': 'iPad Air 5',
                'discount': 12
            },
            {
                'title': 'Samsung Galaxy Tab A9+ 5G',
                'price': 329.99,
                'description': 'Affordable Android tablet with large display and 5G connectivity.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=500',
                'brand': 'Samsung',
                'model': 'Tab A9+',
                'discount': 20
            },
            {
                'title': 'Microsoft Surface Go 3',
                'price': 399.99,
                'description': 'Portable 2-in-1 tablet perfect for students and light productivity tasks.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'Microsoft',
                'model': 'Surface Go 3',
                'discount': 15
            },
            {
                'title': 'Amazon Kindle Scribe',
                'price': 339.99,
                'description': 'Large e-reader with stylus support for reading and note-taking.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'Amazon',
                'model': 'Kindle Scribe',
                'discount': 18
            },
            
            # Smart Home & Electronics (20 more)
            {
                'title': 'Amazon Echo Studio Smart Speaker',
                'price': 199.99,
                'description': 'Hi-Fi smart speaker with 3D audio, Alexa built-in, and smart home hub.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500',
                'brand': 'Amazon',
                'model': 'Echo Studio',
                'discount': 30
            },
            {
                'title': 'Google Nest Hub Max',
                'price': 229.99,
                'description': 'Smart display with Google Assistant, video calling, and smart home control.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Google',
                'model': 'Nest Hub Max',
                'discount': 25
            },
            {
                'title': 'Ring Video Doorbell Pro 2',
                'price': 279.99,
                'description': 'Advanced video doorbell with 1536p HD video, 3D motion detection, and two-way talk.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Ring',
                'model': 'Video Doorbell Pro 2',
                'discount': 20
            },
            {
                'title': 'Philips Hue Play HDMI Sync Box',
                'price': 229.99,
                'description': 'Sync your entertainment to Philips Hue lights for immersive lighting experience.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Philips',
                'model': 'Hue Play Sync Box',
                'discount': 15
            },
            {
                'title': 'Tesla Model S Plaid Onboard Computer',
                'price': 2999.99,
                'description': 'Advanced vehicle computer system with gaming capabilities and neural net processing.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Tesla',
                'model': 'Model S Computer',
                'discount': 5
            },
            
            # More Audio Products
            {
                'title': 'Sony WF-1000XM4 Earbuds',
                'price': 279.99,
                'description': 'Premium noise-canceling earbuds with LDAC codec and long battery life.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=500',
                'brand': 'Sony',
                'model': 'WF-1000XM4',
                'discount': 22
            },
            {
                'title': 'Jabra Elite 85h Headphones',
                'price': 249.99,
                'description': 'Smart wireless headphones with SmartSound technology and 36-hour battery.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'Jabra',
                'model': 'Elite 85h',
                'discount': 28
            },
            {
                'title': 'Shure SM7B Microphone',
                'price': 399.99,
                'description': 'Professional broadcast microphone used by podcasters and musicians worldwide.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'brand': 'Shure',
                'model': 'SM7B',
                'discount': 10
            },
            {
                'title': 'Audio-Technica AT2020USB+ Microphone',
                'price': 169.99,
                'description': 'USB condenser microphone perfect for home recording and streaming.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'brand': 'Audio-Technica',
                'model': 'AT2020USB+',
                'discount': 15
            },
            {
                'title': 'Yamaha HS8 Studio Monitor',
                'price': 369.99,
                'description': 'Professional studio monitor with accurate sound reproduction and bi-amp design.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'Yamaha',
                'model': 'HS8',
                'discount': 12
            },
            
            # Camera Equipment (15 more)
            {
                'title': 'Canon EOS R6 Mark II',
                'price': 2499.99,
                'description': 'Full-frame mirrorless camera with dual pixel autofocus and 4K 60p video.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Canon',
                'model': 'EOS R6 II',
                'discount': 12
            },
            {
                'title': 'Fujifilm X-T5',
                'price': 1699.99,
                'description': 'APS-C mirrorless camera with 40MP sensor and classic film simulation modes.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Fujifilm',
                'model': 'X-T5',
                'discount': 15
            },
            {
                'title': 'Leica Q2 Monochrom',
                'price': 4995.99,
                'description': 'Full-frame compact camera dedicated to black and white photography.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Leica',
                'model': 'Q2 Monochrom',
                'discount': 5
            },
            {
                'title': 'DJI Mavic 3 Pro Drone',
                'price': 2199.99,
                'description': 'Professional drone with Hasselblad camera, 43-minute flight time, and obstacle avoidance.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=500',
                'brand': 'DJI',
                'model': 'Mavic 3 Pro',
                'discount': 18
            },
            {
                'title': 'GoPro Hero 12 Black',
                'price': 399.99,
                'description': 'Rugged action camera with 5.3K video, HyperSmooth stabilization, and waterproof design.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=500',
                'brand': 'GoPro',
                'model': 'Hero 12 Black',
                'discount': 20
            },
            
            # More Electronics & Accessories (30 more)
            {
                'title': 'Anker PowerCore 26800 Power Bank',
                'price': 79.99,
                'description': 'High-capacity portable charger with fast charging for multiple devices.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1609592807107-e818ec901b37?w=500',
                'brand': 'Anker',
                'model': 'PowerCore 26800',
                'discount': 30
            },
            {
                'title': 'Apple MagSafe Charger',
                'price': 39.99,
                'description': 'Wireless charger with magnetic alignment for iPhone 12 and later models.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1609592807107-e818ec901b37?w=500',
                'brand': 'Apple',
                'model': 'MagSafe Charger',
                'discount': 15
            },
            {
                'title': 'Samsung T7 Shield 2TB SSD',
                'price': 199.99,
                'description': 'Rugged portable SSD with USB 3.2 Gen 2 and IP65 water resistance.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Samsung',
                'model': 'T7 Shield',
                'discount': 25
            },
            {
                'title': 'Belkin 3-in-1 Wireless Charger',
                'price': 149.99,
                'description': 'MagSafe compatible charger for iPhone, Apple Watch, and AirPods simultaneously.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1609592807107-e818ec901b37?w=500',
                'brand': 'Belkin',
                'model': '3-in-1 MagSafe',
                'discount': 20
            },
            {
                'title': 'Logitech MX Keys S Keyboard',
                'price': 109.99,
                'description': 'Wireless keyboard with smart illumination, comfortable typing, and multi-device support.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Logitech',
                'model': 'MX Keys S',
                'discount': 18
            },
            {
                'title': 'Keychron K8 Wireless Mechanical',
                'price': 89.99,
                'description': 'Hot-swappable mechanical keyboard with RGB backlighting and wireless connectivity.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Keychron',
                'model': 'K8',
                'discount': 22
            },
            {
                'title': 'SteelSeries Rival 650 Wireless',
                'price': 99.99,
                'description': 'Dual sensor gaming mouse with weight customization and fast wireless.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'SteelSeries',
                'model': 'Rival 650',
                'discount': 25
            },
            {
                'title': 'ASUS TUF Gaming VG27AQ',
                'price': 329.99,
                'description': '27-inch 1440p gaming monitor with 165Hz, G-Sync, and HDR support.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'ASUS',
                'model': 'VG27AQ',
                'discount': 28
            },
            {
                'title': 'Acer Nitro XV272U KV',
                'price': 299.99,
                'description': '27-inch 1440p IPS gaming monitor with 170Hz refresh rate and FreeSync.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'Acer',
                'model': 'Nitro XV272U',
                'discount': 30
            },
            
            # More TVs (10 more)
            {
                'title': 'TCL 55" C845 Mini LED 4K TV',
                'price': 899.99,
                'description': 'Mini LED TV with quantum dots, 144Hz VRR, and Google TV smart platform.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'TCL',
                'model': '55C845',
                'discount': 35
            },
            {
                'title': 'Hisense 65" U8K ULED 4K TV',
                'price': 1199.99,
                'description': 'ULED TV with Mini LED backlighting, Dolby Vision, and 144Hz gaming mode.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'Hisense',
                'model': 'U8K',
                'discount': 28
            },
            {
                'title': 'Roku Ultra 4K Streaming Device',
                'price': 99.99,
                'description': 'Premium streaming device with Dolby Vision, voice remote, and private listening.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'Roku',
                'model': 'Ultra',
                'discount': 20
            },
            {
                'title': 'Apple TV 4K 3rd Generation',
                'price': 179.99,
                'description': 'Streaming device with A15 Bionic chip, Dolby Vision, and Siri Remote.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'Apple',
                'model': 'Apple TV 4K',
                'discount': 12
            },
            {
                'title': 'NVIDIA Shield TV Pro',
                'price': 199.99,
                'description': 'Android TV streaming device with AI upscaling and GeForce NOW gaming.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'NVIDIA',
                'model': 'Shield TV Pro',
                'discount': 15
            },
            
            # More Mobile Devices (15 more)
            {
                'title': 'iPhone 13 Mini 128GB',
                'price': 629.99,
                'description': 'Compact iPhone with A15 Bionic chip, dual cameras, and all-day battery.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=500',
                'brand': 'Apple',
                'model': 'iPhone 13 Mini',
                'discount': 25
            },
            {
                'title': 'Samsung Galaxy A54 5G',
                'price': 449.99,
                'description': 'Mid-range smartphone with 50MP triple camera and 5000mAh battery.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1574944985070-8f3ebc6b79d2?w=500',
                'brand': 'Samsung',
                'model': 'Galaxy A54',
                'discount': 20
            },
            {
                'title': 'Google Pixel 7a',
                'price': 499.99,
                'description': 'Affordable Pixel with Tensor G2 chip, computational photography, and clean Android.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500',
                'brand': 'Google',
                'model': 'Pixel 7a',
                'discount': 15
            },
            {
                'title': 'OnePlus Nord 3 5G',
                'price': 399.99,
                'description': 'Mid-range smartphone with flagship features, 80W fast charging, and premium design.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1580910051074-3eb694886505?w=500',
                'brand': 'OnePlus',
                'model': 'Nord 3',
                'discount': 18
            },
            {
                'title': 'Xiaomi Redmi Note 12 Pro',
                'price': 329.99,
                'description': 'Budget-friendly smartphone with 50MP camera, 120Hz AMOLED, and fast charging.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1601972599720-ad7cb6a938c0?w=500',
                'brand': 'Xiaomi',
                'model': 'Redmi Note 12 Pro',
                'discount': 30
            },
            {
                'title': 'Poco F5 Pro 5G',
                'price': 579.99,
                'description': 'Performance smartphone with Snapdragon 8+ Gen 1 and 67W wireless charging.',
                'category': 'mobile',
                'image': 'https://images.unsplash.com/photo-1601972599720-ad7cb6a938c0?w=500',
                'brand': 'Poco',
                'model': 'F5 Pro',
                'discount': 25
            },
            
            # More Gaming Products (20 more)
            {
                'title': 'Razer Blade Pro 17',
                'price': 2799.99,
                'description': 'Large gaming laptop with RTX 4080, Intel i9, and premium build quality.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'Razer',
                'model': 'Blade Pro 17',
                'discount': 10
            },
            {
                'title': 'ASUS ROG Ally Handheld',
                'price': 699.99,
                'description': 'Windows handheld gaming device with AMD Z1 Extreme and 120Hz display.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500',
                'brand': 'ASUS',
                'model': 'ROG Ally',
                'discount': 15
            },
            {
                'title': 'Corsair K100 RGB Optical',
                'price': 229.99,
                'description': 'Premium gaming keyboard with optical switches, iCUE RGB, and aluminum frame.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Corsair',
                'model': 'K100 RGB',
                'discount': 20
            },
            {
                'title': 'HyperX Cloud Alpha Wireless',
                'price': 199.99,
                'description': 'Gaming headset with 300-hour battery life and crystal-clear audio.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'HyperX',
                'model': 'Cloud Alpha Wireless',
                'discount': 22
            },
            {
                'title': 'Elgato Stream Deck XL',
                'price': 249.99,
                'description': '32-key stream deck with customizable LCD keys for content creators.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Elgato',
                'model': 'Stream Deck XL',
                'discount': 18
            },
            {
                'title': 'Blue Yeti Blackout Microphone',
                'price': 99.99,
                'description': 'Professional USB microphone with multiple pickup patterns for streaming and podcasting.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'brand': 'Blue',
                'model': 'Yeti Blackout',
                'discount': 35
            },
            
            # More Electronics & Smart Devices
            {
                'title': 'Nest Thermostat 4th Gen',
                'price': 129.99,
                'description': 'Smart thermostat that learns your schedule and saves energy automatically.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Google',
                'model': 'Nest Thermostat',
                'discount': 20
            },
            {
                'title': 'Arlo Pro 5S Security Camera',
                'price': 249.99,
                'description': 'Wireless security camera with 2K video, color night vision, and smart detection.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Arlo',
                'model': 'Pro 5S',
                'discount': 25
            },
            {
                'title': 'Sonos Beam Gen 2 Soundbar',
                'price': 449.99,
                'description': 'Compact smart soundbar with Dolby Atmos and voice control support.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'Sonos',
                'model': 'Beam Gen 2',
                'discount': 18
            },
            {
                'title': 'Bose SoundLink Max Portable',
                'price': 399.99,
                'description': 'Premium portable speaker with powerful bass and 20-hour battery life.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'Bose',
                'model': 'SoundLink Max',
                'discount': 20
            },
            {
                'title': 'Ultimate Ears MEGABOOM 4',
                'price': 199.99,
                'description': '360-degree wireless speaker with waterproof design and powerful sound.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'Ultimate Ears',
                'model': 'MEGABOOM 4',
                'discount': 30
            },
            
            # More Accessories & Peripherals
            {
                'title': 'CalDigit TS4 Thunderbolt 4 Dock',
                'price': 379.99,
                'description': 'Professional Thunderbolt 4 dock with 18 ports for ultimate connectivity.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'CalDigit',
                'model': 'TS4',
                'discount': 12
            },
            {
                'title': 'Anker PowerExpand Elite 13-in-1',
                'price': 199.99,
                'description': 'Thunderbolt 4 hub with multiple ports, 4K dual monitor support, and 85W charging.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Anker',
                'model': 'PowerExpand Elite',
                'discount': 25
            },
            {
                'title': 'Peak Design Everyday Backpack V2',
                'price': 279.99,
                'description': 'Camera and laptop backpack with modular design and weatherproof construction.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500',
                'brand': 'Peak Design',
                'model': 'Everyday V2',
                'discount': 15
            },
            {
                'title': 'Bellroy Leather Phone Case iPhone 15',
                'price': 45.99,
                'description': 'Premium leather phone case with card storage and environmental leather.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1609592807107-e818ec901b37?w=500',
                'brand': 'Bellroy',
                'model': 'Leather Case',
                'discount': 20
            },
            {
                'title': 'Lamicall Adjustable Phone Stand',
                'price': 15.99,
                'description': 'Aluminum phone stand with adjustable angle for desk use and video calls.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1609592807107-e818ec901b37?w=500',
                'brand': 'Lamicall',
                'model': 'Phone Stand',
                'discount': 40
            },
            
            # More Gaming & Keyboards/Mice
            {
                'title': 'Glorious Model O 2 Wireless',
                'price': 79.99,
                'description': 'Ultra-lightweight gaming mouse with honeycomb shell and 80-hour battery.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'Glorious',
                'model': 'Model O 2',
                'discount': 25
            },
            {
                'title': 'Finalmouse Starlight-12 Phantom',
                'price': 189.99,
                'description': 'Ultra-premium lightweight gaming mouse with magnesium alloy construction.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'Finalmouse',
                'model': 'Starlight-12',
                'discount': 10
            },
            {
                'title': 'Wooting 60HE+ Keyboard',
                'price': 199.99,
                'description': 'Analog mechanical keyboard with adjustable actuation points and rapid trigger.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Wooting',
                'model': '60HE+',
                'discount': 15
            },
            {
                'title': 'SteelSeries Apex Pro TKL',
                'price': 189.99,
                'description': 'Mechanical gaming keyboard with adjustable switches and OLED smart display.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'SteelSeries',
                'model': 'Apex Pro TKL',
                'discount': 22
            },
            {
                'title': 'Ducky One 3 Mechanical Keyboard',
                'price': 139.99,
                'description': 'Premium mechanical keyboard with Cherry MX switches and double-shot keycaps.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Ducky',
                'model': 'One 3',
                'discount': 18
            },
            
            # High-End Audio Equipment
            {
                'title': 'Audeze LCD-X Headphones',
                'price': 1199.99,
                'description': 'Planar magnetic headphones with reference-quality sound for professionals.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500',
                'brand': 'Audeze',
                'model': 'LCD-X',
                'discount': 12
            },
            {
                'title': 'Beyerdynamic DT 1990 Pro',
                'price': 579.99,
                'description': 'Open-back studio headphones with Tesla drivers and analytical sound signature.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'Beyerdynamic',
                'model': 'DT 1990 Pro',
                'discount': 15
            },
            {
                'title': 'FiiO M17 Portable Music Player',
                'price': 1799.99,
                'description': 'High-end DAP with dual ES9038PRO DACs, Android 10, and premium audio output.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500',
                'brand': 'FiiO',
                'model': 'M17',
                'discount': 10
            },
            {
                'title': 'Chord Mojo 2 DAC/Amp',
                'price': 569.99,
                'description': 'Portable DAC and headphone amplifier with ultra-high resolution audio.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Chord',
                'model': 'Mojo 2',
                'discount': 8
            },
            
            # More Tablets & E-readers
            {
                'title': 'iPad Mini 6th Generation',
                'price': 499.99,
                'description': 'Compact iPad with A15 Bionic chip, USB-C, and Apple Pencil support.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'Apple',
                'model': 'iPad Mini 6',
                'discount': 15
            },
            {
                'title': 'Amazon Fire Max 11 Tablet',
                'price': 229.99,
                'description': 'Large Android tablet with productivity features and long battery life.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=500',
                'brand': 'Amazon',
                'model': 'Fire Max 11',
                'discount': 30
            },
            {
                'title': 'Lenovo Tab P12 Pro',
                'price': 599.99,
                'description': 'Premium Android tablet with OLED display, keyboard support, and stylus.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=500',
                'brand': 'Lenovo',
                'model': 'Tab P12 Pro',
                'discount': 20
            },
            {
                'title': 'reMarkable 2 Paper Tablet',
                'price': 399.99,
                'description': 'Digital paper tablet for note-taking with paper-like writing experience.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'reMarkable',
                'model': 'reMarkable 2',
                'discount': 12
            },
            
            # More Smartwatches & Wearables
            {
                'title': 'Fitbit Sense 2 Health Smartwatch',
                'price': 299.99,
                'description': 'Advanced health smartwatch with stress management and 6-day battery.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Fitbit',
                'model': 'Sense 2',
                'discount': 25
            },
            {
                'title': 'Amazfit GTR 4 Smartwatch',
                'price': 199.99,
                'description': 'Fitness smartwatch with GPS, 14-day battery, and 150+ sports modes.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Amazfit',
                'model': 'GTR 4',
                'discount': 30
            },
            {
                'title': 'Polar Vantage V3 Multisport',
                'price': 599.99,
                'description': 'Premium multisport GPS watch with advanced training metrics and recovery insights.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Polar',
                'model': 'Vantage V3',
                'discount': 15
            },
            {
                'title': 'Suunto 9 Peak Pro GPS Watch',
                'price': 569.99,
                'description': 'Ultra-thin GPS sports watch with titanium construction and extreme battery life.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Suunto',
                'model': '9 Peak Pro',
                'discount': 18
            },
            
            # Networking & Tech Infrastructure
            {
                'title': 'ASUS AX6000 WiFi 6 Router',
                'price': 349.99,
                'description': 'High-performance WiFi 6 router with 6000 Mbps speeds and advanced security.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'ASUS',
                'model': 'AX6000',
                'discount': 20
            },
            {
                'title': 'Netgear Orbi AX6000 Mesh System',
                'price': 699.99,
                'description': 'Tri-band mesh WiFi system covering up to 7,500 sq ft with WiFi 6 speeds.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Netgear',
                'model': 'Orbi AX6000',
                'discount': 25
            },
            {
                'title': 'Ubiquiti Dream Machine Pro',
                'price': 899.99,
                'description': 'Enterprise-grade network security gateway with UniFi protection and IDS/IPS.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Ubiquiti',
                'model': 'Dream Machine Pro',
                'discount': 10
            },
            
            # VR & AR Devices
            {
                'title': 'Meta Quest 3 VR Headset 512GB',
                'price': 649.99,
                'description': 'Mixed reality headset with hand tracking, 4K+ display, and wireless freedom.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500',
                'brand': 'Meta',
                'model': 'Quest 3',
                'discount': 12
            },
            {
                'title': 'Apple Vision Pro',
                'price': 3499.99,
                'description': 'Revolutionary spatial computer with ultra-high resolution displays and eye tracking.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Apple',
                'model': 'Vision Pro',
                'discount': 3
            },
            {
                'title': 'PICO 4 Enterprise VR Headset',
                'price': 799.99,
                'description': 'Business VR headset with pancake lenses, inside-out tracking, and enterprise features.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500',
                'brand': 'PICO',
                'model': 'PICO 4 Enterprise',
                'discount': 15
            },
            
            # More Professional Equipment
            {
                'title': 'Blackmagic Pocket Cinema 6K Pro',
                'price': 2535.99,
                'description': 'Professional cinema camera with 6K recording, built-in ND filters, and CFast recording.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Blackmagic',
                'model': 'Pocket 6K Pro',
                'discount': 8
            },
            {
                'title': 'RED KOMODO-X 6K Camera',
                'price': 9995.99,
                'description': 'Professional cinema camera with 6K global shutter and compact form factor.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'RED',
                'model': 'KOMODO-X',
                'discount': 5
            },
            {
                'title': 'Atomos Ninja V+ 5" Monitor Recorder',
                'price': 799.99,
                'description': '5-inch HDR monitor and recorder with 8K30p recording capability.',
                'category': 'camera',
                'image': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=500',
                'brand': 'Atomos',
                'model': 'Ninja V+',
                'discount': 12
            },
            
            # More TVs & Displays
            {
                'title': 'Sony 85" X90L LED 4K TV',
                'price': 2199.99,
                'description': 'Large 4K LED TV with cognitive processor, perfect for sports and gaming.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'Sony',
                'model': 'X90L',
                'discount': 20
            },
            {
                'title': 'LG C3 55" OLED Smart TV',
                'price': 1399.99,
                'description': 'OLED TV with α9 Gen6 AI processor, Dolby Vision, and webOS smart platform.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'LG',
                'model': 'OLED55C3',
                'discount': 25
            },
            {
                'title': 'TCL 75" C735 QLED 4K TV',
                'price': 999.99,
                'description': 'Large QLED TV with quantum dots, VRR gaming, and Google TV platform.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'TCL',
                'model': '75C735',
                'discount': 30
            },
            {
                'title': 'Hisense 55" A7K Series 4K TV',
                'price': 399.99,
                'description': 'Affordable 4K smart TV with Dolby Vision HDR and Fire TV built-in.',
                'category': 'tv',
                'image': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500',
                'brand': 'Hisense',
                'model': 'A7K Series',
                'discount': 35
            },
            
            # Storage & Computing
            {
                'title': 'WD Black SN850X 2TB NVMe SSD',
                'price': 199.99,
                'description': 'High-performance NVMe SSD with 7300 MB/s read speeds for gaming and creation.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Western Digital',
                'model': 'SN850X',
                'discount': 30
            },
            {
                'title': 'Samsung 980 PRO 1TB SSD',
                'price': 129.99,
                'description': 'PCIe 4.0 NVMe SSD with 7000 MB/s sequential read speeds.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Samsung',
                'model': '980 PRO',
                'discount': 25
            },
            {
                'title': 'Crucial P5 Plus 2TB NVMe SSD',
                'price': 179.99,
                'description': 'PCIe 4.0 SSD with advanced security features and reliable performance.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Crucial',
                'model': 'P5 Plus',
                'discount': 28
            },
            {
                'title': 'Corsair Vengeance LPX 32GB DDR4',
                'price': 119.99,
                'description': 'High-performance desktop memory with aggressive styling and overclocking support.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Corsair',
                'model': 'Vengeance LPX',
                'discount': 20
            },
            
            # Budget-Friendly Options
            {
                'title': 'Redmi Buds 4 Pro Wireless Earbuds',
                'price': 69.99,
                'description': 'Affordable earbuds with active noise cancellation and wireless charging case.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=500',
                'brand': 'Redmi',
                'model': 'Buds 4 Pro',
                'discount': 40
            },
            {
                'title': 'JLab Epic Air Sport ANC',
                'price': 99.99,
                'description': 'Sports earbuds with active noise cancellation and IP66 sweat resistance.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=500',
                'brand': 'JLab',
                'model': 'Epic Air Sport',
                'discount': 35
            },
            {
                'title': 'Anker Soundcore Liberty 4 NC',
                'price': 99.99,
                'description': 'Budget-friendly earbuds with adaptive noise cancelling and 50-hour playtime.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=500',
                'brand': 'Anker',
                'model': 'Liberty 4 NC',
                'discount': 30
            },
            {
                'title': 'TP-Link Archer AX73 WiFi 6 Router',
                'price': 149.99,
                'description': 'Dual-band WiFi 6 router with 5400 Mbps speeds and advanced security.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'TP-Link',
                'model': 'Archer AX73',
                'discount': 25
            },
            
            # Home Entertainment
            {
                'title': 'Klipsch Reference Theater Pack 5.1',
                'price': 399.99,
                'description': 'Complete 5.1 surround sound system with satellite speakers and subwoofer.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'Klipsch',
                'model': 'Reference Theater',
                'discount': 30
            },
            {
                'title': 'Yamaha RX-V6A 7.2 AV Receiver',
                'price': 599.99,
                'description': 'AV receiver with Dolby Atmos, 8K passthrough, and MusicCast multiroom.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'Yamaha',
                'model': 'RX-V6A',
                'discount': 18
            },
            {
                'title': 'SVS SB-1000 Pro Subwoofer',
                'price': 599.99,
                'description': 'Compact sealed subwoofer with 12-inch driver and DSP control.',
                'category': 'speakers',
                'image': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500',
                'brand': 'SVS',
                'model': 'SB-1000 Pro',
                'discount': 15
            },
            
            # Productivity & Work Tools
            {
                'title': 'Wacom Cintiq Pro 27 Graphics Tablet',
                'price': 3199.99,
                'description': 'Professional pen display with 4K resolution and color accuracy for digital artists.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?w=500',
                'brand': 'Wacom',
                'model': 'Cintiq Pro 27',
                'discount': 8
            },
            {
                'title': 'Huion Kamvas Pro 24 2.5K',
                'price': 599.99,
                'description': 'Large pen display with 2.5K resolution, 145% sRGB, and battery-free stylus.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?w=500',
                'brand': 'Huion',
                'model': 'Kamvas Pro 24',
                'discount': 20
            },
            {
                'title': 'Herman Miller Ollin Monitor Arm',
                'price': 395.99,
                'description': 'Premium monitor arm with easy adjustment and cable management.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Herman Miller',
                'model': 'Ollin',
                'discount': 10
            },
            {
                'title': 'Logitech Brio 4K Webcam',
                'price': 199.99,
                'description': '4K webcam with HDR, autofocus, and Windows Hello face recognition.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500',
                'brand': 'Logitech',
                'model': 'Brio 4K',
                'discount': 22
            },
            
            # More Accessories & Tools
            {
                'title': 'Elgato Key Light Air',
                'price': 129.99,
                'description': 'Professional LED panel light for video conferencing and content creation.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Elgato',
                'model': 'Key Light Air',
                'discount': 20
            },
            {
                'title': 'Blue Yeti X Professional Microphone',
                'price': 169.99,
                'description': 'Professional USB microphone with real-time LED meter and intelligent lighting.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'brand': 'Blue',
                'model': 'Yeti X',
                'discount': 25
            },
            {
                'title': 'Rode PodMic USB Microphone',
                'price': 199.99,
                'description': 'Broadcast-quality dynamic microphone designed specifically for podcasting.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500',
                'brand': 'Rode',
                'model': 'PodMic USB',
                'discount': 18
            },
            {
                'title': 'Focusrite Scarlett Solo 3rd Gen',
                'price': 129.99,
                'description': 'USB audio interface with studio-quality preamp for recording and streaming.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Focusrite',
                'model': 'Scarlett Solo',
                'discount': 15
            },
            
            # Fitness Tech
            {
                'title': 'Peloton Guide Strength Training',
                'price': 295.99,
                'description': 'AI-powered strength training system with movement tracking and personal coaching.',
                'category': 'electronics',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Peloton',
                'model': 'Guide',
                'discount': 20
            },
            {
                'title': 'Oura Ring Gen 3 Health Tracker',
                'price': 299.99,
                'description': 'Smart ring with sleep tracking, heart rate monitoring, and activity insights.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'Oura',
                'model': 'Ring Gen 3',
                'discount': 15
            },
            {
                'title': 'WHOOP 4.0 Fitness Tracker',
                'price': 239.99,
                'description': 'Screenless fitness tracker with continuous monitoring and personalized coaching.',
                'category': 'smartwatch',
                'image': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=500',
                'brand': 'WHOOP',
                'model': '4.0',
                'discount': 12
            },
            
            # E-commerce & Productivity
            {
                'title': 'Rocketbook Core Reusable Notebook',
                'price': 27.99,
                'description': 'Reusable smart notebook that connects to cloud services with specialized pen.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500',
                'brand': 'Rocketbook',
                'model': 'Core',
                'discount': 25
            },
            {
                'title': 'Tile Mate Bluetooth Tracker 4-Pack',
                'price': 59.99,
                'description': 'Bluetooth tracking tags to find your keys, wallet, and other important items.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1609592807107-e818ec901b37?w=500',
                'brand': 'Tile',
                'model': 'Mate',
                'discount': 30
            },
            {
                'title': 'Apple AirTag 4-Pack',
                'price': 99.99,
                'description': 'Precision finding tags that integrate seamlessly with the Find My network.',
                'category': 'accessories',
                'image': 'https://images.unsplash.com/photo-1609592807107-e818ec901b37?w=500',
                'brand': 'Apple',
                'model': 'AirTag',
                'discount': 15
            },
            
            # More Gaming Hardware
            {
                'title': 'ASUS TUF Gaming A16 Laptop',
                'price': 999.99,
                'description': 'Gaming laptop with AMD Ryzen 7, RTX 4060, and military-grade durability.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'ASUS',
                'model': 'TUF A16',
                'discount': 20
            },
            {
                'title': 'MSI Katana 15 Gaming Laptop',
                'price': 1199.99,
                'description': 'Performance gaming laptop with RTX 4070, Intel i7, and 144Hz display.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'MSI',
                'model': 'Katana 15',
                'discount': 18
            },
            {
                'title': 'Gigabyte AORUS 17X Gaming Laptop',
                'price': 2299.99,
                'description': 'High-end gaming laptop with RTX 4080, mechanical keyboard, and advanced cooling.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500',
                'brand': 'Gigabyte',
                'model': 'AORUS 17X',
                'discount': 12
            },
            
            # Additional Affordable Options
            {
                'title': 'Amazon Fire HD 10 Tablet',
                'price': 149.99,
                'description': '10.1-inch tablet with all-day battery, hands-free Alexa, and Prime Video.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1586953208448-b95a79798f07?w=500',
                'brand': 'Amazon',
                'model': 'Fire HD 10',
                'discount': 35
            },
            {
                'title': 'Lenovo IdeaPad 3 15" Laptop',
                'price': 549.99,
                'description': 'Budget laptop with AMD Ryzen 5, 8GB RAM, and 256GB SSD for everyday use.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500',
                'brand': 'Lenovo',
                'model': 'IdeaPad 3',
                'discount': 25
            },
            {
                'title': 'ASUS VivoBook 15 X1500EA',
                'price': 499.99,
                'description': 'Lightweight laptop with Intel i5, full-size keyboard, and fingerprint sensor.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'brand': 'ASUS',
                'model': 'VivoBook 15',
                'discount': 30
            },
            {
                'title': 'HP Pavilion 15 Laptop',
                'price': 679.99,
                'description': 'Mid-range laptop with AMD Ryzen 7, 16GB RAM, and modern design.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1484788984921-03950022c9ef?w=500',
                'brand': 'HP',
                'model': 'Pavilion 15',
                'discount': 22
            },
            {
                'title': 'Acer Aspire 5 A515-57',
                'price': 599.99,
                'description': 'Student laptop with Intel i5, comfortable keyboard, and all-day battery.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'brand': 'Acer',
                'model': 'Aspire 5',
                'discount': 28
            },
            
            # More Premium Products
            {
                'title': 'iPad Pro 11-inch M4 1TB',
                'price': 1499.99,
                'description': 'Latest iPad Pro with M4 chip, Tandem OLED display, and enhanced performance.',
                'category': 'tablet',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500',
                'brand': 'Apple',
                'model': 'iPad Pro 11 M4',
                'discount': 8
            },
            {
                'title': 'MacBook Pro 14-inch M3 Pro',
                'price': 1999.99,
                'description': 'Professional laptop with M3 Pro chip, Liquid Retina XDR display, and advanced connectivity.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500',
                'brand': 'Apple',
                'model': 'MacBook Pro 14',
                'discount': 10
            },
            {
                'title': 'Surface Laptop Studio 2 RTX 4060',
                'price': 2399.99,
                'description': 'Versatile laptop with unique hinge design, touchscreen, and discrete graphics.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1629131726692-1accd0c53ce0?w=500',
                'brand': 'Microsoft',
                'model': 'Laptop Studio 2',
                'discount': 12
            },
            
            # Final Products to Reach 100+
            {
                'title': 'Razer BlackShark V2 Pro Wireless',
                'price': 179.99,
                'description': 'Professional esports headset with THX spatial audio and 24-hour battery.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'Razer',
                'model': 'BlackShark V2 Pro',
                'discount': 20
            },
            {
                'title': 'EPOS H6Pro Closed Gaming Headset',
                'price': 179.99,
                'description': 'Closed acoustic gaming headset with premium drivers and broadcast-quality mic.',
                'category': 'headphones',
                'image': 'https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500',
                'brand': 'EPOS',
                'model': 'H6Pro Closed',
                'discount': 25
            },
            {
                'title': 'Creative Sound Blaster X4',
                'price': 149.99,
                'description': 'External sound card with Super X-Fi technology and multiple connectivity options.',
                'category': 'audio',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500',
                'brand': 'Creative',
                'model': 'Sound Blaster X4',
                'discount': 18
            },
            {
                'title': 'SteelSeries Apex 7 TKL Keyboard',
                'price': 159.99,
                'description': 'Mechanical gaming keyboard with OLED smart display and magnetic wrist rest.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'SteelSeries',
                'model': 'Apex 7 TKL',
                'discount': 28
            },
            {
                'title': 'Logitech G915 TKL Lightspeed',
                'price': 229.99,
                'description': 'Wireless mechanical gaming keyboard with low-profile switches and RGB.',
                'category': 'keyboard',
                'image': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=500',
                'brand': 'Logitech',
                'model': 'G915 TKL',
                'discount': 22
            },
            {
                'title': 'Corsair Dark Core RGB Pro SE',
                'price': 89.99,
                'description': 'Wireless gaming mouse with Qi charging, 18K DPI sensor, and customizable weight.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'Corsair',
                'model': 'Dark Core RGB Pro',
                'discount': 30
            },
            {
                'title': 'BenQ ZOWIE EC3-C Gaming Mouse',
                'price': 69.99,
                'description': 'Professional esports mouse with 3360 sensor and ergonomic right-handed design.',
                'category': 'mouse',
                'image': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500',
                'brand': 'BenQ ZOWIE',
                'model': 'EC3-C',
                'discount': 15
            },
            {
                'title': 'ASUS ProArt StudioBook 16 OLED',
                'price': 1799.99,
                'description': 'Creator laptop with OLED display, RTX A2000, and ASUS Dial for creative work.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'brand': 'ASUS',
                'model': 'ProArt StudioBook',
                'discount': 15
            },
            {
                'title': 'Gigabyte AERO 16 Creator Laptop',
                'price': 2199.99,
                'description': 'Creator laptop with 4K OLED display, RTX 4070, and color-accurate screen.',
                'category': 'laptop',
                'image': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=500',
                'brand': 'Gigabyte',
                'model': 'AERO 16',
                'discount': 12
            },
            {
                'title': 'Alienware Aurora R15 Desktop',
                'price': 1999.99,
                'description': 'Gaming desktop with RTX 4070, Intel i7, and liquid cooling system.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500',
                'brand': 'Alienware',
                'model': 'Aurora R15',
                'discount': 15
            },
            {
                'title': 'NZXT BLD H5 Gaming PC',
                'price': 1599.99,
                'description': 'Pre-built gaming PC with RTX 4060 Ti, AMD Ryzen 5, and tempered glass case.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500',
                'brand': 'NZXT',
                'model': 'BLD H5',
                'discount': 18
            },
            {
                'title': 'Origin PC Chronos Gaming Desktop',
                'price': 2799.99,
                'description': 'Custom gaming desktop with RTX 4080, Intel i9, and premium components.',
                'category': 'gaming',
                'image': 'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500',
                'brand': 'Origin PC',
                'model': 'Chronos',
                'discount': 10
            },
            
            # More Monitors & Displays
            {
                'title': 'MSI Optix MAG274QRF-QD',
                'price': 399.99,
                'description': '27-inch 1440p gaming monitor with 165Hz, quantum dot technology, and RGB.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'MSI',
                'model': 'Optix MAG274QRF',
                'discount': 25
            },
            {
                'title': 'ViewSonic Elite XG270QG',
                'price': 549.99,
                'description': '27-inch 1440p gaming monitor with G-Sync, 165Hz, and premium build quality.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'ViewSonic',
                'model': 'Elite XG270QG',
                'discount': 20
            },
            {
                'title': 'AOC CU34G2X Ultrawide Monitor',
                'price': 329.99,
                'description': '34-inch curved ultrawide monitor with 144Hz refresh rate and FreeSync.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'AOC',
                'model': 'CU34G2X',
                'discount': 30
            },
            {
                'title': 'Philips 328E1CA 32" 4K Monitor',
                'price': 299.99,
                'description': '32-inch 4K monitor with IPS panel, USB-C connectivity, and eye care technology.',
                'category': 'monitor',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500',
                'brand': 'Philips',
                'model': '328E1CA',
                'discount': 28
            }
        ]
        
        # Create products
        for product_data in sample_products:
            category = Category.objects.get(name=product_data['category'])
            product, created = Product.objects.get_or_create(
                title=product_data['title'],
                defaults={
                    'price': product_data['price'],
                    'description': product_data['description'],
                    'category': category,
                    'image': product_data['image'],
                    'brand': product_data['brand'],
                    'model': product_data['model'],
                    'discount': product_data['discount']
                }
            )
            if created:
                self.stdout.write(f'Created product: {product_data["title"]}')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated database with {len(sample_products)} products across {len(categories_data)} categories')
        )