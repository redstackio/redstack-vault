---
data: GET /v2/tabbed/home HTTP/1.1
tags:
  - api-query
  - token-usage
type: command
executor: http
platforms:
  - Web
id: 78907bd1-85fd-4e4e-94f0-3a0944840915
created_at: '2025-12-13T09:01:26.137Z'
updated_at: '2025-12-13T09:01:26.137Z'
verified: false
validated: true
submitted: true
---
# GET Tabbed Home

## Command

```http
GET /v2/tabbed/home HTTP/1.1
```

## Description

Retrieves UserID using a stolen X-Access-Token from the Zomato API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses headers like X-Access-Token | No |

## Examples

### Basic Usage

```http
GET /v2/tabbed/home HTTP/1.1
```

## Expected Output

Response containing UserID in JSON.

## Related

- [[procedures/Perform-Account-Takeover-with-Stolen-Tokens]]
