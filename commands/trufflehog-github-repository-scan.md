---
id: 4a9bbb14-13b6-4ab6-80aa-5efa52ef14c7
name: trufflehog-github-repository-scan
type: command
executor: bash
data: 'trufflehog github --repo=https://github.com/owner/repo-name'
output: null
created_at: '2023-04-06T03:55:50.999239+00:00'
updated_at: '2023-04-10T20:21:07.107069+00:00'
platforms:
  - Linux
  - macOS
tags:
  - secrets-scanning
  - github
verified: true
validated: true
---

# trufflehog-github-repository-scan

## Command

```bash
trufflehog github --repo=https://github.com/owner/repo-name
```

## Description

Scans a specific GitHub repository for secrets by fetching its git history via the GitHub API. Useful for remote detection without local cloning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `github` | Specifies GitHub as the source | Yes |
| `--repo` | Full URL of the GitHub repository | Yes |

## Examples

### Basic Usage

```bash
trufflehog github --repo=https://github.com/trufflesecurity/test_keys
```

### With Token for Private Repos

```bash
trufflehog github --repo=https://github.com/owner/private-repo --token=GITHUB_TOKEN
```

## Expected Output

JSON output with secret details:
```
{"SourceMetadata":{"Git":{"RepositoryURL":"https://github.com/owner/repo"}},"Type":"API Key","Decoded":"examplekey"}
```
Empty if no secrets detected.
