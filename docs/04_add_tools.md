# Adding a New Model to the Platform

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

---

## Administrator: Registering the Model

Once the maintainers have deployed the image (see below), the model must be registered in the platform so it appears as an available option for users.

In the **Administrator Panel**, go to **Analytics → Analytics Types** and add a new entry with the following fields:

- **`label`** — the display name shown to users in the interface
- **`model_name`** — the name given to the service in the Docker Swarm compose file (provided by the maintainers)
- **`import_key`** — the annotation format of the model's output. Use `csv` if the output has been converted to the standard ChildProject CSV format.

When setting the **credit cost per hour** of audio, consider:

- How computationally heavy the model is to run
- How long it takes relative to audio duration
- Whether you want to encourage adoption of a newer model — a slightly lower price for a newer model with equivalent computational cost is a reasonable incentive, even if it means a short-term cost reduction

---

## Platform Maintainers: Deployment

Once a model submission is received, using the clone repo of [https://github.com/laac-lscp/analysis-service](https://github.com/laac-lscp/analysis-service):

1. **Build or pull the Docker image** on the server hosting the platform
2. **Add the service to the Swarm compose file**, giving it the agreed `model_name` as the service name
3. **Start the service** alongside the analysis service so it is reachable by the platform
4. Confirm to the model developer and administrators that the service is live, so the Analytics Type entry can be created

> **Note:** The `model_name` set in the compose file must exactly match what is entered in the `model_name` field of the Analytics Type record. A mismatch will cause model runs to fail silently.
