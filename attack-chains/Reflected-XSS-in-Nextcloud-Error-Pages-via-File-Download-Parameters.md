---
id: ac-nextcloud-xss-2017
tags:
  - xss
  - reflected-xss
  - nextcloud
  - information-disclosure
  - html-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-File-Download-Endpoint-in-Nextcloud]]'
  - '[[procedures/Exploit-HTML-Injection-for-Reflected-XSS-in-Nextcloud]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-13T23:52:25.040Z'
description: >-
  A multi-stage attack exploiting inadequate escaping in Nextcloud error pages
  to inject HTML via file download parameters, enabling reflected XSS and path
  disclosure, though limited by CSP.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
---
# Reflected XSS in Nextcloud Error Pages via File Download Parameters

Multi-stage attack chain demonstrating exploitation of reflected XSS in Nextcloud error pages through manipulated file download parameters, leading to HTML injection and potential phishing on logged-in users, alongside path disclosure. The attack is mitigated by strict CSP in modern browsers, reducing exploitability.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Inject HTML Payload]
    B --> C[Trigger Error Page XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for payload testing
- [[Burp Suite]] or similar proxy for parameter manipulation (optional)

### Target Environment

- Nextcloud Server (Web platform)
- PHP-based application
- Access to logged-in session (requires valid credentials)
- Network access to the Nextcloud instance

### Initial Access Requirements

- Valid user credentials for Nextcloud login
- Direct network access to the web interface
- No prior elevated access needed, but logged-in state required for full impact

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint

procedure: [[procedures/Identify-Vulnerable-File-Download-Endpoint-in-Nextcloud]]

**Objective**: Locate and test the file download AJAX endpoint to confirm vulnerability to parameter manipulation that triggers error pages with unescaped output.

**Instructions**: Log in to the Nextcloud instance and navigate to the files app. Use a tool like curl or browser to send a request to the endpoint `/index.php/apps/files/ajax/download.php` with manipulated parameters such as `files` set to a null byte (`%00`) and `dir` to invalid values. This forces an error condition.

Execute a test request using [[commands/curl-nextcloud-download-test]]:

```bash
curl -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid/path" -b "cookie=logged_in_session"
```

**Expected Output**: An error page response containing unescaped elements from the parameters, potentially revealing server paths.

**Success Indicators**:
- Error page loads with reflected parameter values
- Server path disclosure visible in the response

### Step 2: Exploit HTML Injection

procedure: [[procedures/Exploit-HTML-Injection-for-Reflected-XSS-in-Nextcloud]]

**Objective**: Inject arbitrary HTML into the error page via the `dir` parameter to demonstrate reflected XSS, enabling potential phishing or script execution on affected users.

**Instructions**: Build on the identified endpoint by appending closing HTML tags and a payload to the `dir` parameter, such as `</p><script>alert('XSS')</script>`. Send the request while logged in to trigger the injection.

Execute the exploitation request using [[commands/curl-nextcloud-xss-payload]]:

```bash
curl -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid</p><script>alert('XSS')</script>" -b "cookie=logged_in_session"
```

Inspect the response in a browser to view the rendered error page. Note that CSP may block script execution.

**Expected Output**: Error page renders with injected HTML, showing the payload unescaped; potential alert if CSP allows.

**Success Indicators**:
- Injected HTML appears in the page source without escaping
- Path disclosure confirms installation directory
- XSS payload reflects (though execution limited)

## Attack Chain Summary

### Key Achievements

1. Successful identification of vulnerable file download endpoint
2. HTML injection leading to reflected XSS on error pages
3. Disclosure of full Nextcloud installation path for further reconnaissance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Gather Victim Host Information]] Gather Victim Host Information

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
