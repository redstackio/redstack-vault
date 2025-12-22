---
id: proc-execute-csrf-poc-95555
tags:
  - csrf
  - poc
  - twitter
  - poll
  - vote
type: procedure
tools:
  - '[[tools/Twitter-Cards-CSRF-POC]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:28.994Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute CSRF PoC to Force Poll Vote

## Summary

This procedure uses a proof-of-concept webpage to craft and trigger a silent CSRF request to the bypassed Twitter cards API endpoint, forcing an authenticated victim's browser to submit an unauthorized poll vote.

## Description

The PoC tool generates an HTML form or JavaScript that auto-submits a POST to /i/cards/api/v1 with poll parameters, leveraging the victim's Twitter session cookies. When the victim visits the attacker's malicious page (e.g., via phishing link), the vote is recorded without interaction, demonstrating the full CSRF impact.

## Requirements

1. Valid poll details: tweet_id, card_uri, selected_choice
2. Hosted malicious webpage accessible to victim
3. Victim authenticated on Twitter in their browser

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF tokens on all API variants
- Educate users on phishing and suspicious links
- Monitor poll vote anomalies (e.g., rapid changes from single IPs)

## Objectives

1. Generate CSRF payload using PoC tool
2. Trick victim into loading the page to trigger request
3. Confirm unauthorized vote on the poll

## Instructions

### Step 1: Configure PoC Tool

**Context**: Input poll parameters into the web-based PoC to customize the attack.

No command; navigate to http://innerht.ml/pocs/twitter-cards-csrf/ and fill fields: tweet_id=657629231309041664, card_uri=card://657629230759415808, selected_choice=2.

### Step 2: Activate and Deliver Attack

**Context**: Trigger the silent request and deliver via link/email to victim.

Click the activate button in the PoC to test; in attack, host the generated HTML and send to victim.

> The browser submits the POST using victim's cookies, expecting vote success.

### Step 3: Validate Impact

**Context**: Check Twitter poll for the forced vote.

Inspect the tweet; vote count should reflect the selected_choice without victim input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Twitter-Cards-CSRF-POC]]

## Tags

- csrf
- poc
- force-vote
- twitter
