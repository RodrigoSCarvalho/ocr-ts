from pdf2image import convert_from_path
from PIL import Image, ImageDraw
import random
import os
import threading

def add_stains_and_marks(image, num_stains, num_marks):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    
    for _ in range(num_stains):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        radius = random.randint(5, 20)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    for _ in range(num_marks):
        x1 = random.randint(0, width - 1)
        y1 = random.randint(0, height - 1)
        x2 = random.randint(0, width - 1)
        y2 = random.randint(0, height - 1)
        draw.line((x1, y1, x2, y2), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=random.randint(1, 5))
    return image

def process_page(page, page_num, output_dir):
    print(f"Processando página {page_num + 1}...")
    
    modified_image = add_stains_and_marks(page, num_stains=5, num_marks=3)
    
    output_image_path = os.path.join(output_dir, f"page_{page_num}.png")
    modified_image.save(output_image_path, quality=100)
    
    print(f"Thread concluída para processar página {page_num + 1}.")

input_pdf = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\files\ALGUMAS PROPOSIÇÕES.pdf'
output_dir = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\marks'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

pages = convert_from_path(input_pdf, dpi=250)  
threads = []

for page_num, page in enumerate(pages):
    thread = threading.Thread(target=process_page, args=(page, page_num, output_dir))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
