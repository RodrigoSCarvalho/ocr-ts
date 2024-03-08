import matplotlib.pyplot as plt

def plot_bar_chart(results):
    filenames = [f"{result[0]} vs {result[1]}" for result in results]
    similarities = [result[2] * 100 for result in results]  
    plt.figure(figsize=(10, 6))
    plt.barh(filenames, similarities, color='skyblue')
    plt.xlabel('Similarity Percentage')
    plt.title('Comparação de Levenshtein com EasyOCR no Arquivo Original')
    plt.xlim(0, 100)
    for index, value in enumerate(similarities):
        plt.text(value, index, f'{value:.2f}%', va='center')
    plt.show()

if __name__ == "__main__":
    
    results_test1 = [
        ("original", "blur.txt", 0.8),
        ("original", "brightness.txt", 0.95),
        ("original", "failures.txt", 0.96),
        ("original", "geometric.txt", 0.65),
        ("original", "marks.txt", 0.97),
        ("original", "noisy.txt", 0.83),
        ("original", "resolution.txt", 0.38),
        ("original", "rotation.txt", 0.56),
    ]
    plot_bar_chart(results_test1)
