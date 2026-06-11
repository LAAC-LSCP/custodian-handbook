---
title: Adding new models to the platform
description: steps and explanations of what to do to have a new model added to the ELSI platform
icon: lucide/brain-circuit
---

# Adding new models to the platform

This section covers the full process of integrating a new analysis model into ELSI, from implementation to deployment. The process involves two actors: the **model developer** who prepares and submits the model, and the **platform maintainers** who deploy it.

---

## Model Developer: Implementation

### Dockerizing the Model

All models must be packaged as Docker images to run on the platform. The implementation must follow the requirements defined in the [analysis-service-core repository](https://github.com/laac-lscp/analysis-service-core), which specifies the interface your model must expose. This includes:

- **GPU support** — implement if the model can benefit from it
- **Failure reporting** — the model must report errors in the expected format so the platform can surface them to users
- **Effort model** — an estimate of the compute cost relative to input duration, used to calculate credit consumption
- **Progress reporting** — the model must report progress so users can track long-running jobs

Read the repository documentation carefully before starting — the interface requirements are strict and must be met for the model to be accepted onto the platform.

### Annotation Output Format

Check whether your model's output format is already supported by ChildProject by consulting the [list of supported converters](https://github.com/LAAC-LSCP/ChildProject/blob/59783349d42e0f5e4e9e1db3ff8d06362404e6ed/ChildProject/converters.py#L9).

If your format is **not** on that list, you must add a conversion step inside your Docker image that transforms the model output into the standard ChildProject annotation CSV format. The required fields are documented in the [ChildProject annotation format reference](https://childproject.readthedocs.io/en/latest/format.html#annotations-format).

### Submitting to the Platform

Once your Docker image is built and tested, submit it to the platform maintainers. Provide:

- The Docker image or instructions to build/pull it
- The name to use for the service in the Swarm compose file
- A short description of the model and its expected output format

