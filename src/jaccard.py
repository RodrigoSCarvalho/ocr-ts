import os
from nltk import ngrams

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def jaccard_similarity(str1, str2, n=3):
    set1 = set(ngrams(str1, n))
    set2 = set(ngrams(str2, n))
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return round(intersection / union, 2)

def compare_files_jaccard(file1_path, file2_path, n=3):
    content1 = read_file(file1_path)
    content2 = read_file(file2_path)
    similarity = jaccard_similarity(content1, content2, n)
    return similarity

def compare_all_files_with_reference_jaccard(folder_path, reference_file_path, n=3):
    results = []
    reference_content = read_file(reference_file_path)
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            similarity = compare_files_jaccard(reference_file_path, file_path, n)
            results.append((reference_file_path.split("\\")[-1], filename, similarity))
            
            print(f"{filename}: {similarity}")
    return results

def generate_report_jaccard(results, report_file_path):
    with open(report_file_path, 'w', encoding='utf-8') as report_file:
        report_file.write("Comparison Report:\n\n")
        for result in results:
            report_file.write(f"{result[0]} and {result[1]}: {result[2]}\n")
        print(f"Report generated: {report_file_path}")

if __name__ == "__main__":
    algorithms = ['easyocr', 'tesseract']
    reference_file_path = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\oracle\oracle.txt"

    for algorithm in algorithms:
        input_folder = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\result\\" + algorithm
        output_folder = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\output\jaccard\\" + algorithm
    
        results = compare_all_files_with_reference_jaccard(input_folder, reference_file_path)
        
        if results:
            generate_report_jaccard(results, os.path.join(output_folder, "result.txt"))
        else:
            print("Nenhum arquivo encontrado para comparação.")
