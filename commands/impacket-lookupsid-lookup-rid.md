---
id: fc0ae50f-6c12-4e92-a256-304b6af90dc1
type: command
executor: bash
data: 'python3 lookupsid.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP $_RID'
output: S-1-5-21-1111111111-2222222222-3333333333-500 DOMAIN\\Administrator
created_at: '2023-05-29T16:48:53.029709+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - rid
  - enumeration
verified: true
validated: true
---

# impacket-lookupsid-lookup-rid

## Command

```bash
python3 lookupsid.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP $_RID
```

## Description

This command uses impacket-lookupsid to perform an authenticated lookup of a specific Relative Identifier (RID) on a remote Windows target via LSARPC over SMB. It resolves the full SID to a username or group name, aiding in account enumeration. For comprehensive user discovery, repeat this command across a RID range (e.g., 500-2000) using a script or loop, as the tool itself handles single lookups efficiently.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain or workstation name (e.g., DOMAIN or WORKSTATION) | Yes |
| $_USERNAME | Valid username for authentication | Yes |
| $_PASSWORD | Corresponding password (or use -hashes for NTLM) | Yes |
| $_TARGET_IP | IP address of the target Windows host | Yes |
| $_RID | Specific Relative Identifier to resolve (e.g., 500 for Administrator) | Yes |
| -hashes | Optional: Use NTLM hashes instead of password for pass-the-hash | No |
| -k | Optional: Enable Kerberos authentication | No |

## Examples

### Basic Usage

Resolve RID 500 on a domain-joined Windows machine:

```bash
python3 lookupsid.py DOMAIN/user:pass@10.10.10.10 500
```

### Advanced Usage

Lookup using NTLM hashes and a custom RID range simulation (single call):

```bash
python3 lookupsid.py -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 DOMAIN/user@10.10.10.10 1001
```

For brute-force enumeration (wrap in a loop for multiple RIDs):

```bash
for rid in {500..550}; do python3 lookupsid.py DOMAIN/user:pass@10.10.10.10 $rid; done
```

## Expected Output

If the RID resolves to an account, the output displays the full SID followed by the account name. Unresolved RIDs show a "not found" message. Example for a successful user lookup:

```
S-1-5-21-1111111111-2222222222-3333333333-500 DOMAIN\\Administrator
```

For groups or aliases, it may show (SidTypeGroup) or similar type indicators. Failed authentications result in RPC errors like "STATUS_LOGON_FAILURE".

## Related

- [[procedures/brute-force-smb-users-using-rid-authenticated]]
- [[tools/impacket-lookupsid]]
