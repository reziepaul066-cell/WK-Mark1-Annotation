# WK-Mark1 automated annotation scaffold

This repository contains project code and configuration only. Keep the image dataset on its external SSD or in an explicitly chosen cloud storage location; do not copy dataset files into this repository.

## Architecture

- `src/detector.py`: detector adapter boundary (planned Grounding DINO adapter).
- `src/segmenter.py`: segmentation adapter boundary (planned SAM2 adapter).
- `src/mask_processor.py`: post-processing boundary for masks (planned OpenCV-based operations).
- `src/batch_processor.py`: orchestration boundary for image batches and manifests.
- `src/cvat_exporter.py`: boundary for exporting predictions for CVAT review.
- `configs/annotation_config.yaml`: paths and model/runtime settings; use paths available to the active runtime.
- `notebooks/annotation_pipeline.ipynb`: Google Colab entry point for GPU-bound execution.

The modules define replaceable component boundaries. They do not implement inference or annotation algorithms yet.

## GitHub and Colab workflow

1. Keep this repository in GitHub and synchronize it with Colab by cloning or pulling the repository in a Colab session.
2. Select a GPU runtime in Colab when GPU inference is later implemented. GPU setup and model execution belong in the notebook/runtime workflow, not in local project imports.
3. Make the dataset available to the Colab runtime through an explicitly configured storage or transfer method. Direct access to the external SSD is not assumed. The dataset location is intentionally unset in the configuration.
4. Store generated predictions and exports under the configured output location, or another explicitly chosen storage location. Review annotations in CVAT.

Do not commit image datasets, credentials, model weights, or generated annotation batches to GitHub. The `outputs/` directory is kept with a placeholder only; generated files are ignored by Git.

## Development status

This is an initial scaffold. Dependencies are documented as intentions in `requirements.txt` but have not been installed or pinned. Detector, segmenter, mask processing, batch processing, and CVAT export behavior remain placeholders.
