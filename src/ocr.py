import os
import cv2
import pytesseract
import time

start_time_total = time.time()
pytesseract.pytesseract.tesseract_cmd = r'D:\Arquivos Locais\Tesseract-OCR\tesseract.exe'
metamorph = ['original', 'brightness', 'geometric','resolution', 'rotation']#['original', 'blur', 'brightness', 'failures', 'geometric', 'marks', 'noisy', 'resolution', 'rotation']

for relation in metamorph:
    input_folder =  r'C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\\images\\' + relation
    output_folder = 'C:/Users/rodri/Documents/UFF/Mestrado/TS/OCR/src/result/tesseract'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    resultados_globais = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            
            img_path = os.path.join(input_folder, filename)
            
            img = cv2.imread(img_path)
            resultado = pytesseract.image_to_string(img)
            resultados_globais.append(resultado)
    
    global_result_path = os.path.join(output_folder, relation+'.txt')
    with open(global_result_path, 'w', encoding='utf-8') as arq:
        arq.write('\n'.join(resultados_globais))
    print("Resultados globais salvos em", global_result_path)

end_time_total = time.time()
elapsed_time_total = end_time_total - start_time_total
print(f"Tempo total de processamento: {elapsed_time_total:.2f} segundos")
