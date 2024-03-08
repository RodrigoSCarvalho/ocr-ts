from pdf2image import convert_from_path
from PIL import Image
import os
import threading

def simulate_worse_resolution(image, target_dpi):
    # Calcula a nova largura e altura com base na resolução desejada (dpi)
    width, height = image.size
    new_width = int(width * (target_dpi / 300))  # Assumindo uma resolução original de 300 dpi
    new_height = int(height * (target_dpi / 300))

    # Redimensiona a imagem para a nova largura e altura
    image.thumbnail((new_width, new_height))

    return image

def process_page(page, page_num, output_dir):
    print(f"Processando página {page_num + 1}...")

    target_dpi = 50

    cloned_page = page.copy()
    worse_resolution_image = simulate_worse_resolution(cloned_page, target_dpi)

    output_image_path = os.path.join(output_dir, f"page_{page_num}.png")
    worse_resolution_image.save(output_image_path)
    print(f"Thread concluída para processar página {page_num + 1}.")

input_pdf = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\files\Alices_Adventures_in_Wonderland-Lewis_Carroll.pdf'
output_dir = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\images\resolution'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

start_page = 3
end_page = 7

pages = convert_from_path(input_pdf, first_page=start_page, last_page=end_page)
threads = []

for page_num, page in enumerate(pages):
    thread = threading.Thread(target=process_page, args=(page, page_num, output_dir))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
