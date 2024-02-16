import pandas as pd
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset, load_from_disk, load_metric
from TextSummarizer.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i:i+batch_size]

    def calculate_metric_on_test_data(self,
                                      metric,
                                      dataset,
                                      column_text,
                                      column_summary,
                                      batch_size,
                                      model,
                                      tokenizer,
                                      device="cuda" if torch.cuda.is_available() else "cpu"
                                      ):
        article_batches = list(self.generate_batch_sized_chunks(
            dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(
            dataset[column_summary], batch_size))

        # For each batch in the list of article_batches

        for article_batche, target_batche in tqdm(
            zip(article_batches, target_batches),
                total=len(article_batches)

        ):

            inputs = tokenizer(article_batche, max_length=1024,
                               truncation=True, padding="max_length", return_tensors="pt")
            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                                       attention_mask=inputs["attention_mask"].to(
                                           device),
                                       length_penalty=0.8,
                                       num_beams=8,
                                       max_length=128)
            decoded_summaries = [tokenizer.decode(
                s, skip_special_tokens=True, clean_up_tokenization_spaces=True) for s in summaries]

            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            metric.add_batch(predictions=decoded_summaries,
                             references=target_batche)

        score = metric.compute()
        return score

    def evaluate(self, device="cuda" if torch.cuda.is_available() else "cpu"):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_path).to(device)

        # load dataest
        dataset = load_from_disk(self.config.data_path)
        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_metric = load_metric("rouge")
        score = self.calculate_metric_on_test_data(metric=rouge_metric,
                                                   dataset=dataset['test'][0:10],
                                                   column_text="dialogue",
                                                   column_summary="summary",
                                                   batch_size=2,
                                                   model=model_pegasus,
                                                   tokenizer=tokenizer,
                                                   device=device
                                                   )
        rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names)

        df = pd.DataFrame(rouge_dict, index=['pegasus'])
        df.to_csv(self.config.metric_file_name, index=False)
