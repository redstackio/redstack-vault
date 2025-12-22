---
id: ac-clickjacking-wordcamp
tags:
  - clickjacking
  - x-frame-options
  - web-vulnerability
  - wordpress
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inspect-HTTP-Headers-for-X-Frame-Options]]'
  - '[[procedures/Construct-Clickjacking-POC-HTML]]'
  - '[[procedures/Validate-Iframe-Embedding-in-Browser]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.722Z'
description: >-
  A multi-stage attack demonstrating clickjacking on WordCamp.org by exploiting
  the absence of the X-Frame-Options HTTP response header, allowing iframe
  embedding and user interaction hijacking.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Clickjacking Attack on WordCamp.org via Missing X-Frame-Options Header

Multi-stage attack chain demonstrating a complete clickjacking workflow on the WordCamp.org website, exploiting the lack of X-Frame-Options header to enable iframe embedding from malicious domains.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Header Inspection] --> B[POC Construction]
    B --> C[Embedding Validation]
    C --> D[Clickjacking Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools
- Text editor for HTML

### Target Environment

- Web platform
- WordPress-based site (e.g., https://central.wordcamp.org/)
- No specific ports or services required beyond HTTP/HTTPS access

### Initial Access Requirements

- Public internet access to the target URL
- No credentials needed
- Ability to host or locally serve HTML files

## Detailed Attack Procedures

### Step 1: Header Inspection
procedure: [[procedures/Inspect-HTTP-Headers-for-X-Frame-Options]]

**Objective**: Confirm the absence of the X-Frame-Options header on the target site to identify clickjacking vulnerability.

**Instructions**: Use [[commands/curl-check-headers]] to fetch and inspect the HTTP response headers from the target URL:

```bash
curl -I https://central.wordcamp.org/
```

Review the output for the presence of X-Frame-Options. If absent, the site is vulnerable to framing.

**Expected Output**: HTTP headers listing without X-Frame-Options, such as "HTTP/2 200" followed by various headers but no X-Frame-Options.

**Success Indicators**:
- No X-Frame-Options header found in response
- Site returns 200 OK status

### Step 2: POC Construction
procedure: [[procedures/Construct-Clickjacking-POC-HTML]]

**Objective**: Build a malicious HTML page that embeds the target site in an iframe to demonstrate framing capability.

**Instructions**: Create a new HTML file using a text editor with the following content:

```html
<html lang='en-US'>
<head>
<meta charset='UTF-8'>
<title>Clickjacking POC</title>
</head>
<body>
<h3>This site is vulnerable to clickjacking</h3>
<iframe src='https://central.wordcamp.org/' frameborder='2px' height='500px' width='500px'></iframe>
</body>
</html>
```

Save the file as clickjacking-poc.html. This embeds the target without restrictions due to the missing header.

**Expected Output**: A valid HTML file ready for loading in a browser.

**Success Indicators**:
- HTML file saved without errors
- Iframe src points to the vulnerable URL

### Step 3: Embedding Validation
procedure: [[procedures/Validate-Iframe-Embedding-in-Browser]]

**Objective**: Load the POC page to verify that the target site renders inside the iframe, confirming the clickjacking vector.

**Instructions**: Open the clickjacking-poc.html file in a web browser. Observe the iframe loading the WordCamp.org content fully without any framing restrictions or errors.

No specific command needed; use file:// protocol or serve locally if required.

**Expected Output**: The target site visible and interactive within the 500x500 iframe on the local page.

**Success Indicators**:
- Iframe loads without blocking (no X-Frame-Options enforcement)
- User can interact with elements inside the iframe

## Attack Chain Summary

### Key Achievements

1. Confirmed missing X-Frame-Options header enabling iframe embedding
2. Constructed a POC demonstrating clickjacking setup
3. Validated the exploit by rendering the target in a controlled iframe

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
