## Lavatory

### Introduction
Lavatory is a tool to solve the issue of artifact retention in Artifactory.

Retention policy is need for the following reasons:
* Too many artifacts in a repo can cause slow indexing and make delivering application slower.
* Indefinitely keeping all artifacts leads to a build up of stale or broken artifacts.
* Cost effectie, storage never comes free.

### Lavatory Features:
Lavatory has the following features:
* Uses Python plugins for repository policies. One plugin per repository that can have as much Python logic as necessary.
* Time-based retention. Easy helper function for applying a time-based retention policy, such as "keep all artifacts created in the last 120 days".
* Count-based retention. Easy helper function for keep last `N` number of artifacts, such as "keep the last 5 build artifacts.
* AQL based retention. You can use the `Artifactory query language` for searching artifacts to delete. This can also be combined with time-based and count-based retention.
* A default policy that applies to all repos without a specific policy.

### Lavatory Policy:
Each policy in Lavatory is a Python plugin. The plugin should be named `<repo_name>.py`. Each policy needs one function, `def purgelist(artifactory)` and this need sto return a list of artifacts to delete. Other than that, the policies can do anything that Python can do. The default policy is named `default.py` and applied to all repositories without a specific retention policy.

### Some Example Policies
* Keep last 120 dyas of artifacts:
```python
def purgelist(artifactory):
    """Policy to purge all artifacts older than 120 days"""
    purgeable = artifactory.time_based_retention(keep_days=120)
    return purgeable
```
* Keep 5 most recent artifacts:
```python
def purgelist(artifactory):
    """Policy to keep just the 5 most recent artifacts."""
    purgeable = artifactory.count_based_retention(retention_count=5)
    return purgeable
```
* Purge artifacts based on environments deployed to:
```python
def purgelist(artifactory):
    """If deployed to prod, keep artifact forever,
    if deployed to stage, keep 30 days,
    if never deployed, keep 14 days."""

    not_deployed = [ { "@deployed": { "$nmatch": "*" }}]

    only_dev =  [ { "@deployed": { "$match": "*stage*"} },
                { "@deployed": {"$nmatch": "*prod*"} } ]

    undeployed = artifactory.time_based_retention(keep_days=14,
        extra_aql=not_deployed)
    
    only_stage = artifactory.time_based_retention(keep_days=30,
        extra_aql=only_dev)

    all_purgable = undeployed + only_stage
    return sorted(all_purgable, key=lambda k: k['path'])
```
* Move artifacts to different repository after 3 days:
```python
def purgelist(artifactory):
    """Moves artifacts to yum-local after 3 days."""
    movable = artifactory.time_based_retention(keep_days=3)
    artifactory.move_artifacts(artifacts=movable,
        dest_repository='yum-local')
    return []
```

### How to Run Lavatory:
Lavatory is just a CLI tool. We run this nightly in a Jenkins job but could be done from any shell.

Lavatory can be installed from PyPI: `pip install lavatory`

Authentication to Artifactory looks for 3 environment variables: `ARTIFACTORY_URL, ARITFACTORY_USERNAME, ARTIFACTORY_PASSWORD`