---
id: proc-ensure-victim-privileges-187520
tags:
  - csrf
  - prerequisites
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/check-wordpress-session]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:31:30.714Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Ensure-Victim-Privileges-for-Press-This

## Summary

This procedure verifies that the target victim has an active authenticated session in WordPress 4.7 with access to the Press This feature, enabling subsequent CSRF exploitation to trigger SSRF.

## Description

In the attack scenario, the victim must be a logged-in WordPress user capable of using the Press This bookmarklet or endpoint (wp-admin/press-this.php). This prerequisite ensures the CSRF request is processed under the victim's session cookies, leading to server-side scraping that can be hijacked for SSRF. Without this, the attack fails as unauthenticated requests won't trigger the feature. Expected outcome: Confirmed session allowing forged requests.

## Requirements

1. Access to victim's browser or ability to lure them to malicious content (e.g., via phishing email)
2. Knowledge of the target WordPress instance URL
3. Victim's authentication status verifiable via prior interaction

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all admin endpoints
- Monitor for unusual Press This usage from authenticated sessions
- Educate users on phishing and bookmarklet risks

## Objectives

1. Confirm active session and Press This access
2. Set stage for CSRF delivery
3. Ensure attack chain viability

## Instructions

### Step 1: Verify Authentication Status

**Context**: Check if the victim is logged in by attempting to access a protected endpoint or through social engineering.

**Command** ([[commands/check-wordpress-session]]):
```bash
curl -c cookies.txt -b cookies.txt "https://target.com/wp-admin/" -I
```

> This command fetches the admin page headers; a 200 or redirect to dashboard indicates active session. Expected output: HTTP 200 or location to wp-admin/index.php.

### Step 2: Confirm Press This Access

**Context**: Test if Press This is usable by simulating a benign request.

**Command** ([[commands/test-press-this-access]]):
```bash
curl -b cookies.txt "https://target.com/wp-admin/press-this.php?u=https://example.com&url-scan-submit=Scan"
```

> Simulates a scrape; success if server fetches without errors. Expected output: Scraped content or redirect response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- [[commands/check-wordpress-session]]
- [[commands/test-press-this-access]]

## Tools Used

- None

## Tags

- [[csrf]]
- [[prerequisites]]
