def evaluation_classification_model(tp, fp, fn):

    if not isinstance(tp, int):
        raise ValueError("tp must be an integer")
    if not isinstance(fp, int):
        raise ValueError("fp must be an integer")
    if not isinstance(fn, int):
        raise ValueError("fn must be an integer")
    
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, and fn must be greater than zero")

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return precision, recall, f1_score

tp_input = input("Type TP: ")
fp_input = input("Type FP: ")
fn_input = input("Type FN: ")

try:
    tp = int(tp_input)
    fp = int(fp_input)
    fn = int(fn_input)
except ValueError:
    print("tp, fp, and fn must be integers")
    exit()

precision, recall, f1_score = evaluation_classification_model(tp, fp, fn)
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1_score}")

