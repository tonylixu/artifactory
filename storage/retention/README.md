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