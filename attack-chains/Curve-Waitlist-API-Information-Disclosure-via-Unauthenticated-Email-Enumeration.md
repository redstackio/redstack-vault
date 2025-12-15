---
tags:
  - information-disclosure
  - pii-leak
  - api-vulnerability
  - brute-force
  - enumeration
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Curve-Waitlist-API-Endpoint]]'
  - '[[procedures/Intercept-Waitlist-Track-Position-Request]]'
  - '[[procedures/Brute-Force-Email-Parameter-with-Burp-Intruder]]'
  - '[[procedures/Analyze-API-Responses-for-PII-Extraction]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:45.244Z'
description: >-
  Exploit an unauthenticated information disclosure vulnerability in the Curve
  waitlist API to enumerate and retrieve full PII for all waitlisted users by
  brute-forcing the email parameter.
skill_level: intermediate
impact_level: high
id: 72519637-7304-418c-a72f-9c57bb579c18
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Curve Waitlist API Information Disclosure via Unauthenticated Email Enumeration

Multi-stage attack chain demonstrating the exploitation of an unauthenticated API endpoint in Curve's waitlist system to disclose sensitive user PII, including names, mobile numbers, zipcodes, and IDs, through email brute-forcing. This vulnerability allows mass enumeration of waitlisted users' data, leading to privacy violations and potential GDPR non-compliance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Waitlist Page] --> B[Initiate Track Position]
    B --> C[Intercept Request with Burp]
    C --> D[Identify Vulnerable Endpoint]
    D --> E[Brute-Force Emails with Intruder]
    E --> F[Extract PII from Responses]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- Web browser (e.g., Chrome)
- List of target emails for brute-forcing (e.g., from breached data or generated lists)

### Target Environment

- Web platform
- Access to https://curve.com/usa waitlist page
- No authentication required; public-facing API at https://website-api.production.curve.app/api/waitlist/us
- Services: CloudFront, Envoy, Kubernetes
- Tech stack: JavaScript

### Initial Access Requirements

- Internet access to the target website
- No credentials needed
- Proxy setup for request interception (e.g., Burp Suite as proxy)

## Detailed Attack Procedures

### Step 1: Navigate to Waitlist Page and Initiate Track Position
procedure: [[procedures/Discover-Curve-Waitlist-API-Endpoint]]

**Objective**: Access the Curve waitlist functionality to trigger the API request and understand the initial interaction.

**Instructions**: Open a web browser and navigate to https://curve.com/usa. Locate and click the 'Track my position' button, then enter a test email address (e.g., example@gmail.com) and submit the form. Ensure your browser is configured to proxy traffic through Burp Suite for interception in subsequent steps.

**Expected Output**: Form submission triggers a POST request to the waitlist API.

**Success Indicators**:
- Waitlist page loads successfully
- Form submission completes without errors

### Step 2: Intercept the Track Position Request
procedure: [[procedures/Intercept-Waitlist-Track-Position-Request]]

**Objective**: Capture the HTTP request sent by the form to identify the API endpoint and parameters.

**Instructions**: With Burp Suite running as a proxy, submit the form again. In Burp's Proxy tab, intercept the outgoing POST request. Forward it to the server to complete the action, then review the request details in the HTTP history.

**Expected Output**: Intercepted POST request visible in Burp, showing JSON body with email parameter.

**Success Indicators**:
- Request intercepted successfully
- Response received (e.g., 200 OK with user position or error)

### Step 3: Identify the Vulnerable Endpoint and Request Format
procedure: [[procedures/Intercept-Waitlist-Track-Position-Request]]

**Objective**: Analyze the intercepted request to confirm the unauthenticated endpoint and its structure, revealing the information disclosure.

**Instructions**: In Burp's Repeater tab, resend the intercepted request and observe the response. Note the endpoint URL (https://website-api.production.curve.app/api/waitlist/us) and JSON payload {"email":"example@gmail.com"}. Test with a known waitlist email to verify PII disclosure in the response.

**Expected Output**: JSON response containing user details like phoneNumber, zipcode, name, _id, and position if the email exists.

**Success Indicators**:
- Endpoint confirmed as unauthenticated
- Sample PII returned in response

### Step 4: Brute-Force the Email Parameter
procedure: [[procedures/Brute-Force-Email-Parameter-with-Burp-Intruder]]

**Objective**: Automate enumeration by varying the email parameter across a list of potential victim emails to collect PII.

**Instructions**: Right-click the request in Burp and send it to Intruder. Mark the email value as a payload position (§email§). Load a wordlist of emails into Intruder (e.g., from a file with common or breached emails). Set the attack type to 'Sniper' and launch. Monitor for 200 OK responses indicating valid emails.

**Expected Output**: Multiple responses with varying PII data for matching emails.

**Success Indicators**:
- Valid emails identified by response length or status
- PII extracted for numerous users

### Step 5: Analyze Responses and Extract Sensitive Data
procedure: [[procedures/Analyze-API-Responses-for-PII-Extraction]]

**Objective**: Parse the Intruder results to compile and review the disclosed PII, assessing the full impact.

**Instructions**: In Burp Intruder's results table, filter for 200 OK responses. Inspect each JSON response for fields like phoneNumber, zipcode, name, _id, and position. Export or manually collect the data into a spreadsheet or file for analysis.

**Expected Output**: Compiled list of user PII, demonstrating mass disclosure.

**Success Indicators**:
- PII successfully extracted and correlated
- Evidence of full waitlist enumeration

## Attack Chain Summary

### Key Achievements

1. Discovered and confirmed unauthenticated API endpoint for waitlist lookup.
2. Brute-forced email parameter to enumerate all waitlisted users.
3. Retrieved comprehensive PII, enabling privacy violations and potential follow-on attacks like phishing.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
