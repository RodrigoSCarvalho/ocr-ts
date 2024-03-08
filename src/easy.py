import os
import cv2
import easyocr
import time

language = 'pt'
reader = easyocr.Reader([language])
metamorph = ['original', 'brightness', 'geometric','resolution', 'rotation']#['original', 'blur', 'brightness', 'failures', 'geometric', 'marks', 'noisy', 'resolution', 'rotation']
resultados_globais = []
start_time_total = time.time()

for relation in metamorph:
    input_folder = 'C:/Users/rodri/Documents/UFF/Mestrado/TS/OCR/src/images/' + relation
    output_folder = 'C:/Users/rodri/Documents/UFF/Mestrado/TS/OCR/src/result/easyocr'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    resultados_locais = []
    start_time = time.time()  
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img_path = os.path.join(input_folder, filename)
            
            img = cv2.imread(img_path)
            result = reader.readtext(img, detail=0)
            
            resultado = ' '.join(result)
            resultados_locais.append(resultado)
    
    resultados_globais.extend(resultados_locais)
    
    global_result_path = os.path.join(output_folder, relation + '.txt')
    with open(global_result_path, 'w', encoding='utf-8') as arq:
        arq.write('\n'.join(resultados_locais))
    print(f"Resultados locais salvos em {global_result_path}")

end_time_total = time.time()
elapsed_time_total = end_time_total - start_time_total
print(f"Tempo total de processamento: {elapsed_time_total:.2f} segundos")
