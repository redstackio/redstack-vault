---
id: ac-clickjacking-yelp-xframe
tags:
  - clickjacking
  - x-frame-options
  - ui-redressing
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Check-X-Frame-Options-Header-Absence]]'
  - '[[procedures/Create-Proof-of-Concept-HTML-for-Iframe-Embedding]]'
  - '[[procedures/Verify-Iframe-Loading-in-Browser]]'
  - '[[procedures/Capture-Screenshot-as-Proof]]'
  - '[[procedures/Test-Vulnerability-on-Subdomains]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.842Z'
description: >-
  Demonstrates discovery and verification of clickjacking vulnerability on Yelp
  due to absent X-Frame-Options header, enabling iframe embedding from external
  domains.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Clickjacking on Yelp via Missing X-Frame-Options Header

Multi-stage attack chain demonstrating the discovery and verification of a clickjacking vulnerability on Yelp's website and subdomains due to the absence of the X-Frame-Options HTTP response header. This allows malicious sites to embed Yelp in iframes, potentially tricking users into unintended actions like clicking hidden elements for unauthorized form submissions or data disclosure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Header Check] --> B[PoC Creation]
    B --> C[Browser Verification]
    C --> D[Screenshot Capture]
    D --> E[Subdomain Testing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Unspecified]]

### Target Environment

- Web platform
- Access to Yelp.com and subdomains (e.g., m.yelp.com, biz.yelp.com)
- Local file system for saving HTML PoC

### Initial Access Requirements

- Public internet access to Yelp
- Web browser for inspection and testing
- No credentials required

## Detailed Attack Procedures

### Step 1: Header Inspection
procedure: [[procedures/Check-X-Frame-Options-Header-Absence]]

**Objective**: Confirm the absence of X-Frame-Options header in Yelp's HTTP responses, indicating potential for framing.

**Instructions**: Open a web browser and navigate to yelp.com. Use developer tools to inspect the network response headers for the main page load.

**Expected Output**: HTTP response headers without X-Frame-Options, allowing framing by default.

**Success Indicators**:
- No X-Frame-Options header present in response
- Browser confirms site loads without frame restrictions

### Step 2: PoC HTML Creation
procedure: [[procedures/Create-Proof-of-Concept-HTML-for-Iframe-Embedding]]

**Objective**: Build a simple HTML file to test embedding Yelp in an iframe from a local or external domain.

**Instructions**: Create a new HTML file with an iframe element targeting yelp.com, set dimensions to 500x500 pixels, and save it locally.

**Expected Output**: Valid HTML file ready for browser loading.

**Success Indicators**:
- HTML file saves without errors
- Iframe src points correctly to http://yelp.com

### Step 3: Browser Verification
procedure: [[procedures/Verify-Iframe-Loading-in-Browser]]

**Objective**: Load the PoC HTML in a browser to confirm Yelp embeds successfully without blocking.

**Instructions**: Open the saved HTML file in a web browser and observe if Yelp content renders inside the iframe.

**Expected Output**: Yelp homepage visible within the 500x500 iframe boundaries.

**Success Indicators**:
- Site loads in iframe without errors or restrictions
- No browser warnings about framing

### Step 4: Proof Capture
procedure: [[procedures/Capture-Screenshot-as-Proof]]

**Objective**: Document the successful embedding for evidence of the vulnerability.

**Instructions**: With the PoC loaded in the browser, take a screenshot capturing the iframe with Yelp content.

**Expected Output**: Image file showing embedded Yelp site.

**Success Indicators**:
- Clear screenshot of iframe rendering Yelp
- No obstructions or errors in the capture

### Step 5: Subdomain Extension
procedure: [[procedures/Test-Vulnerability-on-Subdomains]]

**Objective**: Extend testing to Yelp subdomains to assess broader vulnerability scope.

**Instructions**: Modify the PoC HTML to target subdomains like m.yelp.com and biz.yelp.com, then reload in browser to verify embedding.

**Expected Output**: Subdomains load similarly in iframes without X-Frame-Options restrictions.

**Success Indicators**:
- Multiple subdomains confirmed vulnerable
- Consistent lack of header across tested endpoints

## Attack Chain Summary

### Key Achievements

1. Identified missing X-Frame-Options on yelp.com
2. Verified iframe embedding via PoC
3. Documented proof through screenshot
4. Confirmed impact on subdomains

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
