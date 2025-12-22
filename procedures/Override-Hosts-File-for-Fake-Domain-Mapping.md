---
tags:
  - hostname-manipulation
  - local-override
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/edit-hosts-file]]'
  - '[[commands/cat-hosts]]'
platforms:
  - Linux
  - macOS
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: df752645-d8ab-442a-85c2-6a826e821a1e
created_at: '2025-12-14T03:15:26.554Z'
updated_at: '2025-12-14T03:15:26.554Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Override-Hosts-File-for-Fake-Domain-Mapping

## Summary

This procedure overrides the local hosts file to map a target's IP address to a fake domain under attacker control, enabling manipulation of hostname resolution for web applications like Concrete CMS that lack canonical URL configurations.

## Description

In scenarios targeting web applications with full page caching, editing the hosts file tricks the local resolver into using a fake domain for requests to the target's IP. This causes the application's URL resolver to embed the fake hostname in generated links and BASE_URL, which get cached. Prerequisites include administrative access on the attacker's machine and knowledge of the target's IP. Expected outcome is local resolution of the fake domain to the target, setting up for cache poisoning.

## Requirements

1. Administrative privileges on the local machine to edit /etc/hosts (Linux/macOS) or C:\Windows\System32\drivers\etc\hosts (Windows)
2. Knowledge of the target's IP address
3. A fake domain (e.g., fake-site.com) that the attacker can later point to malicious content if needed

## Defense

Defensive measures and detection strategies:

- Configure canonical URLs in CMS to enforce consistent hostname usage
- Monitor for unusual cache invalidations or hostname variations in logs
- Use Content Security Policy (CSP) to restrict script sources and mitigate XSS

## Objectives

1. Redirect local requests from target IP to fake domain
2. Enable subsequent requests to embed fake hostname in application output
3. Prepare for cache poisoning without altering the target's DNS

## Instructions

### Step 1: Append Fake Domain Mapping

**Context**: Add an entry to the hosts file to override DNS resolution for the target's IP.

**Command** ([[commands/edit-hosts-file]]):
```bash
echo "11.22.33.44 fake-site.com" | sudo tee -a /etc/hosts
```

> This appends the line '11.22.33.44 fake-site.com' to /etc/hosts, where 11.22.33.44 is the target's IP. On Windows, use notepad as admin to edit the file manually. Expected output: No errors; file updated.

### Step 2: Verify the Mapping

**Context**: Confirm the entry is active and resolution works.

**Command** ([[commands/cat-hosts]]):
```bash
cat /etc/hosts | grep fake-site.com
```

> This greps for the fake domain to show the entry. Test resolution with `ping fake-site.com` to ensure it pings the target IP. Expected output: The mapping line displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/edit-hosts-file]]
- [[commands/cat-hosts]]

## Tools Used


## Tags

- [[hostname-manipulation]]
- [[dns-override]]
