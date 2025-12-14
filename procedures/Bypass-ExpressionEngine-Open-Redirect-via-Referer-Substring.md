---
tags:
  - open-redirect
  - bypass
  - expressionengine
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-set-referer-for-redirect-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.299Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d1c56df0-2c22-436b-8ac9-7b875ac77286
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-ExpressionEngine-Open-Redirect-via-Referer-Substring

## Summary

This procedure exploits a flaw in ExpressionEngine's open redirect protection by crafting a Referer header that includes the legitimate hostname as a substring within a malicious URL, causing PHP's stristr function to incorrectly validate the request origin and allow direct redirects to external sites without user confirmation.

## Description

ExpressionEngine's redirect library in system/ee/legacy/libraries/Redirect.php uses stristr($_SERVER['HTTP_REFERER'], $host) for case-insensitive substring matching on the Referer header. This returns true if the hostname appears anywhere in the Referer string, enabling bypass with headers like 'http://evil.com?http://www.target.com'. The attack targets the index.php?URL= endpoint, facilitating phishing by redirecting users to malicious domains. Prerequisites include public access to an vulnerable ExpressionEngine instance; outcomes include successful bypass confirmed by direct 302 redirects.

## Requirements

1. Access to a vulnerable ExpressionEngine installation (e.g., via public URL)
2. Ability to control HTTP Referer headers (browser dev tools, curl, or proxy like Burp)
3. Target redirect URL (external malicious site)

## Defense

Defensive measures and detection strategies:

- Replace stristr with stricter parsing (e.g., parse_url to extract and match domain exactly)
- Implement additional checks like Origin header validation or CSP for redirects
- Monitor logs for suspicious Referer patterns containing query parameters with hostnames
- Use WAF rules to block Referers with embedded host substrings

## Objectives

1. Bypass the Referer-based open redirect protection
2. Redirect users to arbitrary external URLs without prompts
3. Enable phishing or drive-by attacks on the target site

## Instructions

### Step 1: Identify the Target Endpoint

**Context**: Locate the vulnerable redirect endpoint in the ExpressionEngine instance.

**Instructions**: Confirm the target URL format: http://target.com/PATH_TO_EE/index.php?URL=https://external-site.com. No command needed; use browser to verify the site loads.

### Step 2: Craft the Malicious Referer Header

**Context**: Create a Referer that embeds the target hostname as a substring to fool stristr.

**Instructions**: Use a value like 'http://evil.com?http://target.com'. This can be set in browser dev tools or via curl.

### Step 3: Execute the Bypass Request

**Context**: Send the request with the crafted Referer to trigger the redirect.

**Command** ([[commands/curl-set-referer-for-redirect-bypass]]):
```bash
curl -v -e "http://evil.com?http://target.com" "http://target.com/PATH_TO_EE/index.php?URL=https://www.example.com"
```

> This command uses -e to set the Referer, -v for verbose output to observe the 302 redirect. Expected output includes Location: https://www.example.com without confirmation.

### Step 4: Verify the Bypass

**Context**: Confirm no prompt and direct redirect occurs.

**Instructions**: Check the response for immediate 302 status and Location header pointing to the external URL. In a browser, the page should redirect without interstitial.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-set-referer-for-redirect-bypass]]

## Tools Used


## Tags

- open-redirect
- bypass
- expressionengine
