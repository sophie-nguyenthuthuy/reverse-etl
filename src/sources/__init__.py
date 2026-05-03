from .base import BaseSource
from .postgres import PostgresSource
from .bigquery import BigQuerySource
from .snowflake import SnowflakeSource

SOURCE_REGISTRY: dict[str, type[BaseSource]] = {
    "postgres": PostgresSource,
    "bigquery": BigQuerySource,
    "snowflake": SnowflakeSource,
}

__all__ = ["BaseSource", "PostgresSource", "BigQuerySource", "SnowflakeSource", "SOURCE_REGISTRY"]
