---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csrf
  - flash
  - exploit
  - web
type: procedure
tools:
  - '[[tools/Flash-SWF]]'
  - '[[tools/PHP-Redirector]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.250Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Flash-CSRF-Attack

## Summary

This procedure exploits a CSRF vulnerability using a malicious Flash SWF file to send a POST request via a PHP redirector, updating the ad frequency setting on cp-ng.pinion.gg without proper protection.

## Description

The attack targets the POST endpoint at https://cp-ng.pinion.gg/api-v2/communities/edit/{user_id}, which lacks CSRF tokens. Flash's ability to perform cross-origin POSTs with custom headers (e.g., Content-Type: application/json) bypasses browser same-origin policy. The SWF sends a JSON payload {"frequency":60} to a attacker-controlled PHP script that issues a 307 redirect, preserving the method and body to forward to the target API. This allows site-wide modification of logged-in users' settings, impacting user experience and potentially enabling further unauthorized updates.

## Requirements

1. Authenticated session in the target application (from prior login)
2. Access to host or load the malicious SWF and PHP redirector
3. Browser supporting Flash (legacy, but required for this exploit)
4. Knowledge of the target user's ID for the endpoint

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing POST endpoints
- Disable or block Flash content in browsers and proxies
- Monitor for unexpected redirects (307) and cross-origin requests in logs
- Use same-site cookie attributes to restrict cross-origin usage

## Objectives

1. Bypass CSRF protections to perform unauthorized POST
2. Update ad frequency to a malicious value (e.g., 60%)
3. Demonstrate vulnerability for broader unprotected endpoints

## Instructions

### Step 1: Prepare Malicious Resources

**Context**: Ensure the SWF and PHP redirector are accessible, with the SWF configured to target the PHP endpoint.

Host the SWF at http://geekboy.ninja/poc/freq.swf, containing ActionScript to POST {"frequency":60} with Content-Type: application/json to http://geekboy.ninja/poc/test30.php. The PHP should redirect with: header('Location: https://cp-ng.pinion.gg/api-v2/communities/edit/{user_id}', true, 307);

> Expected output: Resources loaded without errors, verifiable via direct access.

### Step 2: Load SWF in Authenticated Session

**Context**: Trigger the exploit by visiting the SWF while logged in.

In the browser with an active session, navigate to http://geekboy.ninja/poc/freq.swf.

> The SWF executes automatically, sending the request through the redirector to the target. Expected output: Silent execution; ad frequency updated upon verification.

### Step 3: Verify Impact

**Context**: Confirm the unauthorized change.

Check the user's ad settings in the application or monitor ad display frequency.

> Expected output: Ad frequency set to 60%, confirming successful modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Flash-SWF]]
- [[tools/PHP-Redirector]]

## Tags

- [[csrf]]
- [[flash]]
- [[exploit]]
