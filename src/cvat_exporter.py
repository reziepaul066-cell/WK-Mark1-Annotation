"""CVAT handoff boundary for machine-generated annotation records."""
from pathlib import Path
from typing import Any, Iterable


class CvatExporter:
    """Placeholder exporter; format and CVAT integration remain undecided."""

    def export(self, records: Iterable[dict[str, Any]], destination: Path) -> Path:
        """Export records to a CVAT-compatible artifact; implementation pending."""
        raise NotImplementedError("CVAT export is not implemented yet.")
