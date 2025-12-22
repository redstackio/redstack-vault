---
id: ea801e48-173e-4e2a-b3f7-13fbef40eb46
name: Update /etc/hosts with IP and Hostname
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T20:40:41.066848+00:00'
updated_at: '2023-05-26T00:39:38.069025+00:00'
tactics:
  - '[[tactics/Stage Capabilities|TA0026 - Stage Capabilities]]'
techniques:
  - >-
    [[techniques/Upload, install, and configure software/tools|T1362 - Upload,
    install, and configure software/tools]]
sub_techniques: []
tags:
  - '[[tags/Network]]'
commands: []
platforms:
  - Linux
tools: []
validated: true
---

# Update /etc/hosts with IP and Hostname

## Summary

This procedure updates the /etc/hosts file on a Linux system to map a specific IP address to one or more hostnames or subdomains. This is useful in scenarios like testing virtual host (vhost) configurations on web servers, where external DNS resolution should be avoided to prevent requests from leaking to public resolvers. By locally resolving the hostnames, the attacker can direct traffic to controlled IPs without relying on or alerting external DNS infrastructure.

## Description

The /etc/hosts file is a local DNS resolver on Linux systems that overrides DNS lookups for specified IPs and hostnames. In offensive security operations, modifying this file allows attackers to simulate domain resolutions for reconnaissance, exploitation, or staging attacks. For example, when targeting web applications that use vhost routing (e.g., Apache or Nginx with ServerName directives), adding custom entries ensures that requests to subdomains like "testsite1.domain.com" resolve to the attacker's controlled IP (e.g., 10.10.10.10) instead of querying external DNS servers. This technique supports stealthy testing and avoids detection through anomalous DNS queries. The procedure requires root privileges to edit the file and can be verified by pinging the added hostnames to confirm local resolution.

## Requirements

1. Root or sudo access on the Linux system to modify /etc/hosts.
2. Knowledge of the target IP address and desired hostnames/subdomains.
3. A text editor like nano, vim, or echo command for appending entries.
4. Linux platform (e.g., Kali, Ubuntu).

## Defense

Defensive measures and detection strategies:

- Monitor file integrity of /etc/hosts using tools like Tripwire or OSSEC to detect unauthorized modifications.
- Implement host-based intrusion detection (HIDS) to alert on sudo usage for file edits in system directories.
- Review DNS resolution logs or use network monitoring to identify unexpected local resolutions during incident response.
- Enforce least-privilege access to prevent non-admin users from editing system files.

## Objectives

1. Locally map IP addresses to custom hostnames to bypass external DNS.
2. Enable vhost-based testing or exploitation without DNS leakage.
3. Verify the configuration to ensure hostnames resolve correctly.

## Instructions

### Step 1: Open the /etc/hosts File for Editing

**Context**: Access the hosts file with elevated privileges to prepare for modifications. This step ensures you can safely add entries without permission errors.

Use sudo to open the file in a text editor:

```bash
sudo nano /etc/hosts
```

> This command launches the nano editor with root privileges. If nano is unavailable, substitute with vim or another editor. Locate the end of the file (after existing localhost entries) to avoid disrupting default resolutions.

### Step 2: Add the IP and Hostname Mapping

**Context**: Append a new line using the standard format: IP followed by one or more space-separated hostnames. This creates the local DNS override for the specified domains.

Add a line in the following format at the end of the file:

```bash
<IP> <SUBDOMAIN.DOMAINNAME1> <SUBDOMAIN.DOMAINNAME2>
```

For example, to map 10.10.10.10 to two subdomains:

```bash
10.10.10.10     testsite1.domain.com   testsite2.domain.com
```

> Replace <IP> with the actual IP (e.g., your attack machine's IP) and the hostnames with the target subdomains. Multiple hostnames can be added on the same line for the same IP. Save the file (Ctrl+O in nano, then Ctrl+X to exit).

### Step 3: Verify the Update

**Context**: Test the resolution to confirm the hosts file changes are active and hostnames resolve to the intended IP without external DNS queries.

Ping one of the added hostnames:

```bash
ping -c 3 testsite1.domain.com
```

> Expected output should show the IP 10.10.10.10 responding (assuming the IP is reachable). If it resolves to a different IP, check for syntax errors in /etc/hosts or flush DNS cache with `sudo systemd-resolve --flush-caches` on systemd-based systems. No external DNS traffic should occur during this test.
