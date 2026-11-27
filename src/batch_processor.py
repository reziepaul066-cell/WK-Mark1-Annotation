"""Batch orchestration boundary for runtime-accessible images and manifests."""
from pathlib import Path
from typing import Any, Iterable


class BatchProcessor:
    """Coordinates replaceable pipeline components; behavior is not implemented."""

    def __init__(self, detector: Any, segmenter: Any, mask_processor: Any) -> None:
        self.detector = detector
        self.segmenter = segmenter
        self.mask_processor = mask_processor

    def process(self, image_paths: Iterable[Path]) -> list[dict[str, Any]]:
        """Process a batch and return records; implementation pending."""
        raise NotImplementedError("Batch processing is not implemented yet.")
