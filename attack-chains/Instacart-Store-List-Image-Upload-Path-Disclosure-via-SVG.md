---
tags:
  - information-disclosure
  - path-leak
  - rmagick
  - ruby-on-rails
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Instacart-Store-List]]'
  - '[[procedures/Upload-SVG-Image-via-URL]]'
  - '[[procedures/Observe-Path-Disclosure-Error]]'
step_count: 3
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.084Z'
description: >-
  Demonstrates information disclosure of internal server file paths through
  error handling in the Instacart store list background image upload feature
  when using unsupported SVG formats.
skill_level: beginner
impact_level: medium
id: e3f78e55-8f32-48e3-a9fa-dc24cae1a77b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Instacart Store List Image Upload Path Disclosure via SVG

Multi-stage attack chain demonstrating a complete attack workflow for disclosing internal server paths via error messages in Instacart's image upload feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Store List] --> B[Upload SVG via URL]
    B --> C[Observe Error Response]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)
- Access to Instacart web application

### Target Environment

- Instacart web platform
- No specific services/ports required beyond standard HTTPS (443)
- Network access: Public internet

### Initial Access Requirements

- Valid Instacart user account (free signup possible)
- No elevated privileges needed
- Direct web access to app.instacart.com

## Detailed Attack Procedures

### Step 1: Create Store List
procedure: [[procedures/Create-Instacart-Store-List]]

**Objective**: Establish a store list to enable the background image upload functionality.

**Instructions**: Log in to the Instacart web application, navigate to the lists section, and create a new list associated with a store. Select any store from the available options to link the list.

**Expected Output**: Confirmation of list creation with an editable interface for the list details.

**Success Indicators**:
- New list appears in the user's lists dashboard
- Option to customize the list (including background image) is available

### Step 2: Upload SVG Image via URL
procedure: [[procedures/Upload-SVG-Image-via-URL]]

**Objective**: Trigger the image upload process using an unsupported SVG format to invoke error handling in the backend.

**Instructions**: In the list customization interface, locate the background image upload field. Select the option to add an image from a URL and input a publicly accessible SVG file URL (e.g., https://example.com/test.svg). Attempt to save or apply the upload.

**Expected Output**: Upload attempt fails with an error response from the server.

**Success Indicators**:
- Error message is returned in the response
- No successful image upload occurs due to format restriction

### Step 3: Observe Path Disclosure Error
procedure: [[procedures/Observe-Path-Disclosure-Error]]

**Objective**: Capture and analyze the error response to extract disclosed internal server file paths.

**Instructions**: Inspect the JSON error response from the failed upload, focusing on the rmagick manipulation error details. The response will include the full temporary file path where the uploaded content was stored.

**Expected Output**: JSON object containing error details with leaked path, e.g., {"error": "rmagick error: /tmp/uploads/abc123.svg"}.

**Success Indicators**:
- Internal filesystem path (e.g., /tmp/uploads/) is visible in the error message
- Path reveals server environment details like temporary directories

## Attack Chain Summary

### Key Achievements

1. Successful creation of a target list for upload testing
2. Triggering of format validation error with unsupported SVG
3. Extraction of sensitive internal path information for reconnaissance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
