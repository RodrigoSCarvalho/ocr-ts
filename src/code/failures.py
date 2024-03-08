from pdf2image import convert_from_path
from PIL import Image, ImageDraw
import random
import os
import threading

def simulate_scan_failures(image, num_failures):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    for _ in range(num_failures):
        
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        
        size = random.randint(1, 5)
        
        draw.rectangle([x, y, x + size, y + size], fill="black")
    return image

def process_page(page, page_num, output_dir):
    print(f"Processando página {page_num + 1}...")
    num_failures = random.randint(100, 200)
    
    cloned_page = page.copy()
    scanned_image = simulate_scan_failures(cloned_page, num_failures)
    
    output_image_path = os.path.join(output_dir, f"page_{page_num}.png")
    scanned_image.save(output_image_path, quality=100)
    print(f"Thread concluída para processar página {page_num + 1}.")

input_pdf = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\files\ALGUMAS PROPOSIÇÕES.pdf'
output_dir = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\failures'

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
