---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - subdomain-takeover
  - dns
  - wix
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-subdomain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:01.829Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Detect-and-Claim-Unclaimed-Wix-Subdomain

## Summary

This procedure detects an unclaimed subdomain delegated to Wix.com via DNS and claims it for takeover, enabling the attacker to host arbitrary content such as phishing sites under the legitimate domain name. It exploits misconfigurations where subdomains are pointed to third-party services without proper claiming.

## Description

In this attack scenario, the target has delegated an unused subdomain (e.g., accessday.opn.ooo) to Wix.com's nameservers but failed to claim it on Wix, leaving it vulnerable. The procedure starts with reconnaissance by accessing the subdomain to confirm Wix control and unclaimed status, then proceeds to claim it using a free Wix account. Once claimed, the subdomain can be abused for phishing, malware distribution, or reputation hijacking. Prerequisites include public access to the subdomain and a Wix account; no advanced technical skills are needed beyond basic web navigation. Expected outcomes include full attacker control, potentially leading to high-impact domain spoofing.

## Requirements

1. Internet access to resolve and HTTP request the target subdomain
2. Web browser for manual inspection or curl for automated checking
3. Free Wix.com account for claiming (signup requires email)
4. Basic understanding of DNS delegation (CNAME/NS records pointing to Wix)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for unused subdomains delegated to third parties and claim or remove them
- Use automated tools like Subdomain Takeover scanners (e.g., dnstakeover) to monitor for vulnerabilities
- Implement DNS monitoring alerts for changes in subdomain resolutions
- Enforce domain verification processes before delegation

## Objectives

1. Confirm unclaimed status to validate takeover feasibility
2. Gain control of the subdomain for content hosting
3. Enable malicious abuse while maintaining the legitimate domain appearance

## Instructions

### Step 1: Access and Inspect Subdomain

**Context**: Send an HTTP request to the subdomain to observe if it resolves to Wix infrastructure, indicating it's unclaimed.

**Command** ([[commands/curl-check-subdomain]]):
```bash
curl -I http://accessday.opn.ooo/
```

> This command performs a HEAD request and returns headers. Look for Wix-specific indicators like "Location: https://www.wix.com/..." or "Server: openresty". A 301/302 redirect to a Wix claiming page or default template confirms availability.

### Step 2: Verify DNS Delegation

**Context**: Confirm the subdomain's DNS points to Wix nameservers, a prerequisite for claiming.

**Command** (use dig or nslookup, inferred):
```bash
dig NS accessday.opn.ooo
```

> Expected output shows NS records like ns1.wixdns.net, confirming delegation. If not, the takeover path differs.

### Step 3: Claim on Wix

**Context**: Use a browser to sign up/log in to Wix and connect the custom domain.

**Instructions**: Visit https://www.wix.com/, create an account, go to Domains > Connect a domain you already own, enter 'accessday.opn.ooo', and follow prompts to verify via DNS (Wix provides TXT record to add, but since delegated, it auto-verifies). Once connected, use Wix editor to upload malicious content.

> No command needed; manual via web interface. Success: Dashboard shows domain as active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-subdomain]]
- dig (for DNS verification)

## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[wix]]

---
