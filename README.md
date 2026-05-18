# Polarization-HDR-SR-Baseline

A baseline repository for polarization-guided high dynamic range image super-resolution experiments.

## Overview

This project explores how polarization cues can be used to improve HDR image super-resolution. The long-term goal is to build a reproducible baseline for combining polarization imaging, super-resolution, and high dynamic range reconstruction.

## Research Motivation

Conventional image super-resolution methods mainly rely on RGB intensity information. However, polarization images can provide additional physical cues, such as surface reflection, material properties, and scene structure. These cues may be useful for recovering high-frequency details and overexposed regions in HDR reconstruction.

## Planned Features

- Load and inspect polarization image data
- Support high bit-depth image inputs
- Prepare baseline preprocessing scripts
- Organize experiment configurations
- Compare RGB-only and polarization-guided reconstruction methods

## Repository Structure

```text
.
|-- README.md
|-- scripts/
|   `-- read_image.py
|-- data/
|   `-- README.md
`-- results/
    `-- README.md
```

## Next Steps

- Add sample data loading examples
- Document polarization image formats
- Create a baseline preprocessing pipeline

## Status

This repository is currently in the initial setup stage.
真难学啊