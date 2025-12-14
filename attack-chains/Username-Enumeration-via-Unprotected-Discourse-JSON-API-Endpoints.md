---
tags:
  - information-disclosure
  - enumeration
  - api
  - discourse
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-HTTP-Request-with-Burp-Proxy]]'
  - '[[procedures/Send-Request-to-Burp-Intruder]]'
  - '[[procedures/Configure-Fuzzing-Payload-in-Burp-Intruder]]'
  - '[[procedures/Execute-and-Analyze-Burp-Intruder-Attack]]'
step_count: 4
techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.456Z'
description: >-
  Multi-stage attack exploiting lack of access controls in Discourse JSON API
  endpoints to enumerate category IDs and disclose sensitive user information
  like usernames.
skill_level: intermediate
impact_level: high
id: e648a8fd-9d7f-4616-8ce3-cc665cb523f6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Account Discovery]]'
---
# Username Enumeration via Unprotected Discourse JSON API Endpoints

Multi-stage attack chain demonstrating the exploitation of information disclosure in Discourse-based forums like community.brave.com, where JSON API endpoints expose user data without proper access controls on category IDs.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Intercept Request] --> B[Configure Intruder]
    B --> C[Launch Fuzzing]
    C --> D[Analyze Responses]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform running Discourse forum software
- Accessible HTTP/HTTPS endpoints (e.g., /c/category-name/{id}.json)
- No authentication required for public categories

### Initial Access Requirements

- Network access to the target forum (e.g., community.brave.com)
- Burp Suite configured as a proxy (browser traffic routed through Burp)
- No prior credentials needed, as endpoints are unauthenticated

## Detailed Attack Procedures

### Step 1: Intercept Request
procedure: [[procedures/Intercept-HTTP-Request-with-Burp-Proxy]]

**Objective**: Capture a legitimate HTTP GET request to a known JSON API endpoint to serve as a base for fuzzing.

**Instructions**: Configure your browser to use Burp Suite as a proxy, then navigate to a category page like /c/beta-builds/38 on the target forum to trigger a request to /c/beta-builds/38.json.

**Expected Output**: Intercepted HTTP GET request in Burp Proxy history, showing the category ID in the URL path.

**Success Indicators**:
- Request captured with 200 OK response containing JSON data
- Category ID parameter visible in the URL (e.g., /38.json)

### Step 2: Send to Intruder
procedure: [[procedures/Send-Request-to-Burp-Intruder]]

**Objective**: Transfer the captured request to Burp's Intruder module for automated payload injection and fuzzing.

**Instructions**: Right-click the intercepted request in Burp Proxy and select "Send to Intruder" to load it into the Intruder interface.

**Expected Output**: Request loaded in Intruder with default positions marked for potential payloads.

**Success Indicators**:
- Intruder tab opens with the request populated
- No errors in request parsing

### Step 3: Configure Payload
procedure: [[procedures/Configure-Fuzzing-Payload-in-Burp-Intruder]]

**Objective**: Set up the category ID as the fuzzing position and define sequential numeric payloads to enumerate all possible IDs.

**Instructions**: In Burp Intruder, mark the category ID (e.g., §38§) as the payload position using the Positions tab. Select the "Numbers" payload type, configure it for sequential integers starting from 1 (e.g., from 1 to 1000, step 1), and clear any other positions.

**Expected Output**: Payload positions updated, with the category ID marked for injection.

**Success Indicators**:
- Payload set list shows sequential numbers
- Test run confirms payload insertion in the URL

### Step 4: Launch and Analyze
procedure: [[procedures/Execute-and-Analyze-Burp-Intruder-Attack]]

**Objective**: Execute the fuzzing attack to probe multiple category IDs and identify those returning sensitive user data.

**Instructions**: Start the Intruder attack from the Intruder tab. Monitor the results table for responses with 200 OK status codes, then inspect the JSON response bodies for disclosures like usernames in category topics.

**Expected Output**: Table of responses showing varying lengths or content; successful hits reveal JSON with user arrays containing usernames and other details.

**Success Indicators**:
- Multiple 200 OK responses with JSON containing user data
- Enumeration of hidden or all categories, leading to unauthorized user info access

## Attack Chain Summary

### Key Achievements

1. Successful interception and fuzzing of API endpoints without authentication
2. Enumeration of all category IDs, exposing otherwise protected user lists
3. Identification of sensitive data leaks, enabling further reconnaissance like social engineering targets

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

---

*Last updated: 2024-10-01T00:00:00Z*
