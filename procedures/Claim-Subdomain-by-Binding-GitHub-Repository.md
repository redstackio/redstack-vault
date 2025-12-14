---
tags:
  - subdomain-takeover
  - github
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-push]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.267Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 31b5cc76-bbbe-4149-92de-f79cb5ed161a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-by-Binding-GitHub-Repository

## Summary

This procedure exploits an unclaimed GitHub DNS pointer by creating a repository, enabling Pages, and binding the custom domain, allowing hosting of malicious content under the trusted subdomain.

## Description

Once verified unclaimed, attackers create a GitHub repo and configure it as the target for the dangling DNS (e.g., dev.rbk.money). GitHub will serve content from this repo at the subdomain. This leads to phishing or reputation damage. Requires a GitHub account; outcomes include full control, with propagation in minutes.

## Requirements

1. Free GitHub account
2. Git installed for repo management
3. Target subdomain confirmed unclaimed

## Defense

Defensive measures and detection strategies:

- Claim all potential subdomains proactively on services like GitHub
- Use DNS security extensions (DNSSEC) to prevent unauthorized claims
- Monitor for unexpected content on subdomains via uptime checks or security scanners

## Objectives

1. Create and configure GitHub repository
2. Bind custom domain for takeover
3. Deploy and verify malicious content

## Instructions

### Step 1: Create Repository

**Context**: Set up a new repo to host Pages.

Log in to GitHub, create a public repo named e.g., "dev-rbk-money".

### Step 2: Enable GitHub Pages and Bind Domain

**Context**: Configure Pages with custom domain.

In repo settings > Pages, select source (main branch), then under Custom domain, enter "dev.rbk.money" and save. GitHub will verify DNS automatically since it matches.

### Step 3: Deploy Content

**Context**: Push HTML or files to demonstrate control.

**Command** ([[commands/git-clone-push]]):
```bash
git clone https://github.com/yourusername/dev-rbk-money.git
echo '<h1>Phishing Page</h1><form>...</form>' > index.html
cd dev-rbk-money
git add index.html
git commit -m "Deploy malicious content"
git push origin main
```

> After push, wait 5-10 minutes for propagation. Visit https://dev.rbk.money to see content.

### Step 4: Verify Takeover

**Context**: Confirm control.

**Command** ([[commands/curl-http-check]]):
```bash
curl https://dev.rbk.money
```

> Output should match deployed HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-push]]
- [[commands/curl-http-check]]

## Tools Used


## Tags

- [[exploitation]]
- [[github]]
