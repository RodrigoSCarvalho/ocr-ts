import os
import sys
import Levenshtein
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from metric import compare_all_files, run_assertions

def test_levenshtein_ratio_assertions():
    metamorph = ['original', 'blur', 'brightness', 'failures', 'geometric', 'marks', 'noisy', 'resolution', 'rotation']
    all_failed_results = []

    for code in ['easyocr', 'tesseract']:
        print("\n\nTratando das relações do " + code + "\n\n")
        folder_path = r"C:\Users\rodri\Documents\UFF\Mestrado\TS\OCR\src\result\\" + code
        all_passed_results = []
        all_failed_results_per_code = []

        for relation in metamorph:
            reference_file_path = os.path.join(folder_path, relation + ".txt")
            results = compare_all_files(folder_path, reference_file_path)
            passed_results, failed_results = run_assertions(results)
            all_passed_results.extend(passed_results)
            all_failed_results_per_code.extend(failed_results)
            print(f"\n\nSummary for relation {relation} and code {code}:")
            print(f"\nPassed results: {len(passed_results)}")
            print("Passed files:")

            for passed_result in passed_results:
                print(f"{passed_result[0]} and {passed_result[1]}")
            print(f"\nFailed results: {len(failed_results)}")
            print("Failed files:")

            for failed_result in failed_results:
                print(f"{failed_result[0]} and {failed_result[1]}")
        all_failed_results.extend(all_failed_results_per_code)

    if all_failed_results:
        raise AssertionError("One or more assertions failed.")
