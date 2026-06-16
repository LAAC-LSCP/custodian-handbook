---
title: Synchronizing between custodian
description: set of rules and principles put in place by custodians to ensure synchronicity of the datasets
icon: lucide/refresh-ccw
---

# Synchronization of Datasets across custodians

!!! Warning Disclaimer

    This section was written without accounting for possible new datasets being integrated into the consortium. The process for adding a new dataset has not been defined.

## Raw data archiving

The raw data (audios), is only shared through the three archives. The copies stored there are the ground truth and are not to be modified. When acquire data from those archives, the expectation is to place them inside their dedicated folder in the complete datasets, i.e. the `recordings/raw` and `recordings/converted/standard` folders for respectively the raw collected data and the converted to standard (wav format, mono channel, 16kHz sampling) version.

## Dataset structure and sharing

The dataset structure (including the names of the data files) are stored and shared through [GIN](https://gin.g-node.org/). All custodians have access to the repos stored there.

### Ensuring no data is pushed to GIN

On GIN, if you are worried about unknowingly pushing data there (for example because you use nested datasets), first know that this can only happen if you explicitly go into a dataset and push it to its GIN origin url, and not through submodules.

There are 2 steps that will help prevent this:

1. On GIN, make you branch protected (in the dataset page, go to **settings** -> **branches** -> **Protected branches** and make sure the branch you use is protected). This means that it will require you to force push to this branch to modify it.
2. On your local copy of the data (inside the dataset folder), to avoid pushing any annexed data to the remote, set the required and wanted content for `git annex` to match nothing. for this, if your remote is named **origin**(`git remote` lists your remotes), run `git annex required origin "exclude=*"` and `git annex wanted origin "exclude=*"`. this will ensure no data content will be pushed.

### Branches

Multiple branches will be created for each dataset:
 1. `main` branch: this branch is the main version of the dataset, it must stay in a valid state and be usable for analysis. Custodians may merge to this branch but must never directly edit it.
 2. personal branch: Each custodian will own a branch for each dataset. They are free to use and modify that branch freely. They are encouraged to maintain the branch updated in the gin server as well.
 3. working branches: Custodian are free to create and share working branches on GIN, they must preface the branch name with their name

Custodians have access to branches of the others, they can at anytime integrate their work into their version of the dataset by merging. When achieving important advances in the dataset, their are encouraged to merge their work into the main branch
