---
tags:
  - xss
  - stored-xss
  - ruby-on-rails
  - active-storage
  - mathml
  - mimemagic
  - firefox
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-mimemagic-MIME-Type-Mappings-for-mml]]'
  - '[[procedures/Create-Malicious-MathML-XSS-Payload]]'
  - '[[procedures/Upload-Malicious-File-via-Active-Storage]]'
  - '[[procedures/Access-and-Trigger-XSS-in-Firefox]]'
  - '[[procedures/Reproduce-XSS-on-S3-Storage]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:07.782Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in Ruby on Rails
  Active Storage by uploading a MathML file with JavaScript payload, leading to
  arbitrary code execution in Firefox browsers.
skill_level: intermediate
impact_level: high
id: 1abe9517-a1b0-4078-b4ca-e9f48892f619
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
---

# Stored XSS via Malicious MathML Upload in Rails Active Storage

Multi-stage attack chain demonstrating a complete attack workflow exploiting stored XSS in Ruby on Rails Active Storage through MIME type mishandling of .mml files.

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
    A[Review MIME Mappings] --> B[Create MathML Payload]
    B --> C[Upload via Active Storage]
    C --> D[Access in Firefox]
    D --> E[Reproduce on S3]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e74c3c
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Firefox browser (version 63 or compatible for MathML rendering)
- Access to a Ruby on Rails application with Active Storage enabled

### Target Environment

- Ruby on Rails web application
- Active Storage configured (local or S3 backend)
- mimemagic library for MIME detection
- Network access to upload files and retrieve URLs

### Initial Access Requirements

- Authenticated access to the Rails application for file uploads
- No special privileges beyond standard user upload capabilities
- Firefox browser for exploitation testing

## Detailed Attack Procedures

### Step 1: Review MIME Type Mappings
procedure: [[procedures/Review-mimemagic-MIME-Type-Mappings-for-mml]]

**Objective**: Identify the MIME type assignment for .mml files to confirm vulnerability to MathML rendering.

**Instructions**: Examine the mimemagic library source code to verify that .mml extensions map to application/mathml+xml, which enables JavaScript execution in browsers like Firefox.

**Expected Output**: Confirmation of MIME type mapping in the library's tables.rb file.

**Success Indicators**:
- .mml mapped to application/mathml+xml
- No magic byte override for MathML files

### Step 2: Create Malicious MathML Payload
procedure: [[procedures/Create-Malicious-MathML-XSS-Payload]]

**Objective**: Develop a MathML file containing JavaScript that executes on user interaction in Firefox.

**Instructions**: Craft the payload using a <math> element with a javascript: href attribute, referencing known XSS techniques for MathML.

**Expected Output**: A valid .mml file that renders in Firefox and triggers alert on click.

**Success Indicators**:
- Payload file created without syntax errors
- Local test in Firefox shows clickable element triggering JavaScript

### Step 3: Upload Malicious File via Active Storage
procedure: [[procedures/Upload-Malicious-File-via-Active-Storage]]

**Objective**: Upload the payload to the Rails application, leveraging extension-based MIME detection.

**Instructions**: Use the application's file upload interface to submit the .mml file; Active Storage will detect the MIME type as application/mathml+xml due to fallback from mimemagic.

**Expected Output**: Successful upload with a direct URL to the stored file.

**Success Indicators**:
- File uploaded without rejection
- URL accessible and returns the .mml content with correct MIME type

### Step 4: Access and Trigger XSS in Firefox
procedure: [[procedures/Access-and-Trigger-XSS-in-Firefox]]

**Objective**: View the uploaded file in Firefox to render the MathML and execute the JavaScript payload.

**Instructions**: Open the direct URL to the uploaded .mml file in Firefox and click within the rendered MathML content to activate the javascript:alert.

**Expected Output**: Browser alert box displaying the current location, confirming XSS execution.

**Success Indicators**:
- MathML renders without errors
- Click triggers arbitrary JavaScript execution

### Step 5: Reproduce on S3 Storage
procedure: [[procedures/Reproduce-XSS-on-S3-Storage]]

**Objective**: Validate the vulnerability persists when Active Storage uses external services like S3.

**Instructions**: Configure Active Storage to use S3, re-upload the payload, and repeat access in Firefox to confirm consistent exploitation.

**Expected Output**: Identical XSS trigger on the S3-hosted file URL.

**Success Indicators**:
- Upload succeeds to S3
- XSS reproduces independently of storage backend

## Attack Chain Summary

### Key Achievements

1. Identified MIME type flaw enabling MathML XSS
2. Crafted and uploaded executable payload
3. Achieved JavaScript execution in victim browsers
4. Demonstrated persistence across storage services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
