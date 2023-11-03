import tensorflow as tf
class BatchData:
    def __init__(self, dataset):
        self.dataset = dataset
        self.current_batch = None
        self.batch_quantity = None
        self.batch_size = None

    def get_batch_info(self):
        iterator = iter(self.dataset)
        self.current_batch = next(iterator)
        self.batch_quantity = tf.data.experimental.cardinality(self.dataset).numpy()
        self.batch_size = len(self.current_batch[0])
        return self.batch_quantity, self.batch_size, self.current_batch


# Usage example:
dataset = tf.data.Dataset.from_tensor_slices(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])).batch(2)
batch_data = BatchData(dataset)
batch_data.get_batch_info()
batch_data.print_batch_info()