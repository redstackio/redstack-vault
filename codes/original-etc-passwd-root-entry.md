---
id: c9e15ad2-75fb-4007-a3c9-83808da5433b
name: Original /etc/passwd Root Entry
type: code
language: passwd
verified: true
created_at: '2020-03-16T07:01:57.512320+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - configuration
  - example
validated: true
---

# Original /etc/passwd Root Entry

## Code

```passwd
root:x:0:0:root:/root:/bin/bash
```

## Description

This is the standard format for the root user entry in /etc/passwd on a Linux system. The 'x' in the second field indicates that the actual password hash is stored in /etc/shadow. This serves as the baseline before modification in password change procedures.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static example line; no variables to substitute. | N/A |

## Usage

Use this as a reference when identifying the target line in /etc/passwd for editing. View current entries with `grep root /etc/passwd` before applying changes in procedures like [[procedures/Change-Password-in-Writable-Etc-Passwd]].

## Detection

No direct detection needed as this is the default system configuration. Monitor for deviations in file integrity checks.

## Related

- [[procedures/Change-Password-in-Writable-Etc-Passwd]]
