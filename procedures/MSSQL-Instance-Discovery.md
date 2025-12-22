---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.831936+00:00'
updated_at: '2023-04-10T20:36:47.877280+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Discover Remote SQL Server Instances]]'
  - '[[tags/Identify Instances and Databases]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/get-sqlinstance-broadcast]]'
  - '[[commands/get-sqlinstance-scan-udp-threaded]]'
platforms:
  - Windows
tools: []
validated: true
---

# MSSQL-Instance-Discovery

## Summary

MSSQL Instance Discovery is a reconnaissance procedure that identifies remote Microsoft SQL Server instances on a network by sending UDP broadcast requests to the SQL Server Browser service (port 1434). This allows attackers to map out SQL Server deployments, including instance names, versions, and TCP ports, which can serve as entry points for further exploitation such as SQL injection or unauthorized access.

## Description

This procedure leverages PowerShell scripts to query the SQL Server Browser service, which responds with details about running SQL instances. It is particularly useful in internal network environments where SQL Servers are deployed without direct visibility. The broadcast method discovers instances across the local subnet, while the targeted scan focuses on a specific host. Success provides instance details like named instances (e.g., MSSQLSERVER$INSTANCENAME) and dynamic ports, enabling subsequent attacks. This technique assumes the SQL Browser service is enabled, which is common but configurable. It maps to MITRE ATT&CK's Network Service Scanning as it probes for specific service availability over the network.

## Requirements

1. PowerShell execution environment on a Windows host with network access to the target subnet.
2. The PowerSploit or equivalent SQL Server reconnaissance module loaded (e.g., via Import-Module).
3. UDP access to port 1434 (SQL Browser service) on the network.
4. Administrative privileges may be needed for module loading, but execution requires only network connectivity.

## Defense

Defensive measures and detection strategies:

- Limit network access to SQL Server instances to only trusted IP addresses using firewalls or network ACLs.
- Disable the SQL Server Browser service if not required, forcing static port configurations.
- Implement network segmentation to isolate SQL Servers and prevent lateral movement.
- Monitor UDP traffic on port 1434 for anomalous broadcasts using tools like Wireshark or IDS signatures for SQL Browser requests.
- Enable SQL Server auditing for connection attempts and review logs for unauthorized discoveries.

## Objectives

1. Identify all SQL Server instances running on the local network via broadcast.
2. Gather instance details including names, versions, and listening ports for targeted follow-up.
3. Verify presence of SQL services on specific hosts to prioritize attack paths.
4. Collect information to support subsequent techniques like credential dumping or injection attacks.

## Instructions

### Step 1: Perform Network Broadcast for SQL Instance Discovery

**Context**: This step sends a UDP broadcast to discover all SQL Server instances across the local subnet. It queries the SQL Browser service to receive responses with instance details, helping map the attack surface without knowing specific hostnames.

**Command** ([[commands/get-sqlinstance-broadcast]]):
```powershell
Get-SQLInstanceBroadcast -Verbose
```

> The -Verbose flag provides detailed progress and response information. This command broadcasts to port 1434 and parses responses for instance names and ports. Run it from a host on the same subnet as the targets.

### Step 2: Conduct Targeted UDP Scan on Specific Host

**Context**: After initial discovery or when focusing on a known host, this step performs a threaded UDP scan against a specific computer to confirm SQL instances. It is more efficient for verifying a single target and retrieves detailed instance information.

**Command** ([[commands/get-sqlinstance-scan-udp-threaded]]):
```powershell
Get-SQLInstanceScanUDPThreaded -Verbose -ComputerName $_TARGET_HOSTNAME
```

> Replace $_TARGET_HOSTNAME with the actual hostname or IP (e.g., SQLServer1). The -Verbose flag logs scan progress. This uses multi-threading for faster execution on the specified target over UDP port 1434.

### Step 3: Analyze and Verify Results

**Context**: Review the output from both commands to confirm discoveries. Cross-reference instance names and ports to build a list of potential targets. If no responses, check firewall rules or service status.

**Instructions**: Pipe outputs to a file for analysis, e.g., `Get-SQLInstanceBroadcast -Verbose | Out-File sql_instances.txt`. Look for entries like instance names (e.g., MSSQL$INST1) and TCP ports (e.g., 1433 or dynamic).
