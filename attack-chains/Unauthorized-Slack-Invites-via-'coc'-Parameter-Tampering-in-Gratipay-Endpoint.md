---
tags:
  - auth-bypass
  - enumeration
  - slack
  - parameter-tampering
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-Invite-Validation-with-coc-Parameter]]'
  - '[[procedures/Force-Send-Slack-Invite-Emails]]'
  - '[[procedures/Enumerate-Slack-Usernames-via-Response-Codes]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.626Z'
description: >-
  Multi-stage attack exploiting improper validation in the Gratipay Slack invite
  endpoint to force unauthorized invitations and enumerate valid usernames.
skill_level: beginner
impact_level: low
id: df1c001b-87eb-4655-ade6-56838cfbaed4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Unauthorized Slack Invites via 'coc' Parameter Tampering in Gratipay Endpoint

Multi-stage attack chain demonstrating exploitation of a validation bypass in the Gratipay Slack invite system, allowing forced invitations to arbitrary emails and username enumeration through response code differences. The vulnerability stems from client-side checks that can be bypassed by tampering with the 'coc' parameter in POST requests to the /invite endpoint on gratipay-slackin.herokuapp.com. Despite the Slack channel being public, this enables spam invites without rate limits and potential discovery of valid user emails.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Modify POST Request] --> B[Send Invite with Bypass]
    B --> C[Enumerate via Responses]
    C --> D[Arbitrary Invites Sent]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for request modification
- [[commands/curl-post-invite-with-coc-bypass]] for scripted testing

### Target Environment

- Web platform
- Access to inside.gratipay.com/appendices/chat page (public)
- No authentication required

### Initial Access Requirements

- Public internet access
- No credentials needed
- Ability to intercept and modify HTTP requests

## Detailed Attack Procedures

### Step 1: Bypass Invite Validation
procedure: [[procedures/Bypass-Invite-Validation-with-coc-Parameter]]

**Objective**: Tamper with the 'coc' parameter to bypass client-side checks preventing duplicate invites.

**Instructions**: Inspect the network traffic from inside.gratipay.com/appendices/chat when attempting a normal invite. Modify the JSON payload by setting "coc" to 1 before sending the POST to /invite.

Use [[commands/curl-post-invite-with-coc-bypass]] to test:

```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"test@example.com"}'
```

**Expected Output**: HTTP 400 Bad Request with message about prior invitation, but validation bypassed.

**Success Indicators**:
- Request accepted despite modification
- No client-side block on duplicate invites

### Step 2: Force Send Invite Emails
procedure: [[procedures/Force-Send-Slack-Invite-Emails]]

**Objective**: Trigger the server to send invite emails to arbitrary addresses without rate limiting.

**Instructions**: After bypassing validation, the server processes the invite regardless of the error response. Repeat the modified POST for multiple emails.

Execute [[commands/curl-post-invite-with-coc-bypass]] with different emails:

```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"arbitrary@domain.com"}'
```

**Expected Output**: Invite email from feedback@slack.com arrives at the target email, inviting to gratipay.slack.com.

**Success Indicators**:
- Email received despite 400 response
- No rate limits enforced on repeated requests

### Step 3: Enumerate Valid Usernames
procedure: [[procedures/Enumerate-Slack-Usernames-via-Response-Codes]]

**Objective**: Discover valid Slack-associated emails by observing HTTP response differences.

**Instructions**: Send POST requests with guessed email formats (e.g., username@gratipay.com). Analyze responses: 303 for valid, 400 for invalid.

Script or manually use [[commands/curl-post-invite-with-coc-bypass]] in a loop:

```bash
for email in user1@gratipay.com user2@gratipay.com; do
  curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"$email"}' -w "%{http_code}\n"
  sleep 1
done
```

**Expected Output**: 303 See Other for valid emails, 400 Bad Request for invalid.

**Success Indicators**:
- Different response codes for valid vs. invalid emails
- Potential list of enumerated usernames

## Attack Chain Summary

### Key Achievements

1. Bypassed validation to force unlimited Slack invites
2. Sent invites to arbitrary emails despite server errors
3. Enumerated valid usernames via response code side-channel

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
