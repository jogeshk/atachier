# Atachier

## Hardware-Accelerated Spatial Graph Document Extraction Engine

Atachier is a local-first document processing engine designed to represent documents as **2D spatial structures** rather than treating them as plain text.

Instead of reducing a document to:

    Document → Text → Output

Atachier is designed around:

    Document
        ↓
    Pages
        ↓
    Elements
        ↓
    Geometry
        ↓
    Layout
        ↓
    Spatial Relationships
        ↓
    2D Spatial Graph
        ↓
    Spatial Inference
        ↓
    Optional AI / GNN Reasoning
        ↓
    Structured Output

The central idea is simple:

> The physical arrangement of information inside a document is meaningful data.

A title above a paragraph, a caption below an image, a label beside a figure, a table inside a region, or two columns positioned next to each other all contain spatial information.

Atachier is being engineered to preserve and reason about that information.

---

# Why Atachier?

Traditional document extraction often focuses primarily on text.

That approach can lose important information about where things are located.

For example, consider a document containing:

- a title
- multiple paragraphs
- two columns
- a table
- an image
- a caption
- headers
- footers
- labels

The text alone does not fully describe the document.

Atachier aims to preserve the relationship between:

    What something is
    Where it is
    What surrounds it
    What it is spatially related to
    How it participates in the document structure

This creates a foundation for spatial document understanding.

---

# Core Concept

Atachier's central representation is:

    Elements
        +
    Geometry
        +
    Layout
        +
    Spatial Relationships
        +
    Graph

A document can therefore eventually be represented as a 2D spatial graph.

Conceptually:

    ┌─────────────────────┐
    │      Document       │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │        Pages        │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │      Elements       │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │      Geometry       │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │       Layout        │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │Spatial Relationships│
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │   Spatial Graph     │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ Spatial Inference   │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ Structured Output   │
    └─────────────────────┘

---

# 2D First

Atachier is currently a **2D document-processing system**.

The current architecture focuses on document geometry such as:

- X/Y coordinates
- width
- height
- bounding boxes
- page geometry
- element positions
- spatial relationships
- 2D graph structures

3D document processing is intentionally outside the current scope.

The project will not introduce unnecessary 3D abstractions merely for future possibilities.

This keeps the current architecture focused and easier to test, optimize, and maintain.

---

# Local-First Architecture

Atachier is designed to process documents locally.

The core workflow is intended to work without requiring:

- a Atachier server
- a Atachier cloud service
- remote document processing
- uploading documents to a remote service
- external processing APIs
- an internet connection for core processing

PyPI is a distribution mechanism, not a remote processing backend.

The long-term goal is:

```python
import atachier

doc = atachier.load("document.pdf")
result = doc.extract()
