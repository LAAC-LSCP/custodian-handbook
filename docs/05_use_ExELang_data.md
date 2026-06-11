# Using ExELang Data

This section explains how to access and navigate ExELang datasets, whether you are working with them locally or on the platform.

---

## Dataset Structure

### Recordings

All audio files live under the `recordings/` folder:

- `recordings/raw/` — original recordings as collected in the field, in their native format
- `recordings/converted/standard/` — standardised versions of the recordings: mono channel, 16 kHz, WAV format. These are the files used as input for model runs on the platform.

### Annotations

Annotations are stored under the `annotations/` folder, organised into **sets**. Each set corresponds to a particular annotation campaign, tool, or model output, and follows a consistent structure:

```
annotations/
└── <set-name>/
    ├── converted/   ← standard CSV annotations (always present)
    └── raw/         ← original annotation files in their native format (when relevant)
```

The `converted/` folder is the canonical source for working with annotations programmatically. Files in `raw/` are kept for reference and reproducibility but should not be used directly for analysis.

### Metadata

The `metadata/` folder contains three index files that together describe the full dataset:

- **`recordings.csv`** — the index of all recordings in the dataset, with their paths and associated metadata
- **`children.csv`** — participant-level metadata
- **`annotations.csv`** — the index linking recordings to their annotations. For each annotation file, it specifies which recording it annotates, which annotation set it belongs to, what label set is used, and the time window covered. This is the key file for tracing what annotates what.

---

## Working with the Data in Python

[ChildProject](https://childproject.readthedocs.io) is the recommended library for working with ExELang datasets programmatically. It provides tools for loading and filtering annotations, validating dataset structure, computing statistics, and more.

```python
from ChildProject.projects import ChildProject
from ChildProject.annotations import AnnotationManager

project = ChildProject('path/to/dataset')
am = AnnotationManager(project)

am.read()

# Load annotations from a specific set
annotations = am.get_segments(sets=['my-set'])
```

Refer to the [ChildProject documentation](https://childproject.readthedocs.io) for the full API reference and usage examples.
