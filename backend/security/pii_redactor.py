from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from typing import List, Dict

class PIIRedactor:
    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
    
    def analyze_text(self, text: str) -> List[Dict]:
        """Analyze text for PII"""
        results = self.analyzer.analyze(text=text, language='en')
        return [{
            "entity_type": result.entity_type,
            "start": result.start,
            "end": result.end,
            "score": result.score
        } for result in results]
    
    def redact_text(self, text: str) -> str:
        """Redact PII from text"""
        results = self.analyzer.analyze(text=text, language='en')
        anonymized = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results
        )
        return anonymized.text
    
    def has_pii(self, text: str) -> bool:
        """Check if text contains PII"""
        results = self.analyzer.analyze(text=text, language='en')
        return len(results) > 0

pii_redactor = PIIRedactor()