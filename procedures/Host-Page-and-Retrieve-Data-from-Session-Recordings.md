---
id: proc-host-and-retrieve
tags:
  - phishing
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Inspectlet]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Automated Collection]]'
updated_at: '2025-12-14T17:28:12.366Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Automated Collection]]'
---
# Host-Page-and-Retrieve-Data-from-Session-Recordings

## Summary

This procedure hosts the clickjacking page, lures victims via social engineering, and retrieves their IP/geolocation from Inspectlet session replays.

## Description

After integration, upload the HTML to a public host (e.g., GitHub Pages, free web host). Trick users into visiting via email/phishing. Inspectlet captures everything; attacker logs in to view recordings, replays sessions, and inspects network tabs for GeoAPI JSON. Impact: Full location disclosure for any visitor. Requires hosting access and Inspectlet login.

## Requirements

1. Web hosting service
2. Inspectlet dashboard access
3. Method to distribute URL (e.g., email)

## Defense

Defensive measures and detection strategies:

- Train users on phishing detection
- Block inspectlet.com domains in firewalls
- Monitor for geolocation API abuse logs

## Objectives

1. Attract victims to trigger data fetch
2. Capture sessions remotely
3. Extract and compile geo data

## Instructions

### Step 1: Upload to Host

**Context**: Deploy the HTML publicly.

Use any file host; obtain URL like https://attacker-site.com/Clickjacking.html.

### Step 2: Lure Victim

**Context**: Direct victim to the page.

Send link via email/social media, e.g., "Check this interesting page."

> Victim loads page, iframe fetches geo, Inspectlet records.

### Step 3: Access Recordings

**Context**: Replay to extract data.

Log into Inspectlet, go to Session Recordings tab, select recent session, replay, and check network for geo JSON.

**Expected Output**: IP and location details per victim session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[Automated Collection]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Inspectlet]]

## Tags

- [[Phishing]]
- [[data-exfiltration]]
