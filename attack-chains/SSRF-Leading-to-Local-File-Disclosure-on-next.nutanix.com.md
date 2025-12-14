---
tags:
  - ssrf
  - file-disclosure
  - nutanix
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-SSRF-for-Local-File-Disclosure]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.474Z'
description: >-
  A Server-Side Request Forgery vulnerability on next.nutanix.com that allows
  unauthorized access to internal resources and local file disclosure.
skill_level: intermediate
impact_level: high
id: 66fac776-5b28-44fb-9ce4-9759c3789283
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF Leading to Local File Disclosure on next.nutanix.com

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Server-Side Request Forgery (SSRF) vulnerability to disclose local files on the Nutanix next.nutanix.com domain.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify Vulnerable Endpoint] --> B[Exploitation: Trigger SSRF for File Disclosure]
    B --> C[Collection: Retrieve Disclosed Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-ssrf-payload]]

### Target Environment

- Target Platform: Web application on next.nutanix.com
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Public internet access to the target domain

### Initial Access Requirements

- No credentials required
- External network position (no internal access needed initially)
- Prior access not needed; vulnerability is public-facing

## Detailed Attack Procedures

### Step 1: Reconnaissance - Identify Vulnerable Endpoint

procedure: [[procedures/Exploit-SSRF-for-Local-File-Disclosure]]

**Objective**: Locate the SSRF-vulnerable parameter on next.nutanix.com, typically in a URL input field or API endpoint that processes user-supplied URLs without validation.

**Instructions**: Use browser developer tools or a proxy like Burp Suite to inspect requests to next.nutanix.com. Look for features like URL fetching, image loading, or integration with external services that could be abused for SSRF. Test basic SSRF by injecting a localhost URL such as http://127.0.0.1 in the parameter.

Execute a basic test using [[commands/curl-ssrf-payload]] to probe for SSRF:

```bash
curl -X POST 'https://next.nutanix.com/api/endpoint' -d 'url=http://127.0.0.1/admin' -H 'Content-Type: application/x-www-form-urlencoded'
```

**Expected Output**: Server response indicating internal access, such as a 200 OK with internal page content or an error revealing internal connectivity.

**Success Indicators**:
- Response contains internal server data or confirms localhost access
- No external URL fetching; instead, internal resolution

### Step 2: Exploitation - Trigger SSRF for File Disclosure

procedure: [[procedures/Exploit-SSRF-for-Local-File-Disclosure]]

**Objective**: Craft and send a malicious payload to access and disclose local files via the SSRF vulnerability, such as /etc/passwd or configuration files.

**Instructions**: Once the vulnerable parameter is identified, modify the payload to use the file:// protocol to read local files. Send the request using [[commands/curl-ssrf-payload]] with a file URI.

```bash
curl -X POST 'https://next.nutanix.com/api/endpoint' -d 'url=file:///etc/passwd' -H 'Content-Type: application/x-www-form-urlencoded'
```

If the endpoint supports GET, use: 

```bash
curl 'https://next.nutanix.com/endpoint?url=file:///etc/passwd'
```

Parse the response for file contents. Escalate by targeting sensitive files like /proc/version or application configs.

**Expected Output**: Response body containing the contents of the requested local file, e.g., user account listings from /etc/passwd.

**Success Indicators**:
- File contents returned in the HTTP response
- No access denied errors; successful internal file read

## Attack Chain Summary

### Key Achievements

1. Identified SSRF vulnerability in input validation on next.nutanix.com
2. Achieved local file disclosure, exposing sensitive server information
3. Demonstrated high-impact unauthorized access to internal resources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
