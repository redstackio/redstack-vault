---
data: >-
  d = new URLSearchParams(location.search);
  ["code","access_token","state","refresh_token","id_token"].forEach((function(e){
  d.delete(e) }));
tags:
  - javascript
  - sanitization
type: command
executor: javascript
platforms:
  - Web
id: d96e162b-3b71-42b0-900d-bd66dc801762
created_at: '2025-12-11T06:10:22.307Z'
updated_at: '2025-12-11T06:10:22.307Z'
verified: false
validated: true
submitted: true
---
# sanitize-oauth-params

## Command

```javascript
d = new URLSearchParams(location.search); ["code","access_token","state","refresh_token","id_token"].forEach((function(e){ d.delete(e) }));
```

## Description

Sanitizes URL search parameters by deleting sensitive OAuth keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```javascript
let d = new URLSearchParams(location.search); ["code","access_token","state","refresh_token","id_token"].forEach(e => d.delete(e));
```

## Expected Output

Cleaned URLSearchParams.

## Related

- [[procedures/Exploit-XSS-to-Steal-OAuth-Tokens]]
