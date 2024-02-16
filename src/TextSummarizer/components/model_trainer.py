
from transformers import DataCollatorForSeq2Seq, TrainingArguments, Trainer, AutoTokenizer, AutoModelForSeq2SeqLM
from TextSummarizer.config.configurations import ModelTrainerConfig
from datasets import load_from_disk
import torch
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def train(self):
        # device = "cuda" if torch.cuda.is_available() else "cpu"
        device = "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(
            tokenizer, model=model_pegasus)

        # load dataset
        dataset_samasum_tokenized = load_from_disk(self.config.data_path)

        # load arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_training_epochs,
            # uses a low learining rate for a set number of training examples
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            # weight decal for AdamW optimizer
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            # eval_steps                  = self.config.eval_steps,
            # save_steps                  = self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            # auto_find_batch_size=True
        )

        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samasum_tokenized["train"],
            eval_dataset=dataset_samasum_tokenized["validation"]

        )

        # # trainer.train()
        # Save model
        model_pegasus.save_pretrained(os.path.join(
            self.config.root_dir, "pegasus-samsum-model"))
        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(
            self.config.root_dir, "tokenizer"))
