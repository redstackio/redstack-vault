---
tags:
  - idor
  - web
  - api
  - data-leak
  - pii-leak
  - booking-system
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Booking-Cancellation-Endpoint]]'
  - '[[procedures/Modify-Booking-ID-for-IDOR-Exploitation]]'
  - '[[procedures/Submit-Modified-Cancellation-Request]]'
step_count: 3
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.887Z'
description: >-
  An Insecure Direct Object Reference (IDOR) vulnerability in the Eternal
  application's table booking system allows authenticated users to cancel any
  other user's booking and leak sensitive personal information like emails,
  mobile numbers, and UUIDs by manipulating the booking ID in API requests.
skill_level: intermediate
impact_level: high
id: da6e4a1f-4519-4dd7-ab2c-d1f48990238a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Table Booking Cancellation to Cancel Bookings and Leak User PII

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in the Eternal table booking API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Endpoint] --> B[Modify Booking ID]
    B --> C[Submit Cancellation Request]
    C --> D[Booking Canceled and PII Leaked]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for inspecting requests

### Target Environment

- Web application with table booking system (e.g., Eternal app)
- API endpoint for booking management
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Authenticated user account in the application
- Ability to make one's own booking to observe legitimate requests
- Network access to the web application

## Detailed Attack Procedures

### Step 1: Identify Booking Cancellation Endpoint
procedure: [[procedures/Identify-Booking-Cancellation-Endpoint]]

**Objective**: Locate the API endpoint used for cancelling table bookings by inspecting legitimate requests.

**Instructions**: Log in to the Eternal application, create a test table booking, then attempt to cancel it while monitoring network traffic in browser dev tools or a proxy. Identify the request containing the booking ID parameter.

**Expected Output**: API request details, such as POST /api/bookings/{id}/cancel with booking ID in body or path.

**Success Indicators**:
- Endpoint URL and parameters observed
- Booking ID format noted (e.g., sequential integers or UUIDs)

### Step 2: Modify Booking ID for IDOR Exploitation
procedure: [[procedures/Modify-Booking-ID-for-IDOR-Exploitation]]

**Objective**: Alter the booking ID in the request to target another user's booking, testing for authorization bypass.

**Instructions**: Using the identified endpoint, replace your own booking ID with a guessed or enumerated ID of another user (e.g., increment by 1 or use known IDs from listings). Prepare the modified request without submitting yet.

**Expected Output**: Modified request ready for submission, confirming ID format is predictable.

**Success Indicators**:
- Request modification successful without syntax errors
- Target booking ID references a different user's data

### Step 3: Submit Modified Cancellation Request
procedure: [[procedures/Submit-Modified-Cancellation-Request]]

**Objective**: Execute the tampered request to cancel the target booking and extract leaked sensitive data.

**Instructions**: Send the modified request using a tool like curl. For example, use [[commands/curl-cancel-table-booking]] with the altered booking ID:

```bash
curl -X POST https://eternal.example.com/api/v1/bookings/cancel \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"booking_id": "TARGET_BOOKING_ID"}'
```

Validate the response for cancellation success and data leakage.

**Expected Output**: JSON response confirming cancellation and including user PII (email, mobile, UUID).

**Success Indicators**:
- Booking cancelled without ownership error
- Sensitive data (email, mobile, UUID) returned in response

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access and manipulate other users' bookings
2. Cancelled arbitrary table bookings, disrupting service
3. Leaked personally identifiable information (PII) including emails, mobile numbers, and UUIDs

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
