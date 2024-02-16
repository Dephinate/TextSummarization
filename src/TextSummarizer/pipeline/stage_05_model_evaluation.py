from TextSummarizer.config.configurations import ConfigurationManager
from TextSummarizer.components.model_evaluation import ModelEvaluation
# from TextSummarizer.components.model_evaluation_copy1 import ModelEvaluation_copy


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()

            model_evaluator = ModelEvaluation(config=model_evaluation_config)
            model_evaluator.evaluate(device="cpu")

        except Exception as e:
            raise e
