from pdf2image import convert_from_path
from PIL import Image, ImageDraw
import random
import os
import threading
import cv2
import numpy as np

def add_geometric_distortion(image):
    width, height = image.size
    
    
    src_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
    dst_points = np.float32([[random.uniform(0, width * 0.2), random.uniform(0, height * 0.2)],
                             [width - 1 - random.uniform(0, width * 0.2), random.uniform(0, height * 0.2)],
                             [random.uniform(0, width * 0.2), height - 1 - random.uniform(0, height * 0.2)],
                             [width - 1 - random.uniform(0, width * 0.2), height - 1 - random.uniform(0, height * 0.2)]])
    
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    
    distorted_image = cv2.warpPerspective(np.array(image), perspective_matrix, (width, height))
    return Image.fromarray(distorted_image)

def process_page(page, page_num, output_dir):
    print(f"Processando página {page_num + 1}...")
    
    distorted_image = add_geometric_distortion(page)
    
    output_image_path = os.path.join(output_dir, f"page_{page_num}.png")
    distorted_image.save(output_image_path, quality=100)
    
    print(f"Thread concluída para processar página {page_num + 1}.")

input_pdf = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\files\Alices_Adventures_in_Wonderland-Lewis_Carroll.pdf'
output_dir = r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\images\geometric'

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
