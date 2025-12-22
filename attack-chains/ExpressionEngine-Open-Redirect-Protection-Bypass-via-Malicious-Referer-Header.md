---
tags:
  - open-redirect
  - bypass
  - expressionengine
  - phishing
  - web
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
  - '[[procedures/Bypass-ExpressionEngine-Open-Redirect-via-Referer-Substring]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.303Z'
description: >-
  Bypass the open redirect protection in ExpressionEngine by crafting a Referer
  header that tricks the stristr function into matching a substring of the
  legitimate hostname, enabling direct redirects to arbitrary external sites for
  phishing or malware distribution.
skill_level: intermediate
impact_level: medium
id: 32e924fc-2fc2-450e-b990-bf990ffce2b2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# ExpressionEngine Open Redirect Protection Bypass via Malicious Referer Header

Multi-stage attack chain demonstrating the bypass of open redirect protection in ExpressionEngine, allowing attackers to redirect users to malicious external sites without confirmation prompts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare PoC Interface] --> B[Configure Target and Redirect] 
    B --> C[Generate Malicious Link with Referer]
    C --> D[Execute Redirect and Bypass]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser for PoC interaction
- [[commands/curl-set-referer-for-redirect-bypass]] for manual testing

### Target Environment

- ExpressionEngine CMS (versions vulnerable to Referer stristr check)
- Web platform with PHP
- Access to the site's index.php?URL= endpoint

### Initial Access Requirements

- Public access to the ExpressionEngine instance
- No authentication required for the redirect endpoint
- Ability to control the Referer header (via PoC or tools like curl/Burp)

## Detailed Attack Procedures

### Step 1: Visit the Prepared PoC HTML Page
procedure: [[procedures/Bypass-ExpressionEngine-Open-Redirect-via-Referer-Substring]]

**Objective**: Load the demonstration interface to facilitate the bypass setup.

**Instructions**: Open a web browser and navigate to the PoC page at http://strukt.tk/pocs/eeredirect.html. This page provides a user interface for inputting the target details and generating the exploit link.

**Expected Output**: The PoC interface loads, displaying fields for the target hostname and redirect URL.

**Success Indicators**:
- PoC page accessible without errors
- Input fields visible for configuration

### Step 2: Enter the Target ExpressionEngine Hostname and Desired External Redirect URL
procedure: [[procedures/Bypass-ExpressionEngine-Open-Redirect-via-Referer-Substring]]

**Objective**: Specify the vulnerable ExpressionEngine instance and the malicious target for redirection.

**Instructions**: In the PoC interface, input the target URL in the format http://HOST/PATH_TO_EE/index.php?URL=https://www.example.com, where HOST is the ExpressionEngine hostname (e.g., target.com) and the URL parameter is the external malicious site (e.g., https://evil.com/phish).

**Expected Output**: Fields populated with the target details, ready for link generation.

**Success Indicators**:
- Target hostname and redirect URL correctly entered
- No validation errors in the PoC form

### Step 3: Click the 'Test !!' Button to Generate the Malicious Link
procedure: [[procedures/Bypass-ExpressionEngine-Open-Redirect-via-Referer-Substring]]

**Objective**: Craft a link with a malicious Referer header that includes the target hostname as a substring to bypass the check.

**Instructions**: Click the 'Test !!' button in the PoC. This sets the Referer header to a value like http://evil.com?http://target.com, exploiting the stristr substring match, and generates a clickable link to the redirect endpoint.

For manual execution without PoC, use [[commands/curl-set-referer-for-redirect-bypass]] to test the header:

```bash
curl -e "http://evil.com?http://target.com" -I "http://target.com/PATH_TO_EE/index.php?URL=https://www.example.com"
```

**Expected Output**: A generated hyperlink or curl response showing a 302 redirect to the external URL.

**Success Indicators**:
- Malicious link generated
- Referer header includes substring match (verifiable in browser dev tools or curl verbose output)

### Step 4: Click the Generated Link and Observe the Direct Redirect
procedure: [[procedures/Bypass-ExpressionEngine-Open-Redirect-via-Referer-Substring]]

**Objective**: Trigger the bypass and confirm the redirect occurs without the user confirmation prompt.

**Instructions**: Click the generated link in the PoC or execute the manual curl command. The request to http://target.com/PATH_TO_EE/index.php?URL=external-site will bypass the Referer check due to stristr matching the hostname substring, resulting in an immediate redirect.

Monitor the response with curl verbose mode:

```bash
curl -v -e "http://evil.com?http://target.com" "http://target.com/PATH_TO_EE/index.php?URL=https://www.example.com"
```

**Expected Output**: HTTP 302 redirect to the external URL without any interstitial confirmation page.

**Success Indicators**:
- Direct redirect to external site
- No confirmation prompt from ExpressionEngine
- Browser or curl logs show successful bypass

## Attack Chain Summary

### Key Achievements

1. Loaded PoC interface for easy exploitation
2. Configured malicious Referer to exploit stristr substring vulnerability
3. Generated and executed bypass link
4. Achieved direct redirect to arbitrary external site, enabling phishing attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
