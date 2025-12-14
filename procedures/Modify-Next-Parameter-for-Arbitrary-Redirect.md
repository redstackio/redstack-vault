---
id: uuid-proc-2-683298
tags:
  - open-redirect
  - arbitrary-url
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:35.092Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Modify-Next-Parameter-for-Arbitrary-Redirect

## Summary

This procedure modifies the 'next' parameter in the MoPub login URL to an arbitrary external domain, exploiting the open redirect to demonstrate potential for phishing or social engineering attacks.

## Description

The MoPub login page fails to validate the 'next' parameter, allowing attackers to specify any URL, including malicious ones. By replacing the value with a controlled domain (e.g., https://evil.com), post-login redirection can lead users to phishing sites. URL encoding can obfuscate the payload to bypass basic filters. This step builds on URL construction and requires browser interaction to test the redirect flow.

## Requirements

1. Valid MoPub login credentials.
2. Web browser or proxy for URL editing.
3. Attacker-controlled domain for testing (e.g., a simple HTML page on evil.com).

## Defense

Defensive measures and detection strategies:

- Enforce domain allowlists for redirect parameters.
- Use Content Security Policy (CSP) to restrict navigations.
- Scan logs for anomalous redirects to external domains.

## Objectives

1. Redirect user to attacker site post-login.
2. Enable phishing by mimicking legitimate pages.
3. Obfuscate with encoding to evade detection.

## Instructions

### Step 1: Edit the Parameter

**Context**: Change 'next' to a malicious URL to test redirection.

Construct:

```url
https://app.mopub.com/login?next=https://evil.com
```

For obfuscation:

```url
https://app.mopub.com/login?next=%68%74%74%70%73%3A%2F%2F%65%76%69%6C%2E%63%6F%6D
```

> Load in browser; parameter should persist.

### Step 2: Verify Redirect Potential

**Context**: Ensure no immediate blocking before login.

Submit the page without logging in or use dev tools to inspect.

> Expected: Page loads; no sanitization errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Phishing: Spearphishing Link

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[open-redirect]]
- [[Phishing]]
