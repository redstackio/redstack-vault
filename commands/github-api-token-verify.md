---
data: 'curl -H "Authorization: token TOKEN" https://api.github.com/user/repos'
tags:
  - verification
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 880b7998-6595-46b2-970c-eeec5e8b940b
created_at: '2025-12-11T06:10:15.498Z'
updated_at: '2025-12-11T06:10:15.498Z'
verified: false
validated: true
submitted: true
---
# github-api-token-verify

## Command

```bash
curl -H "Authorization: token TOKEN" https://api.github.com/user/repos
```

## Description

Verifies a GitHub token by querying the user's repositories, confirming validity and access scope.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `TOKEN` | The GitHub token to verify | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: token ghp_exampletoken" https://api.github.com/user/repos
```

### Advanced Usage

```bash
curl -H "Authorization: token ghp_exampletoken" https://api.github.com/user/repos | jq '.[] | .full_name'
```

## Expected Output

JSON list of repositories if valid; 401 error if invalid.

## Related
- [[procedures/Verify-Token-Validity-and-Access-Scope]]
