import os
from TextSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_from_disk
from datasets import DatasetDict


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

# Method to tokenize input and output
    def convert_examples_to_features(self, example_batch):
        '''
        Converts input to embeddings
        Input: Document
        Output: Dictionary of Input Encodings, Attention Masks, Target Encoding
        '''
        try:

            input_encodings = self.tokenizer(
                example_batch['dialogue'], max_length=1024, truncation=True)

            with self.tokenizer.as_target_tokenizer():
                target_encodings = self.tokenizer(
                    text=example_batch['summary'], max_length=128, truncation=True)

            return {
                'input_ids': input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }
        except Exception as e:
            raise e

    def preprocess_function(self, examples_batch):
        inputs = examples_batch['dialogue']
        targets = examples_batch['summary']
        model_inputs = self.tokenizer(inputs, max_length=1024, truncation=True)
        # Setup the tokenizer for targets
        with self.tokenizer.as_target_tokenizer():
            labels = self.tokenizer(targets, max_length=128, truncation=True)
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        tokenized_data = dataset_samsum.map(
            self.convert_examples_to_features, batched=True)
        tokenized_data.save_to_disk(os.path.join(
            self.config.root_dir, "samsum_dataset"))
