---
id: becf4e29-33a3-4b23-8448-ec458fa75296
name: Modified /etc/passwd Root Entry with SHA512 Hash
type: code
language: passwd
verified: true
created_at: '2020-03-17T05:46:47.579871+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - configuration
  - example
  - persistence
validated: true
---

# Modified /etc/passwd Root Entry with SHA512 Hash

## Code

```passwd
root:$6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/:0:0:root:/root:/bin/bash
```

## Description

This example shows a modified root entry in /etc/passwd where the 'x' has been replaced with a full SHA512-crypt hash. This allows direct password authentication via /etc/passwd, bypassing /etc/shadow, and is used for persistence or escalation when the file is writable.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $6$SALT$HASH | The SHA512-crypt hash; replace with output from [[commands/openssl-generate-sha512-crypt-hash]] | $6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/ |

## Usage

Insert this format into /etc/passwd using a text editor or sed after generating the hash. Test with `su root` using the corresponding plaintext password (e.g., 'secretpass' for this example hash). Revert if needed from backup.

## Detection

- File integrity monitoring tools (e.g., AIDE) alerting on /etc/passwd changes.
- Audit logs showing writes to /etc/passwd by non-root processes.
- Unexpected successful logins with new credentials.

## Related

- [[procedures/Change-Password-in-Writable-Etc-Passwd]]
