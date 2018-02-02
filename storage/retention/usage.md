### Running
```bash
$ lavaory --help
Usage: lavatory [OPTIONS] COMMAND [ARGS]...

  Lavatory is a tool for managing Artifactory Retention Policies.

Options:
  -v, --verbose  Increases logging level.
  --help         Show this message and exit.

Commands:
  purge  Deletes artifacts based on retention policies.
  stats    Get statistics of a repo.
  version  Print version information.
```

### Purging Artifacts
```bash
$ lavatory purge --policies-path=/path/to/policies

To get help

$ lavatory purge --help
Usage: lavatory purge [OPTIONS]

  Deletes artifacts based on retention policies.

Options:
  --policies-path TEXT            Path to extra policies directory.
  --dryrun / --nodryrun           Dryrun does not delete any artifacts.
                                  [default: True]
  --default / --no-default        Applies default retention policy.  [default:
                                  True]
  --repo TEXT                     Name of specific repository to run against.
                                  Can use --repo multiple times. If not
                                  provided, uses all repos.
  --repo-type [local|virtual|cache|any]
                                  The types of repositories to search for.
                                  [default: local]
  --help                          Show this message and exit.
```
If you want to run Lavatory against a specific repository, you can use `--repo <repo_name>`. You can specify `--repo` as multiple times to run against multiple repos. If `--repo` is not provided, Lavatory will run against all repos in Artifactory.