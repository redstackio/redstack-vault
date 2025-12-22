---
id: proc-set-malicious-username-nextcloud
tags:
  - xss
  - stored-xss
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.553Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Malicious-Username-in-Nextcloud

## Summary

This procedure involves updating the attacker's display name in Nextcloud to include a malicious XSS payload, which is stored without sanitization and later rendered in collaborative interfaces like Collabora Online.

## Description

In the context of Nextcloud integrated with Collabora Online, user display names are not properly escaped for HTML and JavaScript when shown in collaborative editing sessions. By setting the display name to a payload such as '<img src=a onerror=alert(window.parent.location)>', the attacker stores malicious code that executes in the victim's browser upon joining a shared document edit. This step requires an authenticated attacker account and targets the profile update functionality.

## Requirements

1. Authenticated access to a Nextcloud user account with profile editing permissions
2. Web browser to access the Nextcloud interface
3. Knowledge of a basic XSS payload suitable for the target context

## Defense

Defensive measures and detection strategies:

- Implement server-side HTML/JS escaping for all user-generated content, including display names
- Enable Content Security Policy (CSP) to restrict inline script execution in the collaborative interface
- Monitor for unusual profile updates or JavaScript errors in browser consoles during editing sessions

## Objectives

1. Persist a stored XSS payload in the user's display name
2. Set up the payload for delivery in collaborative contexts
3. Achieve execution without direct interaction beyond profile update

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in to Nextcloud and navigate to the user profile to prepare for username modification.

Log in to your Nextcloud account via the web interface and click on your avatar or user menu to access settings.

> Expected: Profile page loads with current display name visible.

### Step 2: Update Display Name with Payload

**Context**: Enter the malicious payload into the display name field to store the XSS vector.

In the profile settings, locate the "Display name" field and set it to: '<img src=a onerror=alert(window.parent.location)>'.

Save the changes.

> Expected: Confirmation message that the profile has been updated; no errors indicating sanitization.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored by viewing the profile or account details.

Refresh the profile page or view the account in another session to ensure the payload is displayed as entered.

> Expected: Payload appears in the display name without being escaped (e.g., tags visible in HTML source).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[nextcloud]]
