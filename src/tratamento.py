import PyPDF2
import numpy as np
import shutil
import os
def remove_empty_pages(pdf_file):
  """
  Remove páginas que não tenham texto de um PDF.
  Args:
    pdf_file: O caminho para o arquivo PDF.
  Returns:
    O arquivo PDF com as páginas vazias removidas.
  """
  
  pdf = PyPDF2.PdfReader (pdf_file)
  
  new_pdf = PyPDF2.PdfWriter()
  
  for page in pdf.pages:
    
    if isinstance(page, int):
      
      current_page = pdf.pages[page]
      
      if not current_page.extractText():
        
        pdf.removePage(page)
  
  with open("new.pdf", "wb") as f:
    new_pdf.write(f)
def add_gaussian_noise(pdf_file, sigma):
  """
  Adiciona ruídos Gaussianos a todas as páginas de um PDF.
  Args:
    pdf_file: O caminho para o arquivo PDF.
    sigma: O desvio padrão do ruído Gaussiano.
  Returns:
    O arquivo PDF com ruídos adicionados.
  """
  
  pdf_writer = PyPDF2.PdfWriter()
  
  pdf = PyPDF2.PdfReader (pdf_file)
  
  for page in pdf.pages:
    
    if isinstance(page, int):
      
      page_image = pdf.pages[page].getImage()
      
      noise = np.random.normal(0, sigma, size=page_image.size)
      page_image = page_image + noise
      
      page_image = np.mean(page_image, axis=2)
      
      pdf_writer.addPage(page)
  
  with open("new.pdf", "wb") as f:
    pdf_writer.write(f)
if __name__ == "__main__":
    pdf_file = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\assets\A_Escrava_Isaura.pdf"
        
    
    remove_empty_pages(pdf_file)
    
    new_pdf_file = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\assets\temp.pdf"
    
    shutil.copyfile(pdf_file, new_pdf_file)
    
    
    pdf_file = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\assets\temp.pdf"
    
    sigma = 30
    
    add_gaussian_noise(pdf_file, sigma)
    
    new_pdf_file = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\assets\noisy"
    
    if not os.path.exists(new_pdf_file):
        os.makedirs(new_pdf_file)
    
    shutil.copyfile(pdf_file, new_pdf_file + r"\A_Escrava_Isaura.pdf")
