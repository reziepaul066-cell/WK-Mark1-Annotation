"""Replaceable segmentation adapter boundary.

No model loading or segmentation logic is implemented in this scaffold.
"""
from typing import Any, Protocol


class Segmenter(Protocol):
    """Interface expected from a future segmentation implementation."""

    def segment(self, image: Any, prompts: list[dict[str, Any]]) -> list[Any]:
        """Return masks corresponding to prompts; implementation pending."""
        ...


class Sam2Segmenter:
    """Placeholder adapter for a future pretrained SAM2 implementation."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("SAM2 loading is not implemented yet.")

    def segment(self, image: Any, prompts: list[dict[str, Any]]) -> list[Any]:
        raise NotImplementedError("Segmentation is not implemented yet.")
