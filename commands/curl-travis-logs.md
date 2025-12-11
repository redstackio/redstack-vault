---
data: 'curl -s https://api.travis-ci.org/repos/REPO_OWNER/REPO_NAME/builds | jq'
tags:
  - recon
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 44580105-5e6d-4870-8437-ca7f9f935760
created_at: '2025-12-11T06:10:15.500Z'
updated_at: '2025-12-11T06:10:15.501Z'
verified: false
validated: true
submitted: true
---
# curl-travis-logs

## Command

```bash
curl -s https://api.travis-ci.org/repos/REPO_OWNER/REPO_NAME/builds | jq
```

## Description

Fetches build metadata from Travis CI for a specified repository, allowing analysis of public logs for leaked information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `REPO_OWNER` | Repository owner (e.g., grammarly) | Yes |
| `REPO_NAME` | Repository name | Yes |

## Examples

### Basic Usage

```bash
curl -s https://api.travis-ci.org/repos/grammarly/repo/builds | jq
```

### Advanced Usage

```bash
curl -s https://api.travis-ci.org/repos/grammarly/repo/builds | jq '.builds[] | {id: .id, state: .state}'
```

## Expected Output

JSON array of build objects, including IDs and states, which can be used to fetch full logs.

## Related
- [[procedures/Identify-Leaked-Tokens-in-CI-Build-Logs]]
