---
tags:
  - open-redirect
  - phishing
  - slack
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Slack-Open-Redirect]]'
step_count: 1
techniques:
  - '[[T1566.002]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.391Z'
description: >-
  An attack chain exploiting an open redirect vulnerability in Slack's /link
  endpoint to facilitate phishing by redirecting users to malicious external
  sites without validation or warnings.
skill_level: beginner
impact_level: medium
id: 4a159265-8ef6-4fef-977b-1b1c28cf0e22
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
  - '[[Exploit Public-Facing Application]]'
---
# Slack Open Redirect for Phishing Attacks

Multi-stage attack chain demonstrating a complete attack workflow exploiting Slack's open redirect to enable phishing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Construct Malicious Link] --> B[Distribute and Redirect to Phishing Site]
    B --> C[Steal Credentials or Cookies]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[curl]] for testing

### Target Environment

- Web platform
- Access to Slack's public website (https://slack.com)
- No specific services or ports required beyond standard HTTP/HTTPS

### Initial Access Requirements

- No credentials needed
- Public network access to slack.com
- Ability to craft and share URLs

## Detailed Attack Procedures

### Step 1: Construct and Test Malicious Redirect
procedure: [[procedures/Exploit-Slack-Open-Redirect]]

**Objective**: Create a URL that redirects from Slack to an attacker-controlled phishing site, tricking users into believing the link originates from Slack.

**Instructions**: Manually construct the vulnerable URL by appending the /link endpoint with an arbitrary external URL as the 'url' parameter. For testing, use [[commands/curl-test-slack-redirect]] to verify the redirect behavior:

```bash
curl -L "https://slack.com/link?url=http://example-phishing.com" -v
```

This command follows the redirect (-L) and shows verbose output (-v) to confirm the immediate jump to the external site without validation.

To distribute, embed the crafted URL (e.g., https://slack.com/link?url=http://attacker-phishing-site.com/login) in emails, messages, or social engineering lures impersonating Slack notifications.

**Expected Output**: The browser or curl output shows a direct HTTP 302 redirect to the specified external URL, with no user warning or referrer stripping confirmation visible to the attacker.

**Success Indicators**:
- Redirect occurs immediately to the external site
- No validation errors or blocks from Slack
- Victim's browser lands on the phishing page, potentially exposing cookies or prompting credential entry

## Attack Chain Summary

### Key Achievements

1. Successful open redirect exploitation without authentication
2. Enabled phishing vector by masquerading malicious links as legitimate Slack URLs
3. Potential for credential theft or session hijacking via redirected site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.002]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
