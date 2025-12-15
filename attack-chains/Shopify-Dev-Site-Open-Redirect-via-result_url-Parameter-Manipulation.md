---
tags:
  - open-redirect
  - phishing
  - shopify
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Navigate-to-Shopify-Dev-and-Perform-Search]]'
  - '[[procedures/Copy-and-Modify-Search-Result-URL]]'
  - '[[procedures/Trigger-Open-Redirect-via-Modified-URL]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.571Z'
description: >-
  Multi-stage attack chain exploiting an open redirect vulnerability in the
  Shopify developer documentation search functionality by manipulating the
  'result_url' parameter to bypass domain validation and redirect to arbitrary
  external sites, enabling potential phishing attacks.
id: 54dd6f83-64b6-4fc9-a381-eb62e322ce86
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Shopify Dev Site Open Redirect via result_url Parameter Manipulation

Multi-stage attack chain demonstrating exploitation of an open redirect in the Shopify developer documentation site (www.shopify.dev) search functionality. By manipulating the 'result_url' parameter with a prepended '@' symbol, attackers can bypass validation restricting redirects to shopify.dev domains, allowing redirection to external sites like www.facebook.com. This can facilitate phishing through social engineering, though it requires user interaction to click the malicious link.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate and Search] --> B[Modify URL Parameter] --> C[Trigger Redirect]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to https://shopify.dev
- No special services or ports required

### Initial Access Requirements

- Public internet access
- No credentials needed
- Direct browser navigation to the target site

## Detailed Attack Procedures

### Step 1: Navigate and Search
procedure: [[procedures/Navigate-to-Shopify-Dev-and-Perform-Search]]

**Objective**: Access the Shopify developer site and generate a search result link containing the vulnerable 'result_url' parameter.

**Instructions**: Open a web browser and navigate to the Shopify introduction page at https://shopify.dev/concepts/shopify-introduction. Locate and interact with the search box on the page. Enter the query 'POC' into the search box and press Enter to perform the search, generating results.

**Expected Output**: A list of search results appears, with the first result labeled 'POS' or similar.

**Success Indicators**:
- Search results page loads successfully
- At least one result link is available for copying

### Step 2: Copy and Modify Search Result URL
procedure: [[procedures/Copy-and-Modify-Search-Result-URL]]

**Objective**: Extract the search result URL and alter the 'result_url' parameter to include an '@' prefix followed by an external domain, bypassing validation.

**Instructions**: Right-click on the first search result (e.g., 'POS') and select 'Copy link address'. The copied URL will be in the format: https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=%2Ftools%2Fapp-bridge%2Factions%2Fpos&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false. Edit the 'result_url' parameter by replacing its value (e.g., %2Ftools%2Fapp-bridge%2Factions%2Fpos) with '@www.facebook.com' (URL-encode if necessary, but '@' works directly).

**Expected Output**: Modified URL ready for use, e.g., https://shopify.dev/search/result?query=poc&rank=1&result_gid=ae6c33f6-62d4-4ff2-966e-96c09267ee87&result_url=@www.facebook.com&search_uuid=34eeea9d-2b99-4f86-bf00-807efd4036ba&suggested=false.

**Success Indicators**:
- URL successfully modified without syntax errors
- Parameter change is visible in the address bar or editor

### Step 3: Trigger Open Redirect
procedure: [[procedures/Trigger-Open-Redirect-via-Modified-URL]]

**Objective**: Access the modified URL to exploit the vulnerability and observe the redirect to the external domain.

**Instructions**: Paste the modified URL into the browser's address bar and press Enter. The site will process the request, but due to the '@' bypass, it will redirect to the external domain (e.g., www.facebook.com) instead of staying within shopify.dev.

**Expected Output**: Browser redirects to the specified external site, confirming the open redirect.

**Success Indicators**:
- Immediate redirect to external domain
- No error messages from Shopify site
- Network logs (if inspected) show redirect response

## Attack Chain Summary

### Key Achievements

1. Successful generation of a vulnerable search result URL
2. Bypass of domain validation using '@' in 'result_url' parameter
3. Demonstration of arbitrary external redirect, enabling phishing vectors

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
