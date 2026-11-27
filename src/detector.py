"""Replaceable object detection adapter boundary.

No model loading or inference is implemented in this scaffold. Keep GPU-specific
initialization inside the Colab workflow and pass runtime-ready dependencies here.
"""
from typing import Any, Protocol


class Detector(Protocol):
    """Interface expected from a future detector implementation."""

    def detect(self, image: Any, text_prompt: str) -> list[dict[str, Any]]:
        """Return normalized detections for one image; implementation pending."""
        ...


class GroundingDinoDetector:
    """Placeholder adapter for a future pretrained Grounding DINO implementation."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Grounding DINO loading is not implemented yet.")

    def detect(self, image: Any, text_prompt: str) -> list[dict[str, Any]]:
        raise NotImplementedError("Detection is not implemented yet.")
