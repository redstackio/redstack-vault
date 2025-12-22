---
id: a7401d51-8980-49c3-b132-3889bd1fd6eb
name: reuse-kerberos-ccache-tickets-from-tmp
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.533846+00:00'
updated_at: '2023-04-10T20:36:14.367262+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Steal or Forge Kerberos Tickets]]'
sub_techniques:
  - '[[cme-smb-enable-rdp]]'
  - '[[Silver Ticket]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/CCACHE ticket reuse from /tmp]]'
commands:
  - '[[commands/find-krb5ccname-environment-variable]]'
  - '[[commands/list-kerberos-ticket-cache-files-in-tmp]]'
  - '[[commands/set-krb5ccname-to-specific-cache-file]]'
  - '[[commands/set-krb5ccname-to-tmp-ticket-ccache]]'
platforms:
  - Linux
validated: true
---

# reuse-kerberos-ccache-tickets-from-tmp

## Summary

This procedure demonstrates how to locate and reuse Kerberos ticket cache (CCACHE) files from the /tmp directory on a compromised Linux system to facilitate lateral movement into an Active Directory environment. By extracting and setting the KRB5CCNAME environment variable to point to an existing ticket cache, an attacker can impersonate the ticket owner for authentication to AD services without re-authentication.

## Description

CCACHE ticket reuse from /tmp is a post-exploitation technique targeting Linux systems integrated with Active Directory via Kerberos authentication. When a user authenticates to AD from Linux, Kerberos tickets are cached in /tmp as files like krb5cc_<UID>. An attacker with shell access can identify these caches, copy or reference them, and set the KRB5CCNAME environment variable to reuse the tickets for accessing AD resources such as shares, services, or further lateral movement. This avoids the need for password cracking or new authentications. Technically, Kerberos tickets (TGTs and service tickets) are stored in these cache files; tools like kinit or Impacket can then use them directly. This is particularly effective in hybrid environments where Linux joins AD domains. Prerequisites include shell access on the Linux host and the target having prior AD authentication. Outcomes include unauthorized access to AD-protected resources, enabling escalation or exfiltration.

## Requirements

1. Shell access to a compromised Linux system joined to or authenticating against Active Directory.
2. The target user must have recently authenticated to AD, leaving valid tickets in /tmp.
3. Basic tools like bash (pre-installed on Linux) for environment manipulation; optional: klist for ticket inspection.
4. Knowledge of the domain and service principals for ticket usage.

## Defense

- Monitor /tmp for unauthorized access or copying of krb5cc* files using file integrity monitoring (e.g., auditd).
- Restrict permissions on /tmp to prevent non-privileged users from reading others' cache files; use AppArmor or SELinux policies.
- Implement Kerberos ticket lifetime restrictions and monitor for anomalous authentications from Linux hosts.
- Enable multi-factor authentication (MFA) for AD to limit ticket reuse impact.
- Regularly rotate credentials and use ticket delegation restrictions.

## Objectives

1. Identify and locate existing Kerberos ticket cache files in /tmp.
2. Set the KRB5CCNAME environment variable to reuse a specific ticket cache for authentication.
3. Authenticate to Active Directory services using the reused tickets for lateral movement.
4. Access sensitive AD resources without additional credentials.

## Instructions

### Step 1: Identify Current Kerberos Ticket Cache Location

**Context**: Begin by checking the current KRB5CCNAME environment variable to see if a ticket cache is already in use. This reveals the path to the active cache file, typically in /tmp, and confirms Kerberos configuration.

**Command** ([[commands/find-krb5ccname-environment-variable]]):
```bash
env | grep KRB5CCNAME
```

> This command lists environment variables and filters for KRB5CCNAME, which points to the current ticket cache (e.g., FILE:/tmp/krb5cc_1000). If set, it indicates an active session; if not, proceed to locate caches manually. Expected output shows the variable if present, helping identify the default cache location.

### Step 2: List Available Kerberos Ticket Cache Files in /tmp

**Context**: Scan /tmp for all krb5cc* files, which store cached tickets from prior authentications. This step uncovers potential tickets from other users or sessions for reuse.

**Command** ([[commands/list-kerberos-ticket-cache-files-in-tmp]]):
```bash
ls /tmp/ | grep krb5cc
```

> The ls command lists files in /tmp, piped to grep for krb5cc patterns. This reveals files like krb5cc_1000 or krb5cc_<timestamp>. Expected output is a list of cache files; select one based on UID or recency for the target user. If no files appear, no recent authentications occurred.

### Step 3: Set KRB5CCNAME to a Specific Cache File

**Context**: Once a suitable cache file is identified (e.g., from a privileged user), export the KRB5CCNAME variable to point to it. This configures subsequent Kerberos operations to use the reused tickets.

**Command** ([[commands/set-krb5ccname-to-specific-cache-file]]):
```bash
export KRB5CCNAME=/tmp/krb5cc_1569901115
```

> Replace the path with the actual file from Step 2. This sets the environment variable for the current session, allowing tools like kinit or smbclient to use the tickets. Expected output is none (silent success); verify with `echo $KRB5CCNAME` showing the new path. Test by running `klist` to list tickets from the cache.

### Step 4: Set KRB5CCNAME to a Custom Ticket Cache (Alternative)

**Context**: If copying a cache to a new file (e.g., for persistence or modification), set KRB5CCNAME to the custom location. This is useful after extracting or renaming a cache file.

**Command** ([[commands/set-krb5ccname-to-tmp-ticket-ccache]]):
```bash
export KRB5CCNAME=/tmp/ticket.ccache
```

> Use this after copying a krb5cc file to /tmp/ticket.ccache (e.g., `cp /tmp/krb5cc_1000 /tmp/ticket.ccache`). It overrides the default cache for reuse. Expected output is none; confirm with `klist` showing loaded tickets. This enables authentication to AD services like `smbclient //dc.example.com/share -k`.
