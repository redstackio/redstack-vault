---
type: command
executor: powershell
data: Get-SQLInstanceScanUDPThreaded -Verbose -ComputerName $_TARGET_HOSTNAME
output: null
created_at: '2023-04-06T03:56:19.826556+00:00'
updated_at: '2023-04-10T20:36:47.895751+00:00'
platforms:
  - Windows
tags:
  - discovery
  - mssql
  - network-scan
verified: true
validated: true
---

# get-sqlinstance-scan-udp-threaded

## Command

```powershell
Get-SQLInstanceScanUDPThreaded -Verbose -ComputerName $_TARGET_HOSTNAME
```

## Description

This PowerShell command performs a multi-threaded UDP scan against a specific target host to discover SQL Server instances via the Browser service. It is ideal for verifying SQL presence on known hosts identified during broader scans.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName | Specifies the target hostname or IP to scan (e.g., SQLServer1 or 192.168.1.100) | Yes |
| -Verbose | Provides detailed logging of the scan process and results | No |

## Examples

### Basic Targeted Scan

```powershell
Get-SQLInstanceScanUDPThreaded -ComputerName SQLServer1
```

### Verbose Targeted Scan

```powershell
Get-SQLInstanceScanUDPThreaded -Verbose -ComputerName 192.168.1.100
```

## Expected Output

Details of SQL instances on the target, such as:

ComputerName : SQLServer1
InstanceName : MSSQL$INST1
TcpPort : 49250
IsClustered : False
Version : 14.0.1000.169

Empty output indicates no SQL Browser response or service unavailable.

## Related

- [[procedures/MSSQL-Instance-Discovery]]
- [[commands/get-sqlinstance-broadcast]]
