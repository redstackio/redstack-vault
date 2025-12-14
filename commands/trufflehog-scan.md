---
id: cmd-trufflehog-scan-001
data: trufflehog filesystem ./repo
tags:
  - secrets
  - scan
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.863Z'
verified: false
validated: true
submitted: true
---
# trufflehog-scan

## Command

```bash
trufflehog filesystem ./repo
```

## Description

Scans a directory or Git repository for leaked secrets using entropy analysis and regex detectors for API tokens and credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `filesystem` | Scan mode for local directories | Yes |
| `./repo` | Path to the repository directory | Yes |

## Examples

### Basic Usage

```bash
trufflehog filesystem ./cloned-repo
```

### Advanced Usage

```bash
trufflehog git https://github.com/target/repo.git --since-commit HEAD~10  # Scan specific commits
```

## Expected Output

Tracked search result for "API Token"\nHIGH: abc123... at ./config.py:10

## Related

- [[commands/git-clone]]
- [[tools/truffleHog]]
