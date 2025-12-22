---
id: proc-khan-url-construct-6564
name: Construct Malicious Redirect URL in SWF Player
tags:
  - open-redirect
  - url-construction
  - flash
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:26.364Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Construct Malicious Redirect URL in SWF Player

## Summary

This procedure involves crafting a URL for the SmartHistory Khan Academy Flash media player (SWF) that exploits the unvalidated 'link' parameter to specify an arbitrary external redirect target, setting up the foundation for phishing attacks.

## Description

The SmartHistory Khan Academy media player at http://smarthistory.khanacademy.org/assets/images/media/player.swf accepts parameters like displayclick=link&link=[URL]&file=[image]. Due to lack of validation, the 'link' parameter can be set to any external domain, such as a malicious phishing site. When embedded in a webpage or shared as a link, this allows attackers to redirect users upon interaction. The target environment is any web browser supporting Flash (legacy). Prerequisites include basic URL construction knowledge and access to a malicious domain. Expected outcomes: A functional SWF URL that loads the player with the custom redirect configured.

## Requirements

1. Web browser with Flash support (or emulator for testing)
2. Control over a malicious external domain for the redirect target
3. No authentication or special network access needed

## Defense

Defensive measures and detection strategies:

- Implement URL validation in Flash parameters to whitelist domains
- Use Content Security Policy (CSP) to restrict redirects
- Monitor for anomalous outbound redirects from embedded media
- Deprecate Flash usage in favor of modern HTML5 players with strict sanitization

## Objectives

1. Create a redirect-capable SWF URL targeting a malicious site
2. Verify the parameter acceptance without errors
3. Prepare for user interaction to trigger the exploit

## Instructions

### Step 1: Prepare the Base URL and Parameters

**Context**: Start with the known vulnerable endpoint and append the required parameters to configure the redirect behavior.

No command required; manually construct:

The base URL is `http://smarthistory.khanacademy.org/assets/images/media/player.swf`. Add `?displayclick=link&link=http://evil.com/phish&file=1.jpg` (replace http://evil.com/phish with your malicious URL).

> This sets the player to redirect on click to the specified link. Test by loading the full URL in a browser; the SWF should embed without errors, and inspecting network requests confirms the parameter.

### Step 2: Encode and Validate the URL

**Context**: Ensure the URL is properly formatted and test loading to confirm the 'link' parameter is accepted.

No command; use browser developer tools:

Load the constructed URL directly. If Flash is enabled, the player loads an image (1.jpg) with click-to-link functionality pointing to your external site.

> Expected: Player displays without validation errors. Success if clicking (in Step 2 of chain) redirects correctly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Phishing: Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[flash]]
