from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFilter
import random
import os
import threading

def simulate_blur(image, blur_radius):
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return blurred_image

def process_page(page, page_num, output_dir):
    print(f"Processando página {page_num + 1}...")
    blur_radius = random.uniform(1, 3)
    blurred_image = simulate_blur(page, blur_radius)
    output_image_path = os.path.join(output_dir, f"page_{page_num}.png")
    blurred_image.save(output_image_path, quality=100)
    print(f"Thread concluída para processar página {page_num + 1}.")

input_pdf = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\files\ALGUMAS PROPOSIÇÕES.pdf'
output_dir = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\blur'

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
