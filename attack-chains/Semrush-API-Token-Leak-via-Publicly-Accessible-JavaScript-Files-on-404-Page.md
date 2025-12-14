---
tags:
  - information-disclosure
  - api-token-leak
  - javascript
  - semrush
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Trigger-404-Page-to-Reveal-JavaScript-Files]]'
  - '[[procedures/Inspect-404-Page-Source-for-Internal-JS-References]]'
  - '[[procedures/Download-Publicly-Accessible-Internal-JavaScript-Files]]'
  - '[[procedures/Extract-Embedded-API-Token-from-JavaScript-Code]]'
  - '[[procedures/Utilize-Leaked-API-Token-to-Access-Internal-Statistics]]'
step_count: 5
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Credentials In Files]]'
  - '[[T1078.004]]'
  - '[[Data from Information Repositories]]'
description: >-
  A multi-step information disclosure attack exploiting misconfigured publicly
  accessible JavaScript files on a 404 error page to leak an internal API token,
  enabling unauthorized access to Semrush's system statistics.
skill_level: beginner
impact_level: high
id: 7dcaae5a-8ab0-489e-ad30-717508fbaa03
created_at: '2025-12-14T17:32:39.198Z'
updated_at: '2025-12-14T17:32:39.198Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Credentials In Files]]'
  - '[[T1078.004]]'
  - '[[Data from Information Repositories]]'
---
# Semrush API Token Leak via Publicly Accessible JavaScript Files on 404 Page

Multi-stage attack chain demonstrating an information disclosure vulnerability where internal API tokens are exposed in publicly accessible JavaScript files loaded on a 404 error page, leading to unauthorized access to internal system statistics.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Trigger 404 Page] --> B[Inspect Source Code]
    B --> C[Access JS Files]
    C --> D[Extract API Token]
    D --> E[Access Internal Statistics]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web application hosted by Semrush
- Publicly accessible website (e.g., semrush.com or related domains)
- No authentication required for initial access

### Initial Access Requirements

- Internet access to the target domain
- No prior credentials needed
- Basic knowledge of web navigation and source code inspection

## Detailed Attack Procedures

### Step 1: Trigger 404 Page
procedure: [[procedures/Trigger-404-Page-to-Reveal-JavaScript-Files]]

**Objective**: Access a non-existent page to generate a 404 error response, which inadvertently loads and exposes references to internal JavaScript files in the page source.

**Instructions**: Open a web browser and navigate to a URL on the target domain that does not exist, such as appending a random path like "/nonexistent-page" to the base URL (e.g., https://www.semrush.com/nonexistent-page). This triggers the 404 error page, whose source code will include script tags referencing multiple JavaScript files, including internal ones.

**Expected Output**: A 404 error page loads, and viewing the page source reveals <script> tags listing various JS files.

**Success Indicators**:
- 404 error page displayed
- Page source contains references to JavaScript files, some marked as internal (e.g., related to system statistics)

### Step 2: Inspect 404 Page Source
procedure: [[procedures/Inspect-404-Page-Source-for-Internal-JS-References]]

**Objective**: Examine the HTML source of the 404 page to identify references to internal JavaScript files that may contain sensitive information.

**Instructions**: Right-click on the 404 page and select "View Page Source" (or press Ctrl+U). Search for <script src=...> tags in the source code. Look for files with names indicating internal functionality, such as those related to Semrush's system statistics interface.

**Expected Output**: List of JavaScript file URLs in the source, including paths to internal JS files that are unexpectedly public.

**Success Indicators**:
- Identification of multiple JS file references
- Discovery of internal JS files (e.g., stats-related scripts) without authentication barriers

### Step 3: Access JavaScript Files
procedure: [[procedures/Download-Publicly-Accessible-Internal-JavaScript-Files]]

**Objective**: Directly access and retrieve the content of the identified internal JavaScript files, which are publicly available due to misconfiguration.

**Instructions**: Copy the URLs of the internal JS files from the source code (e.g., https://example.semrush.com/internal/stats.js). Paste them into a new browser tab or use a download tool to fetch the file. The files should load without any authentication prompts.

**Expected Output**: Raw JavaScript code displayed or downloaded, containing application logic and potentially sensitive data.

**Success Indicators**:
- JS files load successfully in the browser
- No redirects or access denied errors occur

### Step 4: Extract API Token
procedure: [[procedures/Extract-Embedded-API-Token-from-JavaScript-Code]]

**Objective**: Analyze the downloaded JavaScript code to locate and extract the embedded internal API token for api.semrush.com.

**Instructions**: Open the JS file in a text editor or browser console. Search for strings like "api.semrush.com" or common API token patterns (e.g., long alphanumeric strings used in API calls). Copy the token value found in the code, such as in an AJAX request or configuration object.

**Expected Output**: A valid API token string extracted from the JS code, e.g., a Bearer token or API key.

**Success Indicators**:
- Token identified in the code (e.g., var apiToken = 'abc123...')
- Token appears to be for internal endpoints based on context

### Step 5: Access Internal Statistics
procedure: [[procedures/Utilize-Leaked-API-Token-to-Access-Internal-Statistics]]

**Objective**: Use the extracted API token to make unauthorized requests to internal API endpoints, retrieving sensitive system statistics.

**Instructions**: Use a tool like curl or Postman to send requests to api.semrush.com endpoints with the token in the Authorization header. For example, query a stats endpoint: curl -H "Authorization: Bearer [TOKEN]" https://api.semrush.com/internal/stats. Replace [TOKEN] with the extracted value and adjust the endpoint based on JS code hints.

**Expected Output**: JSON response containing internal system statistics, such as usage metrics or server data.

**Success Indicators**:
- API responds with 200 OK and data
- Access to restricted internal information without further authentication

## Attack Chain Summary

### Key Achievements

1. Exposed internal JavaScript files via 404 page misconfiguration
2. Leaked API token enabling unauthorized API access
3. Retrieved sensitive internal system statistics from Semrush

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]
- [[Credentials In Files]]
- [[T1078.004]]
- [[Data from Information Repositories]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Credential Access]]
- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2024-10-04T00:00:00Z*
