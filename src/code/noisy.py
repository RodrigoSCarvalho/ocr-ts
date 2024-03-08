from pdf2image import convert_from_path
from PIL import Image, ImageDraw
import random
import os
import threading

def add_noise_to_image(image, noise_intensity):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    for _ in range(int(width * height * noise_intensity)):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return image

def process_page(page, page_num, output_dir):
    print(f"Processando página {page_num + 1}...")
    noisy_image = add_noise_to_image(page, noise_intensity=0.2)  
    
    output_image_path = os.path.join(output_dir, f"page_{page_num}.png")
    noisy_image.save(output_image_path, quality=100)
    
    print(f"Thread concluída para processar página {page_num + 1}.")
    

input_pdf = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\files\ALGUMAS PROPOSIÇÕES.pdf'
output_dir = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\noisy'

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