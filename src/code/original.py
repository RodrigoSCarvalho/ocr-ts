from pdf2image import convert_from_path
import os
import threading

def process_page(page, page_num, output_dir):
    print(f"Processando página {page_num + 1}...")
    
    output_image_path = os.path.join(output_dir, f"page_{page_num}.png")
    page.save(output_image_path, quality=100)
    print(f"Thread concluída para processar página {page_num + 1}.")

input_pdf = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\files\Alices_Adventures_in_Wonderland-Lewis_Carroll.pdf'
output_dir = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\images\original'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

start_page = 3
end_page = 7

pages = convert_from_path(input_pdf, dpi=300, first_page=start_page, last_page=end_page)  
threads = []

for page_num, page in enumerate(pages):
    thread = threading.Thread(target=process_page, args=(page, page_num, output_dir))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
