"""Mask post-processing boundary; algorithm selection remains pending."""
from typing import Any, Protocol


class MaskProcessor(Protocol):
    """Interface for replaceable mask cleanup/transform implementations."""

    def process(self, masks: list[Any]) -> list[Any]:
        """Return processed masks; implementation pending."""
        ...


class OpenCVMaskProcessor:
    """Placeholder for future OpenCV-based mask processing."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Mask processing is not implemented yet.")

    def process(self, masks: list[Any]) -> list[Any]:
        raise NotImplementedError("Mask processing is not implemented yet.")
