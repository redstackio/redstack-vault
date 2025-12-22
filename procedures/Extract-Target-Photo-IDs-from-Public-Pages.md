---
id: proc-404797-extract-public-photo-ids
tags:
  - public-recon
  - photo-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/zomato-photo-viewer-data-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:34.454Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract Target Photo IDs from Public Pages

## Summary

This procedure gathers photo IDs from a target restaurant's public Zomato page via intercepted requests, enabling targeted IDOR attacks without authentication.

## Description

By visiting a restaurant's public profile and interacting with the 'All photos' section, a POST request to /php/photoviewerData.php is intercepted, leaking photo_id values (e.g., u_1MDU1NjE2NzE5M). These can be converted (u_ to r_) for deletion targeting. This reconnaissance step targets unauthenticated public endpoints in Zomato's web app, with outcomes including a list of exploitable IDs stored in S3.

## Requirements

1. Access to the target's public restaurant page
2. Proxy for intercepting POST requests
3. Basic understanding of request parameters like res_id and category

## Defense

Defensive measures and detection strategies:

- Obfuscate or avoid exposing internal IDs in public API responses
- Implement rate-limiting on photoviewerData.php to prevent bulk scraping
- Monitor for repeated requests to public photo endpoints from suspicious IPs

## Objectives

1. Collect photo_ids from competitor or target restaurants
2. Prepare IDs for IDOR insertion
3. Validate IDs for restaurant-specific prefix

## Instructions

### Step 1: Access Public Restaurant Page

**Context**: Locate and interact with the target's photo gallery.

Navigate to the target page (e.g., https://www.zomato.com/washington-dc/old-ebbitt-grill-downtown) and click 'All photos' to trigger data fetch.

**Expected Output**: Photo viewer loads; network shows POST to photoviewerData.php.

### Step 2: Intercept and Parse Response

**Context**: Capture the request and extract IDs from the JSON payload.

Intercept using [[commands/zomato-photo-viewer-data-request]]:

```http
POST /php/photoviewerData.php HTTP/1.1
Host: www.zomato.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.zomato.com/
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 384
Cookie: REDACTED
Connection: close
X-Forwarded-For: 127.0.0.1

photoviewersize=NORMAL&photo_id=u_1MDU1NjE2NzE5M&type=res&index=1&category=all&res_id=16872578&group_id=false&onPage=true&moreToFetch%5B%5D=0&moreToFetch%5B%5D=1&moreToFetch%5B%5D=2&moreToFetch%5B%5D=3&moreToFetch%5B%5D=4&moreToFetch%5B%5D=5&moreToFetch%5B%5D=6&moreToFetch%5B%5D=7&moreToFetch%5B%5D=8&moreToFetch%5B%5D=9&moreToFetch%5B%5D=10&moreToFetch%5B%5D=11&moreToFetch%5B%5D=12
```

> Parse JSON for photo_id fields; convert u_ to r_ for restaurant photos.

**Expected Output**: List of photo_ids (e.g., r_1MDU1NjE2NzE5M) ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Hardware]] Gather Victim Network Identity and Characteristics

## Commands Used

- [[commands/zomato-photo-viewer-data-request]]

## Tools Used


## Tags

- reconnaissance
- public-exposure
