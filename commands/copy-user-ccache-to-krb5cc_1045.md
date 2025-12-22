---
id: generated-uuid-1
name: copy-user-ccache-to-krb5cc_1045
type: command
executor: bash
data: cp user.ccache /tmp/krb5cc_1045
output: null
created_at: '2023-04-06T03:56:31.279197+00:00'
updated_at: '2023-04-10T20:38:00.094828+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# copy-user-ccache-to-krb5cc_1045

## Command

```bash
cp user.ccache /tmp/krb5cc_1045
```

## Description

This command copies a Kerberos ticket cache file (ccache) from its current location to a temporary credential cache file expected by the SSH client's GSSAPI mechanism. It is used after transferring the ticket from a Windows host to prepare for Kerberos-based SSH authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user.ccache | Source Kerberos ticket cache file (exported from Windows) | Yes |
| /tmp/krb5cc_1045 | Destination path for the credential cache, named by UID (e.g., 1045 for attacker user) | Yes |

## Examples

### Basic Usage

```bash
cp user.ccache /tmp/krb5cc_1045
```

### Advanced Usage

If the source file has a different name or path:

```bash
cp /path/to/extracted-ticket.ccache /tmp/krb5cc_$(id -u)
```

## Expected Output

No output on success (standard cp behavior). Verify with:

```bash
ls -l /tmp/krb5cc_1045
-rw------- 1 user user 1234 Oct 10 12:00 /tmp/krb5cc_1045
```

Error if source missing: "cp: cannot stat 'user.ccache': No such file or directory".

## Related

- [[procedures/Windows-SSH-with-Kerberos-Authentication]]
- [[commands/ssh-with-gssapi-authentication-to-domain]]
