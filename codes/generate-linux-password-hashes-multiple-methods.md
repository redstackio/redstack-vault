---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hashing
  - privesc
validated: true
---

# generate-linux-password-hashes-multiple-methods

## Code

```bash
openssl passwd -1 -salt hacker hacker
mkpasswd -m SHA-512 hacker
python2 -c 'import crypt; print crypt.crypt("hacker", "$6$salt")'
```

## Description

This code snippet provides multiple methods to generate Linux-compatible password hashes for use in /etc/passwd or /etc/shadow during account creation in privilege escalation scenarios. The first uses OpenSSL for MD5, the second mkpasswd for SHA-512, and the third Python's crypt module for SHA-512. Useful when one tool is unavailable on the target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| hacker | Password to hash | hacker |
| hacker (salt) | Salt value for MD5 | hacker |
| $6$salt | SHA-512 salt prefix | $6$salt |

## Usage

Run each line individually in a shell to generate hashes. Use the output in echo commands to add users, e.g., echo 'user:OUTPUT_HASH:0:0:...'. Ideal for red team ops where target lacks certain tools; test hashes with su before full exploit.

## Detection

- Monitor process creation for openssl, mkpasswd, or python crypt executions in low-priv contexts.
- Log file writes to /etc/passwd following hash generation.
- Anomaly detection on unusual crypt module imports in Python scripts.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/generate-md5-password-hash]]
