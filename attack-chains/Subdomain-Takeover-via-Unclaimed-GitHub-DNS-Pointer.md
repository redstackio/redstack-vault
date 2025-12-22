---
tags:
  - subdomain-takeover
  - dns
  - github
  - misconfiguration
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Vulnerable-Subdomain-via-DNS-Analysis]]'
  - '[[procedures/Verify-Unclaimed-GitHub-Custom-Domain]]'
  - '[[procedures/Claim-Subdomain-by-Binding-GitHub-Repository]]'
step_count: 3
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:31.284Z'
description: >-
  A multi-stage attack exploiting a dangling DNS record pointing to GitHub
  infrastructure, allowing takeover of the dev.rbk.money subdomain for malicious
  content hosting.
skill_level: intermediate
impact_level: high
id: 202c8a1c-0cc5-45e2-aee7-c221a513c8f2
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Subdomain Takeover via Unclaimed GitHub DNS Pointer

Multi-stage attack chain demonstrating a complete subdomain takeover workflow by exploiting unclaimed DNS pointers to GitHub infrastructure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Subdomain DNS] --> B[Verification: Check Claim Status]
    B --> C[Exploitation: Claim and Host Malicious Content]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/dig-dns-query]]
- Web browser for GitHub verification

### Target Environment

- Public DNS resolution
- Access to GitHub account (free tier sufficient)
- No special ports required; uses standard DNS (port 53) and HTTPS (port 443)

### Initial Access Requirements

- No credentials needed for reconnaissance
- GitHub account for exploitation
- Public internet access

## Detailed Attack Procedures

### Step 1: Discover Vulnerable Subdomain
procedure: [[procedures/Discover-Vulnerable-Subdomain-via-DNS-Analysis]]

**Objective**: Identify subdomains with dangling DNS records pointing to external services like GitHub.

**Instructions**: Start by enumerating subdomains of the target domain (e.g., rbk.money) using common brute-forcing or certificate transparency logs. Then, query DNS records for suspicious entries.

Use [[commands/dig-dns-query]] to analyze the CNAME record:

```bash
dig dev.rbk.money CNAME
```

**Expected Output**: Response showing a CNAME to GitHub's infrastructure, such as github.io or pages.github.com, without active resolution to a claimed site.

**Success Indicators**:
- CNAME points to unclaimed service (e.g., GitHub)
- Subdomain does not resolve to legitimate content

### Step 2: Verify Unclaimed Status
procedure: [[procedures/Verify-Unclaimed-GitHub-Custom-Domain]]

**Objective**: Confirm that the subdomain is not associated with any existing GitHub repository or account.

**Instructions**: Access GitHub and search for repositories or pages using the subdomain. Attempt to visit the subdomain URL to check for default or error pages indicating unclaimed status.

Browse to https://dev.rbk.money in a web browser and observe if it shows a GitHub 404 or unconfigured page.

Additionally, use [[commands/dig-dns-query]] to confirm ongoing DNS setup:

```bash
dig dev.rbk.money
```

**Expected Output**: No active GitHub Pages site; DNS resolves to GitHub but no content served.

**Success Indicators**:
- No repository found on GitHub with the custom domain
- Subdomain loads a generic GitHub error page

### Step 3: Exploit Takeover
procedure: [[procedures/Claim-Subdomain-by-Binding-GitHub-Repository]]

**Objective**: Claim control of the subdomain by associating it with a new GitHub repository and hosting malicious content.

**Instructions**: Create a new GitHub repository, enable GitHub Pages, and configure the custom domain. Push content to demonstrate control, such as a phishing page.

1. Log in to GitHub and create a new repository (e.g., "takeover-repo").
2. Go to repository settings > Pages > Custom domain, and enter "dev.rbk.money".
3. Commit and push an index.html file with test content:

```bash
git init
git remote add origin https://github.com/yourusername/takeover-repo.git
echo '<h1>Takeover Successful</h1>' > index.html
git add .
git commit -m "Initial commit"
git push -u origin main
```

Wait for DNS propagation (up to 10 minutes), then verify by visiting https://dev.rbk.money.

**Expected Output**: The subdomain now serves content from your repository.

**Success Indicators**:
- Custom domain binds successfully without errors
- Subdomain loads attacker-controlled content

## Attack Chain Summary

### Key Achievements

1. Identified dangling DNS pointer to GitHub
2. Confirmed unclaimed status for takeover feasibility
3. Demonstrated full control by hosting arbitrary content

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
