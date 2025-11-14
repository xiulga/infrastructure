from .logging import init_logging
from .metrics import init_metrics
from .tracing import init_tracing

def init_telemetry(service_name: str) -> None:
    """Initialize logging, metrics, and tracing for the given service."""
    init_logging(service_name)
    init_tracing(service_name)
    init_metrics(service_name)
