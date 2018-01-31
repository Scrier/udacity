import math
def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    assert len(features) == len(labels)
    # TODO: Implement batching
    batch_result = []
    for start in range(0, len(features), batch_size):
        stop = start + batch_size
        batch_result.append((features[start:stop], labels[start:stop]))
    return batch_result

