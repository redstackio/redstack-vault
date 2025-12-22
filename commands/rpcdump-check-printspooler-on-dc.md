---
id: b834da02-9204-4c23-ab3e-3413f403bfbc
name: rpcdump-check-printspooler-on-dc
type: command
executor: bash
data: rpcdump.py $_TARGET_DC_IP | grep -A 6 "spoolsv"
output: null
created_at: '2023-04-06T03:56:02.745283+00:00'
updated_at: '2023-04-10T20:36:02.527266+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - active-directory
verified: true
validated: true
---

# rpcdump-check-printspooler-on-dc

## Command

```bash
rpcdump.py $_TARGET_DC_IP | grep -A 6 "spoolsv"
```

## Description

This command uses Impacket's rpcdump.py to enumerate RPC endpoints on a target Domain Controller and filters output to check for the Print Spooler service (spoolsv.exe), confirming if it's a viable target for PrinterBug exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DC_IP | IP address of the target Domain Controller | Yes |
| grep -A 6 | Show 6 lines after match for context on service UUIDs | Built-in |
| "spoolsv" | Filter string for Print Spooler service name | Built-in |

## Examples

### Basic Usage

```bash
rpcdump.py 10.10.10.10 | grep -A 6 "spoolsv"
```

### Advanced Usage

```bash
rpcdump.py -hashes :$_NTLM_HASH $_DOMAIN/$_USERNAME@$_TARGET_DC_IP | grep -A 6 "spoolsv"
```

(Use with pass-the-hash if needed for authenticated dump.)

## Expected Output

```
spoolsv: 12345678-1234-abcd-ef00-0123456789ab:2.0
  Interface: IPrintSpooler (6bffd098-a112-3610-9833-012892020162)
  Binding: ncacn_ip_tcp:10.10.10.10[135]
  UUID: 6bffd098-a112-3610-9833-012892020162 v2.0
  Endpoint: ncacn_ip_tcp:10.10.10.10[49669]
```

Success is indicated by the presence of the spoolsv interface UUID, confirming the service is running and accessible.

## Related

- [[Related Procedure: Exploit-ZeroLogon-and-PrinterBug-for-DC-System-Access]]
