---
id: 6e15bcf8-e341-42d2-bf73-8f3e675cf465
name: trufflehog-github-organization-scan
type: command
executor: bash
data: trufflehog github --org=organization-name
output: null
created_at: '2023-04-06T03:55:51.000548+00:00'
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

# trufflehog-github-organization-scan

## Command

```bash
trufflehog github --org=organization-name
```

## Description

Scans all accessible repositories in a GitHub organization for secrets, aggregating findings across multiple repos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `github` | Specifies GitHub source | Yes |
| `--org` | Name of the GitHub organization | Yes |

## Examples

### Basic Usage

```bash
trufflehog github --org=trufflesecurity
```

### With Authentication

```bash
trufflehog github --org=org-name --token=GITHUB_TOKEN
```

## Expected Output

Per-repo secret listings in JSON:
```
{"SourceType":"Git","Type":"Private Key","Decoded":"-----BEGIN RSA-----"}
```
Summarizes total findings at the end.
