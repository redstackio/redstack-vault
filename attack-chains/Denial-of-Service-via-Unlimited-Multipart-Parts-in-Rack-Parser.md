---
id: ac-rack-multipart-dos-001
tags:
  - dos
  - rack
  - ruby
  - multipart
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Ruby
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-Rack-Endpoints]]'
  - '[[procedures/Craft-Multipart-DoS-Request]]'
  - '[[procedures/Send-DoS-Request-to-Trigger-Exhaustion]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.218Z'
description: >-
  Multi-stage attack exploiting Rack's multipart MIME parser by sending requests
  with excessive non-file parts to cause CPU and memory exhaustion on vulnerable
  Ruby on Rails applications.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Denial of Service via Unlimited Multipart Parts in Rack Parser

Multi-stage attack chain demonstrating a complete DoS workflow against vulnerable Rack-based applications by abusing the multipart parser's lack of limits on total parts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoints] --> B[Craft Malicious Request]
    B --> C[Send Request to Exhaust Resources]
    C --> D[DoS Achieved: CPU/Memory Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Ruby on Rails applications using vulnerable Rack versions (3.0.4.x < 3.0.4.2, 2.2.6.x < 2.2.6.3, 2.1.4 < 2.1.4.3, 2.0.9.x < 2.0.9.3)
- POST endpoints accepting multipart/form-data
- No proxy limiting request body size to double-digit MB

### Initial Access Requirements

- Network access to the target web application
- No authentication required if public POST endpoint exists
- Ability to send large HTTP POST requests

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoints
procedure: [[procedures/Identify-Vulnerable-Rack-Endpoints]]

**Objective**: Locate affected Rack versions and discover POST endpoints in the target Ruby on Rails application to prepare for exploitation.

**Instructions**: Review the application's tech stack to confirm Rack usage and version. Use tools like browser developer tools or reconnaissance scans to identify POST endpoints that handle multipart uploads, such as file upload forms.

**Expected Output**: List of vulnerable versions and endpoint URLs (e.g., /upload).

**Success Indicators**:
- Confirmed vulnerable Rack version
- Identified at least one multipart-accepting POST endpoint

### Step 2: Craft Malicious Multipart Request
procedure: [[procedures/Craft-Multipart-DoS-Request]]

**Objective**: Generate a POST request body with an excessive number of empty or field-only multipart parts to bypass file part limits and force unbounded parsing.

**Instructions**: Construct the request using a script or manual boundary definition. For example, create thousands of empty form fields like 'field1=', 'field2=', etc., within a multipart/form-data body. Use the following example structure (adapt boundary and part count):

```bash
# Example partial body (expand to 10,000+ parts for effect)
--boundary123
Content-Disposition: form-data; name="field1"


--boundary123
Content-Disposition: form-data; name="field2"


--boundary123--
```

**Expected Output**: A large request body file (e.g., dos_request.txt) exceeding typical limits but focused on non-file parts.

**Success Indicators**:
- Request body generated with 10,000+ parts
- Body size remains manageable (under proxy limits if present)

### Step 3: Send Request to Trigger Exhaustion
procedure: [[procedures/Send-DoS-Request-to-Trigger-Exhaustion]]

**Objective**: Transmit the crafted request to the target endpoint, causing the Rack parser to process unlimited parts and exhaust CPU/memory resources.

**Instructions**: Use curl to send the multipart request to the identified endpoint. Ensure the Content-Type header specifies multipart/form-data with the correct boundary. Execute using [[commands/curl-multipart-dos]]:

```bash
curl -X POST -H "Content-Type: multipart/form-data; boundary=boundary123" --data-binary @dos_request.txt https://target.com/upload
```

Monitor server response time and resource usage on the target (if accessible) or observe delayed responses to other requests.

**Expected Output**: Slow or failed response from the server; potential 500 errors or timeouts.

**Success Indicators**:
- Server response delayed by minutes
- High CPU/memory usage observed (via monitoring tools)
- Other concurrent requests blocked or OOM killer activated

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable components in Rack-based apps
2. Crafted efficient DoS payload exploiting parser limits
3. Achieved resource exhaustion leading to service disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
