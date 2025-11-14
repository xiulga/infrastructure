import logging
from opentelemetry.instrumentation.logging import LoggingInstrumentor

def init_logging(service_name: str) -> None:
    """Configure structured logging with OpenTelemetry context."""
    logging.basicConfig(
        format=f"%(asctime)s [%(levelname)s] [{service_name}] %(message)s",
        level=logging.INFO,
    )
    LoggingInstrumentor().instrument(set_logging_format=True)
    logging.info(f"Logging initialized for {service_name}")
