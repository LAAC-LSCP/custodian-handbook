# Administering ELSI

This section covers the responsibilities and procedures for administrators of the ELSI platform. Administrator access grants global control over the platform — use it carefully.

---

## Administrator Duties

### Approving and Refusing New Accounts

When a user signs up, their account is pending until an administrator reviews it. To process sign-up requests:

1. Log in and open the **Administrator Panel**
2. Navigate to **Accounts** in the top right section
3. Review each pending request — check the user's affiliation and purpose if provided
4. Approve or refuse accordingly

Refused requests should be accompanied by a reason where possible, so the user can reapply or contact the team if there was a misunderstanding.

### Approving and Refusing Dataset Creation Requests

Users can request the creation of a new dataset, which must be reviewed before being provisioned on the server.

1. In the **Administrator Panel**, go to **Datasets** in the top right section
2. Review pending dataset creation requests
3. Check **Naming**: dataset names should avoid blank spaces and special characters as much as possible. If a submitted name contains spaces, ask the requester to revise it or correct it before approving.
4. Check **Size**: be cautious with the maximum size declared — datasets must not risk saturating the server. If in doubt, start with a conservative allocation and adjust later.
5. Approve or refuse the request.

### Managing Credits

Credits are the currency used to run models on the platform. They are consumed based on the duration of the audio processed and a cost per hour of audio.

Credits can be allocated to accounts in two situations:
- **In exchange for financial participation** to server maintenance costs
- **For free**, in the case of collaborators contributing to the project

To assign credits:

1. In the **Administrator Panel**, go to **Accounts**
2. Select the relevant account
3. Enter the number of credits to assign and confirm

Keep a note of credit allocations and their rationale for accounting and transparency purposes.

### User Roles

There are currently three roles on the platform. The first two are dataset-level roles, the third is a global role:

- **Analyst** — associated with a specific dataset. Can request model runs and access the resulting annotations, but cannot access or download raw data.
- **Manager** — associated with a specific dataset. Can manage the dataset's content, add or remove members, and download raw data.
- **Administrator** — global role. Can manage all datasets, accounts, credits, and platform settings regardless of dataset-level assignments.

Every dataset must have at least one Manager at all times. Managers can add other Managers and Analysts to their dataset directly. Administrators can intervene on any dataset regardless of whether they are assigned as Manager.

Dataset membership is managed from within the dataset itself, in the right-hand panel.

---

## Managing Datasets

Administrators may need to intervene in dataset management when something goes wrong, a dataset is in an inconsistent state, or a user requests help.

### ChildProject Principles

All datasets on ELSI follow the structure and conventions defined by **ChildProject**. Before intervening in a dataset's filesystem, familiarise yourself with its documentation and expected folder layout. Any manual intervention must leave the dataset in a valid ChildProject-compliant state.

→ Refer to the [ChildProject documentation](https://childproject.readthedocs.io) for details on dataset structure, metadata requirements, and validation tools.

### Keeping the Filesystem and Database in Sync

The platform maintains a database that tracks dataset contents and metadata. The filesystem (where the actual data files live) and this database must always be consistent with one another. Discrepancies can cause model runs to fail or data to appear missing.

If you intervene directly on the filesystem (e.g. moving, renaming, or deleting files), make sure the corresponding database records are updated. If you are unsure whether a change will cause a sync issue, consult the technical lead before proceeding.

> **Note:** Never modify dataset files directly on the server without first checking whether the change needs to be reflected in the database. When in doubt, ask.
