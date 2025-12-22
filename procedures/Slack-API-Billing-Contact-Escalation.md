---
id: proc-slack-billing-escalation-001
tags:
  - privilege-escalation
  - slack
  - api
  - billing
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/slack-add-billing-contact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:36.725Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Slack-API-Billing-Contact-Escalation

## Summary

This procedure exploits a privilege escalation vulnerability in Slack's API, allowing team admins to add unauthorized emails to the billing contacts list—a function intended only for team owners. By sending a crafted POST request with an admin token, attackers can potentially gain access to billing information or enable further unauthorized modifications.

## Description

In Slack workspaces, billing contact management is restricted to team owners to protect sensitive financial data. However, due to insufficient authorization checks on the /api/team.billing.addContact endpoint, team admins can bypass this restriction. The attack involves authenticating as an admin, crafting an API request to add an arbitrary email, and verifying the change. This can lead to unauthorized access to billing details, invoice notifications, or even escalation to owner-like privileges if the added email is controlled by the attacker. The vulnerability was reported via HackerOne and affects Slack's web API over HTTPS.

## Requirements

1. Valid team admin credentials for Slack workspace authentication
2. Access to an HTTP client (e.g., curl) for API requests
3. Team owner credentials for verification (optional but recommended)
4. Network connectivity to the Slack workspace domain

## Defense

Defensive measures and detection strategies:

- Implement strict role-based access control (RBAC) validation on all API endpoints, ensuring owner-only actions reject admin tokens
- Monitor API logs for unusual POST requests to billing endpoints from non-owner accounts
- Enable multi-factor authentication (MFA) for admin and owner roles
- Regularly audit billing contacts and API access patterns using Slack's audit logs

## Objectives

1. Escalate privileges from team admin to perform owner-restricted actions
2. Add unauthorized emails to expose billing data or enable further attacks
3. Demonstrate the vulnerability for reporting and remediation

## Instructions

### Step 1: Authenticate and Obtain Admin Token

**Context**: Log in as a team admin to retrieve a valid API token for subsequent requests.

**Instructions**: Use the Slack web interface or OAuth flow to authenticate and capture the token (format: xoxs-...).

### Step 2: Execute API Request to Add Contact

**Context**: Send the unauthorized POST request to add the billing contact using the admin token.

**Command** ([[commands/slack-add-billing-contact]]):
```bash
curl -X POST 'https://satishb3mailinator.slack.com/api/team.billing.addContact' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -d 'email=hacker@hacker.com&token=xoxs-3206092076-3204538285-3743137121-836b042620&set_active=true&_attempts=1'
```

> This command sends the POST request with the required parameters. Expected output is a JSON response like {"ok":true,"contact":{"email":"hacker@hacker.com"}}, indicating successful addition.

### Step 3: Verify the Addition

**Context**: Confirm the escalation by checking the billing contacts as the team owner.

**Instructions**: Log in as the team owner, navigate to Settings > Billing > Contacts, and verify the new email appears in the list.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/slack-add-billing-contact]]

## Tools Used


## Tags

- privilege-escalation
- slack
- api
- billing
