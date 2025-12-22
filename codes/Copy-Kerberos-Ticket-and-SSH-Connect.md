---
id: 4db516f4-192e-4b09-ad89-d9f14aa9c09d
name: Copy-Kerberos-Ticket-and-SSH-Connect
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:31.279075+00:00'
updated_at: '2023-04-10T20:38:00.046573+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - ssh
  - lateral-movement
validated: true
---

# Copy-Kerberos-Ticket-and-SSH-Connect

## Code

```bash
cp user.ccache /tmp/krb5cc_1045
ssh -o GSSAPIAuthentication=yes user@domain.local -vv
```

## Description

This bash script snippet copies a Kerberos ticket cache to the expected location and then initiates an SSH connection using GSSAPI authentication. It is designed for use on a Linux attacker machine after transferring a ticket from a compromised Windows host, enabling seamless lateral movement to Kerberos-integrated SSH servers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| user.ccache | Path to the source Kerberos ticket cache file | /home/attacker/user.ccache |
| /tmp/krb5cc_1045 | Destination cache path (UID-based) | /tmp/krb5cc_1000 |
| user | SSH username/principal | DOMAIN\\attacker |
| domain.local | Target SSH server hostname | target-server.domain.local |

## Usage

Save as a script (e.g., kerb_ssh.sh), make executable (`chmod +x kerb_ssh.sh`), and run after placing user.ccache in the working directory. Ensure KRB5CCNAME is set if needed (`export KRB5CCNAME=/tmp/krb5cc_1045`). Used in post-exploitation phases for credential reuse across platforms.

## Detection

- Monitor for cp commands accessing /tmp/krb5cc_* files from unusual sources.
- SSH logs showing GSSAPI auth from non-standard IPs or with mismatched principals.
- File transfer indicators (e.g., SMB/HTTP) of .ccache files from Windows to Linux hosts.
- Kerberos pre-auth logs for ticket usage anomalies.

## Related

- [[procedures/Windows-SSH-with-Kerberos-Authentication]]
