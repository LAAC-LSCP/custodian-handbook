# How to Add New Developed Tools on the Server

This guide covers how to deploy a new script, tool, or pipeline to the shared ExELang server so that other team members can access and use it.

## Before You Start

- Confirm your tool is ready for shared use: it should be documented, tested on your local machine, and not contain any hardcoded local paths or credentials.
- Ensure you have SSH access to the server (see [How to Onboard a New Student](#how-to-onboard-a-new-student) if you need to set this up).
- For major new tools or pipelines, discuss with the PI or technical lead before deploying, to agree on the right location and naming conventions.

## Repository Structure

All tools live under `/shared/tools/` on the server, organised by type:

```
/shared/tools/
├── analysis/       ← R and Python analysis scripts
├── processing/     ← Audio/video preprocessing pipelines
├── scoring/        ← Automated scoring tools
└── utilities/      ← Misc helper scripts
```

Place your tool in the most appropriate subfolder. If none fits, raise it with the technical lead.

## Step-by-Step Deployment

### 1. Prepare your repository

Your tool should have at minimum:
- A `README.md` explaining what the tool does, its inputs/outputs, dependencies, and a usage example
- A `requirements.txt` (Python) or `renv.lock` / `DESCRIPTION` (R) listing dependencies
- No hardcoded absolute paths — use relative paths or a config file

### 2. Push to the shared Git repository

The server tools are version-controlled on the project's internal GitLab instance.

```bash
# Clone the tools repo (first time only)
git clone git@gitlab.exelang.org:tools.git

# Create a branch for your tool
git checkout -b add/my-tool-name

# Copy your tool into the correct subfolder
# Commit and push
git add .
git commit -m "Add [tool name]: brief description"
git push origin add/my-tool-name
```

Then open a Merge Request on GitLab and assign it to the technical lead for review.

### 3. After merge — install dependencies on the server

Once your MR is merged, SSH into the server and run the setup:

```bash
ssh exelang-server
cd /shared/tools/<subfolder>/<your-tool>

# For Python tools:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# For R tools:
Rscript -e "renv::restore()"
```

### 4. Test on the server

Run a quick sanity check using a small test file before announcing the tool to the team. Use paths under `/shared/test-data/` for this purpose — do not use real participant data for deployment testing.

### 5. Announce to the team

Send a short email to the team list describing:
- What the tool does
- Where it lives (`/shared/tools/...`)
- How to run it (or link to the README)
- Any known limitations or works-in-progress

> **Note:** If your tool processes participant data, it must comply with the data handling rules outlined in the Collaborator Responsibilities policy. Do not write output files containing participant IDs to any location outside `/shared/outputs/`.
