# TODO: Create a function to calculate accuracy and precision metrics
def calculate_metrics(matrix):
    tp, fp, fn, tn = map(int, matrix)
    
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    if tp + fp != 0:
        precision = tp / (tp + fp)
    else:
        precision = 0 

    return accuracy, precision

# TODO: Create a function to find the matrix index with the best combined accuracy and precision
def best_performance(matrices):
    best_index = -1
    best_accuracy = -1
    best_precision = -1
    # TODO: Define Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
        # TODO: Calculate accuracy and precision
        accuracy, precision = calculate_metrics(matrix)

        # TODO: Update best metrics if found
        if (accuracy > best_accuracy) or (accuracy == best_accuracy and precision > best_precision):
            best_index = index
            best_accuracy = accuracy
            best_precision = precision
       
    return best_index, round(best_accuracy, 2), round(best_precision, 2)
    
def main():
    n = int(input())
    matrices = []

    for _ in range(n):
        matrix = input()
        matrices.append(matrix.split(','))

    index, accuracy, precision = best_performance(matrices)
    
    # Print the results
    print(f"Índice: {index + 1}")
    print(f"Acurácia: {accuracy}")
    print(f"Precisão: {precision}")
    
if __name__ == "__main__":
    main()