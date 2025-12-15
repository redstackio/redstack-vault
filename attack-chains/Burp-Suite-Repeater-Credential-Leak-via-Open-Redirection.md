---
id: ac-burp-repeater-leak-001
tags:
  - credential-leak
  - information-disclosure
  - open-redirection
  - burp-suite
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Suite-Repeater]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Desktop Application
  - Web
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Open-Redirection-Endpoint]]'
  - '[[procedures/Configure-Burp-Suite-Platform-Authentication]]'
  - '[[procedures/Issue-Request-to-Redirection-Endpoint-in-Repeater]]'
  - '[[procedures/Follow-Redirection-in-Burp-Repeater]]'
  - '[[procedures/Observe-Credential-Leak-on-External-Domain]]'
step_count: 5
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:31:19.397Z'
description: >-
  Demonstrates how Burp Suite's Repeater feature leaks HTTP Basic authentication
  credentials to external domains when following redirections, enabling
  unauthorized credential disclosure.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Burp Suite Repeater Credential Leak via Open Redirection

Multi-stage attack chain demonstrating how an attacker can exploit Burp Suite's Repeater feature to leak configured HTTP Basic authentication credentials to an external domain through an open redirection vulnerability.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Redirection] --> B[Configure Auth]
    B --> C[Send Request]
    C --> D[Follow Redirect]
    D --> E[Leak Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Burp-Suite-Repeater]]

### Target Environment

- Desktop application running Burp Suite (Java-based)
- Controlled web server for open redirection (e.g., Apache/PHP on Linux)
- Attacker-controlled domain (e.g., evil.com) to capture leaked requests
- Network access to both controlled site and external domain

### Initial Access Requirements

- Administrative access to set up a controlled site with open redirection
- Burp Suite installed and running
- No prior credentials needed, but demonstrates leak of configured auth

## Detailed Attack Procedures

### Step 1: Set Up Open Redirection

procedure: [[procedures/Set-Up-Open-Redirection-Endpoint]]

**Objective**: Create a vulnerable endpoint on a controlled site that redirects to arbitrary external URLs, simulating a redirection flaw exploitable by Burp Suite.

**Instructions**: Deploy a simple PHP script on a server like example.com to handle open redirections. Ensure the server is accessible from the Burp Suite environment.

**Expected Output**: A functional /redirect.php endpoint that redirects based on the 'url' parameter.

**Success Indicators**:
- Endpoint responds with a 302 redirect when queried
- Redirect location matches the provided URL parameter

### Step 2: Configure Platform Authentication

procedure: [[procedures/Configure-Burp-Suite-Platform-Authentication]]

**Objective**: Set up HTTP Basic authentication in Burp Suite for the controlled site, which will be inadvertently forwarded during redirection.

**Instructions**: In Burp Suite, navigate to the Platform Authentication settings and add credentials for example.com.

**Expected Output**: Authentication configured, with credentials applied to requests targeting the domain.

**Success Indicators**:
- Burp Suite logs show Authorization header added to requests for example.com
- Test request to example.com includes base64-encoded credentials

### Step 3: Issue Request to Redirection Endpoint in Repeater

procedure: [[procedures/Issue-Request-to-Redirection-Endpoint-in-Repeater]]

**Objective**: Use Burp Repeater to send an initial request to the open redirection endpoint, targeting an attacker-controlled domain.

**Instructions**: Paste or craft a GET request in Repeater for /redirect.php?url=http://evil.com on Host: example.com, then send it.

**Expected Output**: Initial response from example.com with a 302 redirect to http://evil.com.

**Success Indicators**:
- Repeater shows 302 status code
- Location header points to the external domain

### Step 4: Follow Redirection in Burp Repeater

procedure: [[procedures/Follow-Redirection-in-Burp-Repeater]]

**Objective**: Trigger the Follow Redirection feature, causing Burp to generate and send a new request to the external domain while preserving the Authorization header.

**Instructions**: After sending the initial request, click the 'Follow redirection' button in Repeater to process the redirect.

**Expected Output**: A new request tab or log entry showing the forwarded request to http://evil.com with the Authorization header intact.

**Success Indicators**:
- New request includes Authorization: Basic header
- Request is sent to the external domain

### Step 5: Observe Credential Leak on External Domain

procedure: [[procedures/Observe-Credential-Leak-on-External-Domain]]

**Objective**: Capture and verify the leaked credentials on the attacker-controlled site, confirming the disclosure.

**Instructions**: Monitor logs or a capture tool on evil.com to inspect incoming requests for the leaked Authorization header.

**Expected Output**: Request to evil.com containing Authorization: Basic dXNlcjpwYXNz (base64 for user:pass).

**Success Indicators**:
- Credentials decoded from base64 in the header
- Potential for misuse if credentials grant access to resources

## Attack Chain Summary

### Key Achievements

1. Successful setup of an open redirection endpoint to simulate a vulnerable site.
2. Configuration of sensitive credentials in Burp Suite that are leaked without user awareness.
3. Exploitation of Repeater's redirection handling to forward auth headers cross-domain.
4. Capture of leaked credentials, enabling potential unauthorized access.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### MITRE ATT&CK Tactics

- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
