---
id: proc-uuid-67890
tags:
  - csrf
  - web
  - bypass
  - preview-box
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-csrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:36.150Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Trigger-CSRF-via-Preview-Box

## Summary

This procedure triggers the CSRF attack by directing an authenticated VK.com user to the malicious page, exploiting the preview box's insufficient hash checks to perform unauthorized actions like widget configuration changes.

## Description

Once the malicious page is crafted, this step focuses on delivery and execution. The attack relies on the victim's active session with VK.com; loading the page causes the browser to submit the forged request to the widget preview endpoint. Due to weak hash validation, the server processes it as legitimate. This is effective in scenarios where widgets are embedded or previewed in third-party contexts. Outcomes include session-based actions without direct authentication bypass.

## Requirements

1. Malicious HTML page from prior procedure
2. Social engineering vector (e.g., email link) to reach victim
3. Victim's browser must have VK.com cookies active

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookie attributes (Lax/Strict) to limit cross-site requests
- Log and alert on widget preview actions from non-VK referers
- Educate users on phishing and unexpected page loads

## Objectives

1. Execute the forged request using victim's session
2. Confirm unauthorized action via server response
3. Validate impact on victim's account

## Instructions

### Step 1: Deliver Malicious Link

**Context**: Use phishing or other lures to get the victim to visit the hosted malicious page while logged into VK.com.

No command; send URL via email or message.

> Ensure the link appears benign, e.g., disguised as a widget demo.

### Step 2: Verify Request Execution

**Context**: Test the trigger by loading the page in a controlled environment with VK session, using curl to simulate if needed.

**Command** ([[commands/curl-csrf-test]]):
```bash
curl -X POST https://vk.com/widget_preview \
  -H "Cookie: vk_session=valid_session_cookie" \
  -d "action=update_widget&widget_id=target&malicious_param=attacker_value"
```

> This simulates the form submission. Expected output: HTTP 200 with success message or updated widget state, indicating bypass of hash checks.

### Step 3: Monitor Impact

**Context**: Check VK.com account for changes post-trigger to confirm exploitation.

Access victim account dashboard.

> Look for altered widget settings or unauthorized actions as indicators of success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-test]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[bypass]]
