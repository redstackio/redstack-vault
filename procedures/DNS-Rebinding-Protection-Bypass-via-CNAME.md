---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Dynamic Resolution|T1568 - Dynamic Resolution]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques:
  - >-
    [[sub-techniques/Domain Generation Algorithms|T1568.002 - Domain Generation
    Algorithms]]
tags:
  - '[[tags/CNAME]]'
  - '[[tags/DNS Rebinding]]'
  - '[[tags/Protection Bypasses]]'
commands:
  - '[[commands/dig-query-cname-record]]'
platforms:
  - Linux
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# DNS-Rebinding-Protection-Bypass-via-CNAME

## Summary

This procedure demonstrates how to bypass DNS rebinding protections by leveraging CNAME records to resolve a domain to an internal IP address not covered by same-origin policy restrictions. It enables attackers to access vulnerable internal web applications from an external malicious site, potentially leading to unauthorized data access or remote code execution.

## Description

DNS rebinding attacks exploit the ability of DNS to resolve the same domain to different IP addresses over time or via different record types, bypassing browser same-origin policy (SOP) that typically blocks cross-origin requests. By using a CNAME record, an attacker can make an external domain resolve to an internal target IP (e.g., 127.0.0.1 or a private LAN address), tricking the browser into treating the request as same-origin. This is particularly effective against applications with weak DNS rebinding mitigations that only check A/AAAA records but not CNAME chains.

In a typical scenario, the attacker controls a domain (e.g., attacker.com) and sets up a CNAME for a subdomain (e.g., rebinding.attacker.com) pointing to the target's internal hostname (e.g., internal-app.local). A malicious webpage hosted on attacker.com includes JavaScript that makes fetch/XMLHttpRequest calls to rebinding.attacker.com, which resolves to the internal IP. If the target application is vulnerable (e.g., an admin panel), this allows unauthorized access to sensitive resources like APIs or files. This technique is commonly used in phishing campaigns where victims are lured to the attacker's site.

The procedure focuses on verifying the CNAME setup and testing the rebinding, assuming the attacker has DNS control over their domain. Success grants lateral movement to internal services, potentially exfiltrating data or escalating privileges.

## Requirements

1. Control over a domain and DNS server to configure CNAME records (e.g., via a registrar like Cloudflare or a custom DNS server).
2. A vulnerable internal web application protected by DNS rebinding but not fully mitigating CNAME chains (e.g., resolving to 192.168.x.x or localhost).
3. Access to a server to host the malicious webpage (e.g., Apache/Nginx on Linux).
4. Tools like dig (from BIND utilities) installed on a Linux system for DNS queries.
5. Victim browser without strict DNS rebinding protections (e.g., older Chrome/Firefox versions or misconfigured enterprise setups).

## Defense

Defensive measures and detection strategies:

- Implement strict DNS rebinding protections in web applications by validating all IP resolutions (including CNAME chains) against a whitelist of allowed IPs; use libraries like dns-rebinding-protection in Node.js or browser extensions.
- Enforce network segmentation to isolate internal services, preventing external resolution to private IPs (e.g., via firewall rules blocking non-RFC 1918 traffic).
- Monitor DNS queries for suspicious CNAME patterns or rapid IP changes using tools like Suricata or DNS logging in BIND.
- Educate users on phishing via email simulations and deploy browser policies (e.g., Chrome's --disable-web-security disabled in production).
- Use Content Security Policy (CSP) with strict origins and monitor for anomalous cross-origin requests in web logs.

## Objectives

1. Configure and verify a CNAME record that enables DNS rebinding to an internal target.
2. Test the rebinding setup to confirm bypass of SOP and access to protected resources.
3. Gain unauthorized access to sensitive internal information via the rebinding exploit.

## Instructions

### Step 1: Configure Malicious DNS Records

**Context**: Set up your controlled domain with a CNAME record pointing to the target's internal hostname. This tricks the resolver into mapping your external domain to an internal IP. Use your DNS provider's panel or tools like nsupdate.

Why: This establishes the rebinding mechanism, allowing the same domain to resolve differently based on query type or timing.

**Instructions**: Log in to your DNS provider (e.g., Cloudflare) and add a CNAME record for a subdomain like 'rebind.attacker.com' pointing to 'target.internal.local'. Set TTL low (e.g., 60s) for dynamic changes if needed. Verify propagation with a basic dig query.

**Expected Output**: DNS panel confirms the record; initial dig shows the CNAME alias.

### Step 2: Host Malicious Webpage

**Context**: Create a simple HTML page with JavaScript to trigger requests to the rebinding subdomain, exploiting the CNAME to access internal resources.

Why: The webpage lures the victim and executes the cross-origin bypass automatically upon load.

**Instructions**: On your server, create index.html with <script>fetch('http://rebind.attacker.com/admin/api');</script>. Serve via HTTP on port 80. For phishing, embed in an email template.

**Expected Output**: Page loads without errors; browser dev tools show requests to the internal IP.

### Step 3: Verify CNAME Rebinding Vulnerability

**Context**: Use DNS tools to confirm the CNAME resolves to the expected internal target, indicating the protection bypass is feasible.

Why: This validates the DNS setup before deploying the attack, ensuring the rebinding chain works without alerting defenders.

**Command** ([[commands/dig-query-cname-record]]):
```bash
$ dig cname.example.com +noall +answer
```

> Replace 'cname.example.com' with your subdomain (e.g., rebind.attacker.com). The +noall +answer flags limit output to the answer section for clean results. This queries the authoritative DNS for the CNAME record.

**Expected Output**:
```
cname.example.com.            381     IN      CNAME   target.local.
```
A successful response shows the CNAME pointing to the internal target (e.g., target.local resolves to 192.168.1.100). If no record or NXDOMAIN, the setup failed. If it resolves to public IPs only, rebinding protections may block private IPs—retry with a different chain.
