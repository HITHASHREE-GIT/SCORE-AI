import spacy

from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import SpacyNlpEngine
from presidio_anonymizer import AnonymizerEngine


# Use small model instead of 400MB large model
nlp_engine = SpacyNlpEngine(
    models=[
        {
            "lang_code": "en",
            "model_name": "en_core_web_sm"
        }
    ]
)

analyzer = AnalyzerEngine(
    nlp_engine=nlp_engine
)

anonymizer = AnonymizerEngine()


def pii_redactor(text: str):

    if not text:
        return text

    results = analyzer.analyze(
        text=text,
        language="en"
    )

    if results:
        anonymized = anonymizer.anonymize(
            text=text,
            analyzer_results=results
        )

        return anonymized.text

    return text