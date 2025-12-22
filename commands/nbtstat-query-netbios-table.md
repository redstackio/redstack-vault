---
type: command
executor: cmd
data: nbtstat -a $_TARGET_IP_OR_HOSTNAME
tags:
  - enumeration
  - netbios
platforms:
  - Windows
verified: true
validated: true
---

# nbtstat-query-netbios-table

## Command

```cmd
nbtstat -a $_TARGET_IP_OR_HOSTNAME
```

## Description

This command queries and displays the NetBIOS name table of a remote Windows host, useful for network enumeration to identify workstations, servers, and domains before poisoning attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Performs remote name lookup and displays the NetBIOS name table | Yes |
| $_TARGET_IP_OR_HOSTNAME | IP address or hostname of the target system | Yes |

## Examples

### Basic Usage

```cmd
nbtstat -a 192.168.1.100
```

### Advanced Usage

```cmd
nbtstat -a TARGETHOST
```

## Expected Output

```
NetBIOS Remote Machine Name Table

    Name               Type         Status
--------------------------------------------- 
WORKSTATION     <00>  UNIQUE      Registered
DOMAIN          <00>  GROUP       Registered
WORKSTATION     <20>  UNIQUE      Registered
```
This shows registered NetBIOS names and their types/statuses, indicating active hosts and roles.

## Related

- [[procedures/Net-NTLMv2-Hash-Capture-and-Cracking]]
- [[tools/Nbtstat]]
