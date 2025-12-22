---
data: perl -e 'print "\r\n"' >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
tags:
  - payload
type: command
executor: bash
platforms:
  - Linux
id: 1058a989-8257-4a6b-bf1e-4510ac6cb12b
created_at: '2025-12-13T09:01:22.337Z'
updated_at: '2025-12-13T09:01:22.337Z'
verified: false
validated: true
submitted: true
---
# Perl Append CRLF

## Command

```bash
perl -e 'print "\r\n"' >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

## Description

Appends a carriage return and newline to the file using Perl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Execute the following Perl code | Yes |

## Examples

### Basic Usage

```bash
perl -e 'print "\r\n"' >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
```

## Expected Output

File appended with \r\n.

## Related

- [[procedures/Craft-Oversized-Trailer-Payload]]
