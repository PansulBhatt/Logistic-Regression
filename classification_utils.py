def confusion_matrix(truth_values, predicted_values):
    """
    Function to fetch the True positive, true negative, false negative and false positive
    """
    actual_values = truth_values.iloc[:, 0].tolist()
    return {
        'TP': sum(1 for i in range(len(actual_values)) if actual_values[i] == predicted_values[i] == 'yes'),
        'TN': sum(1 for i in range(len(actual_values)) if actual_values[i] == predicted_values[i] == 'no'),
        'FN': sum(1 for i in range(len(actual_values)) if actual_values[i] == 'yes' and predicted_values[i] == 'no'),
        'FP': sum(1 for i in range(len(actual_values)) if actual_values[i] == 'no' and predicted_values[i] == 'yes'),
    }


def accuracy(truth_values, predicted_values):
    """
    Computes accuracy
    :param truth_values: true values
    :param predicted_values: predictions

    :return: accuracy
    """
    _matrix = confusion_matrix(truth_values, predicted_values)
    
    accuracy = (_matrix['TP'] + _matrix['TN']) / sum(_matrix.values())
    
    return accuracy

def precision(truth_values, predicted_values):
    """
    Computes precision
    :param truth_values: true values
    :param predicted_values: predictions

    :return: precision
    """
    _matrix = confusion_matrix(truth_values, predicted_values)
    
    precision = (_matrix['TP']) / (_matrix['TP'] + _matrix['FP'])
    
    return precision


def recall(truth_values, predicted_values):
    """
    Computes recall
    :param truth_values: true values
    :param predicted_values: predictions

    :return: recall
    """
    _matrix = confusion_matrix(truth_values, predicted_values)
    
    recall = _matrix['TP'] / (_matrix['TP'] + _matrix['FN'])

    return recall

