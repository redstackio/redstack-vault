---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques:
  - '[[sub-techniques/Password Guessing|T1110.001 - Password Guessing]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Password spraying]]'
  - '[[tags/Spray passwords against the RDP service]]'
commands:
  - '[[commands/git-clone-rdpassspray-repository]]'
  - '[[commands/run-rdpassspray-script]]'
  - '[[commands/hydra-rdp-brute-force]]'
  - '[[commands/ncrack-rdp-brute-force]]'
platforms:
  - Windows
tools:
  - '[[tools/rdpas-sspray]]'
  - '[[tools/Hydra]]'
  - '[[tools/ncrack]]'
verified: true
validated: true
---

# RDP-Service-Password-Spraying

## Summary

RDP Service Password Spraying is a credential access technique that involves attempting a small set of common passwords against a large number of RDP-enabled accounts to identify valid credentials without triggering account lockouts. This procedure uses tools like RDPassSpray, Hydra, and Ncrack to perform the spraying, targeting Remote Desktop Protocol services on Windows systems in an Active Directory environment.

## Description

This procedure targets the RDP service (port 3389) on Windows hosts, commonly used for remote access. By spraying common passwords across multiple usernames, attackers can compromise accounts with weak passwords while minimizing detection from failed login thresholds. It is effective in environments with poor password policies and exposed RDP endpoints. Success allows lateral movement, privilege escalation, or data exfiltration. The approach leverages automated tools to handle the spraying logic, ensuring low and slow attempts to evade defenses like account lockouts.

## Requirements

1. Network access to target RDP hosts (e.g., via firewall rules allowing TCP/3389).
2. List of target usernames (e.g., from enumeration) and a wordlist of common passwords (e.g., rockyou.txt).
3. Installed tools: RDPassSpray, Hydra, or Ncrack on a Linux-based attacker machine (Kali recommended).
4. Domain information if targeting Active Directory-joined systems.

## Defense

- Implement strong password policies requiring complexity and regular rotation.
- Configure account lockout policies after a low number of failed attempts (e.g., 5).
- Enable multi-factor authentication (MFA) for RDP access.
- Use network segmentation and RDP gateways to limit exposure.
- Monitor for anomalous RDP login attempts via SIEM or EDR tools.

## Objectives

1. Identify valid RDP credentials using password spraying to gain initial access.
2. Compromise RDP service accounts for remote shell access.
3. Enable pivoting to other systems within the network.
4. Facilitate privilege escalation using obtained credentials.

## Instructions

### Step 1: Clone and Setup RDPassSpray Tool

**Context**: Obtain the RDPassSpray tool, which is designed for targeted RDP password spraying against a single IP with multiple username-password combinations to avoid lockouts.

**Command** ([[commands/git-clone-rdpassspray-repository]]):
```bash
git clone https://github.com/xFreed0m/RDPassSpray
```

> This clones the repository to your local directory. Navigate into the cloned folder afterward. Expected output includes download progress and confirmation of the repository structure.

### Step 2: Run RDPassSpray for Targeted Spraying

**Context**: Execute RDPassSpray to spray passwords against a specific target IP, using a single password or list across usernames. This step assumes you have a usernames file and password list prepared.

**Command** ([[commands/run-rdpassspray-script]]):
```bash
python3 RDPassSpray.py -u [USERNAME] -p [PASSWORD] -d [DOMAIN] -t [TARGET IP]
```

> Replace placeholders with actual values (e.g., -u users.txt for a file, -p passwords.txt). This performs the spraying attempts. Expected output shows connection attempts, successes, or failures per credential pair. If a valid credential is found, it will indicate successful authentication.

### Step 3: Alternative Spraying with Hydra

**Context**: If RDPassSpray is unavailable, use Hydra for brute-force spraying on RDP. Limit threads to 1 to mimic legitimate traffic and reduce detection risk.

**Command** ([[commands/hydra-rdp-brute-force]]):
```bash
hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.10
```

> This sprays the rockyou wordlist against the 'administrator' user on the target IP. The -f flag stops after the first success. Expected output includes verbose login attempts and highlights valid credentials if found.

### Step 4: Alternative Spraying with Ncrack

**Context**: Use Ncrack as another option for RDP spraying, with connection limits to control speed and avoid lockouts.

**Command** ([[commands/ncrack-rdp-brute-force]]):
```bash
ncrack --connection-limit 1 -vv --user administrator -P password-file.txt rdp://10.10.10.10
```

> This attempts passwords from the file against the specified user. Verbose output details each attempt. Expected output shows progress and confirms valid logins upon success.

### Step 5: Verify Access and Cleanup

**Context**: Upon finding valid credentials, test RDP connection using an RDP client (e.g., remmina or mstsc). Document successful pairs and clear any logs if operating in a controlled environment.

> No specific command here; use the credentials in an RDP client. Success is indicated by a successful remote desktop session. If no successes, review wordlists or enumerate more usernames.
