from TextSummarizer.config.configurations import ConfigurationManager
from TextSummarizer.components.model_evaluation import ModelEvaluation


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main():
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluator = ModelEvaluation(config=model_evaluation_config)
            model_evaluator.evaluate()
        except Exception as e:
            raise e
