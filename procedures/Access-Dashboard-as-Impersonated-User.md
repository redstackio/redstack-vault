---
tags:
  - auth-bypass
  - openid
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e62a68bb-0a61-4cd0-9558-ecc41df363c3
created_at: '2025-12-14T17:31:42.517Z'
updated_at: '2025-12-14T17:31:42.517Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Dashboard-as-Impersonated-User

## Summary

This procedure confirms successful impersonation by accessing the Airflow dashboard and performing actions as the targeted user, demonstrating full account hijacking.

## Description

Post-authentication, the forged session grants access to the Airflow interface. The attacker can now manage DAGs, view logs, or escalate further if the user has admin privileges. This exploits the trust in the OpenID response, leading to complete compromise. Validation involves checking user context in the UI.

## Requirements

1. Successful forged authentication from prior step
2. Browser session maintained
3. Target user with known permissions

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication (MFA) beyond OpenID
- Monitor session creation logs for anomalous user-IDP pairings
- Regular audits of user sessions and logout on suspicious activity

## Objectives

1. Verify session as impersonated user
2. Access sensitive Airflow features
3. Demonstrate privilege hijacking

## Instructions

### Step 1: Follow Redirect to Dashboard

**Context**: Complete the login flow to reach the protected area.

After the backend accepts the response, the browser redirects to /home/ or the dashboard. Allow the redirect to complete.

> The URL should change to the Airflow homepage without re-prompting for login.

### Step 2: Verify User Identity

**Context**: Confirm impersonation in the UI.

Check the user profile or top-right menu for the impersonated username. Attempt a simple action like viewing the DAG list.

> Expected: UI shows the target user's name and grants access to their resources.

### Step 3: Perform Privileged Actions

**Context**: Test the extent of access gained.

Navigate to areas like /admin/ or execute a DAG if permissions allow. Document any sensitive data accessed.

> Success: Full functionality as the user, e.g., editing workflows or viewing secrets.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[openid]]
- [[privilege-escalation]]
