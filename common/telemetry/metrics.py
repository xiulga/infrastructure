from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry import metrics
from prometheus_client import start_http_server

def init_metrics(service_name: str, port: int = 9464) -> None:
    """Initialize Prometheus metrics exporter."""
    reader = PrometheusMetricReader()
    provider = MeterProvider(metric_readers=[reader])
    metrics.set_meter_provider(provider)
    start_http_server(port)
    print(f"✅ Prometheus metrics server started for {service_name} on port {port}")
