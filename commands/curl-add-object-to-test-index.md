---
data: >-
  curl "https://c1-in-2.algolianet.com/1/indexes/test/batch" -H
  "x-algolia-api-key: 0580d14b1c12e191b078f193b5e0e3ce" -H
  "x-algolia-application-id: FTCHS7XZX2" -H "Content-Type: application/json"
  --data
  '{"requests":[{"action":"addObject","body":{"firstname":"John","lastname":"Doe","zip_code":null}}]}'
tags:
  - algolia
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.436Z'
id: bf08476d-6aed-486c-881b-585a1213639e
verified: false
validated: true
submitted: true
---
# curl-add-object-to-test-index

## Command

```bash
curl "https://c1-in-2.algolianet.com/1/indexes/test/batch" -H "x-algolia-api-key: 0580d14b1c12e191b078f193b5e0e3ce" -H "x-algolia-application-id: FTCHS7XZX2" -H "Content-Type: application/json" --data '{"requests":[{"action":"addObject","body":{"firstname":"John","lastname":"Doe","zip_code":null}}]}'
```

## Description

Sends a POST request to Algolia's batch endpoint for the 'test' index to add a sample object using a restricted API key, verifying permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-algolia-api-key: KEY"` | API key for authentication | Yes |
| `-H "x-algolia-application-id: ID"` | Application ID | Yes |
| `--data 'JSON'` | Payload with addObject action | Yes |

## Examples

### Basic Usage

```bash
curl "https://c1-in-2.algolianet.com/1/indexes/test/batch" -H "x-algolia-api-key: KEY" -H "x-algolia-application-id: ID" -H "Content-Type: application/json" --data '{"requests":[{"action":"addObject","body":{"firstname":"John","lastname":"Doe"}}]}'
```

### Advanced Usage

Add multiple objects by extending the requests array in the JSON payload.

## Expected Output

{"taskID": 1234567890} on success, indicating the operation is queued.

## Related

- [[commands/curl-add-object-to-unauthorized-index]]
