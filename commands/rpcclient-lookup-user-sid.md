---
id: new-uuid-lookup-sid
name: rpcclient-lookup-user-sid
type: command
executor: bash
data: rpcclient -U "" -N $_TARGET_IP -c "lookupnames $_USERNAME"
output: null
created_at: '2023-04-06T03:56:02Z'
updated_at: '2023-04-10T20:26:04Z'
platforms:
  - Linux
tags:
  - discovery
  - active-directory
verified: true
validated: true
---

# rpcclient-lookup-user-sid

## Command

```bash
rpcclient -U "" -N $_TARGET_IP -c "lookupnames $_USERNAME"
```

## Description

This command uses rpcclient to perform a null session lookup of a specific username on a Windows domain controller, retrieving the user's Security Identifier (SID). It is useful for targeted account discovery in Active Directory environments, particularly as a precursor to privilege escalation exploits like MS14-068.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target domain controller | Yes |
| $_USERNAME | Username to look up (e.g., administrator) | Yes |
| -U "" | Specifies empty username for null session | Yes |
| -N | No password (null authentication) | Yes |
| -c | Execute the specified command (lookupnames) | Yes |

## Examples

### Basic Usage

```bash
rpcclient -U "" -N 10.10.10.10 -c "lookupnames administrator"
```

### Advanced Usage

For scripting, wrap in a loop to lookup multiple users:

```bash
for user in admin guest; do rpcclient -U "" -N 10.10.10.10 -c "lookupnames $user"; done
```

## Expected Output

```
result was OK
names
username
  <administrator>
  <sid>
  S-1-5-21-1234567890-1234567890-1234567890-500
```

The output shows the username and its domain SID if successful. Errors like 'NT_STATUS_ACCESS_DENIED' indicate insufficient access.

## Related

- [[commands/rpcclient-enum-domain-users]]
- [[procedures/sid-enumeration-and-wmi-query-for-ms14-068-exploitation]]
