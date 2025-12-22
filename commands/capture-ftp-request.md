---
data: tcpdump -i any port 21 -vv
tags:
  - exfiltration
  - network
type: command
executor: bash
platforms:
  - Linux
id: 2ef2df03-9733-4847-a873-4b1330d58687
created_at: '2025-12-13T09:00:27.886Z'
updated_at: '2025-12-13T09:00:27.886Z'
verified: false
validated: true
submitted: true
---
# Capture FTP Request

## Command

```bash
tcpdump -i any port 21 -vv
```

## Description

Captures incoming FTP requests to monitor for exfiltrated data embedded in URLs during XXE attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i any` | Interface to capture on | Yes |
| `port 21` | Filter for FTP port | Yes |
| `-vv` | Verbose output | No |

## Examples

### Basic Usage

```bash
tcpdump -i any port 21 -vv
```

### Advanced Usage

```bash
tcpdump -i any port 21 -vv -w capture.pcap
```

## Expected Output

Packet capture showing FTP requests with embedded data.

## Related

- [[procedures/Receive-Exfiltrated-Data-via-Out-of-Band-Channel]]
