import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.jaccard import compare_all_files, run_jaccard_assertions

def test_jaccard_similarity_assertions():
    metamorph = ['original', 'blur', 'brightness', 'failures', 'geometric', 'marks', 'noisy', 'resolution', 'rotation']
    all_passed_results = []
    all_failed_results = []

    for code in ['easyocr', 'tesseract']:
      print("\n\nTratando das relações do "+code+"\n\n")

      for relation in metamorph:
        
          folder_path = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\result\\"+code
          reference_file_path = os.path.join(folder_path, relation + ".txt")
          results_tesseract = compare_all_files(folder_path, reference_file_path)
          
          passed_results, failed_results = run_jaccard_assertions(results_tesseract)
          all_passed_results.extend(passed_results)
          all_failed_results.extend(failed_results)
          
          print(f"\nSummary for relation {relation}:")
          print(f"Passed results: {len(passed_results)}\n")
          print("Passed files:")

          for passed_result in passed_results:
              print(f"{passed_result[0]} and {passed_result[1]}\n\n")
          print(f"Failed results: {len(failed_results)}")
          print("Failed files:")

          for failed_result in failed_results:
              print(f"{failed_result[0]} and {failed_result[1]}")
    
    print("\nSummary for Jaccard similarity:")
    print(f"\nTotal passed results: {len(all_passed_results)}\n")
    print("Passed files:")

    for passed_result in all_passed_results:
        print(f"{passed_result[0]} and {passed_result[1]}")
    
    if all_failed_results:
        raise AssertionError("\nOne or more assertions failed.")