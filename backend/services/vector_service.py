# services/vector_service.py
from services.simple_vector_service import SimpleVectorService

# Create a single instance
vector_service = SimpleVectorService()

# Export for use in other files
__all__ = ['vector_service']