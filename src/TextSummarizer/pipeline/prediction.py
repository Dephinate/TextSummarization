from transformers import AutoTokenizer
from transformers import pipeline
from TextSummarizer.config.configurations import ConfigurationManager
import torch


class PredictionPipeline:
    def __init__(self) -> None:
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text, device=-1):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8,
                      "num_beams": 8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path,
                        tokenizer=tokenizer, device=device)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]

        print("Dialouge:")
        print(text)

        print("\nModel Summary:")
        print(output)

        return output, pipe(text, **gen_kwargs)
