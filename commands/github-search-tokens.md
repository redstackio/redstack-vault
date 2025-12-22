---
data: >-
  gh search code "access_token OR api_key" --repo organization/repo-name --limit
  100
tags:
  - discovery
  - github
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: fee88325-46fd-4be6-a15c-9876437b7998
created_at: '2025-12-14T17:32:10.806Z'
updated_at: '2025-12-14T17:32:10.806Z'
verified: false
validated: true
submitted: true
---
# github-search-tokens

## Command

```bash
gh search code "access_token OR api_key" --repo organization/repo-name --limit 100
```

## Description

This command uses the GitHub CLI to search for code containing potential token or key patterns within a specified public repository, aiding in the discovery of exposed credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `search code` | Initiates code search | Yes |
| `"access_token OR api_key"` | Query string for token patterns | Yes |
| `--repo organization/repo-name` | Targets a specific repository | Yes |
| `--limit 100` | Limits results to 100 matches | No |

## Examples

### Basic Usage

```bash
gh search code "token" --repo reverb/experimental
```

### Advanced Usage

```bash
gh search code "api_key OR secret" --repo organization/repo --owner reverb --limit 500
```

## Expected Output

A list of search results showing file paths, line numbers, and code snippets with matching strings, e.g.,:

```
repo-name/file.js:10:const token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...';
```

## Related

- [[commands/git-clone-repo]]
- [[procedures/Discover-Exposed-Tokens-in-Public-GitHub-Repositories]]
