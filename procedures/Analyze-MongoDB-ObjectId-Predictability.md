---
tags:
  - mongodb
  - id-analysis
  - predictability
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:47.715Z'
sub_techniques: []
id: 6b0b45cb-19ad-48c1-bf24-d96516bdc09e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-MongoDB-ObjectId-Predictability

## Summary

This procedure involves dissecting the structure of MongoDB ObjectIds to reveal their predictable components, enabling subsequent brute-force attacks in systems like Semrush's Social Media Ads service where IDs are used for direct object access.

## Description

MongoDB ObjectIds are 12-byte hexadecimal strings composed of a 4-byte timestamp (seconds since Unix epoch), a 5-byte random value (unique to the machine and process), and a 3-byte incrementing counter that starts randomly but increases sequentially for objects created in the same second. In vulnerable applications, this structure allows attackers to guess nearby IDs by estimating the timestamp from the application's launch date and iterating the counter. For Semrush, this predictability in the Social Media Ads service endpoint leads to IDOR exploitation. Prerequisites include access to a legitimate user ID via API inspection.

## Requirements

1. Authenticated session to the target service (e.g., Semrush account)
2. Access to API responses containing ObjectIds (via browser or proxy)
3. Basic knowledge of hexadecimal and Unix timestamps

## Defense

Defensive measures and detection strategies:

- Use UUIDv4 or cryptographically secure IDs instead of MongoDB ObjectIds for sensitive resources
- Implement proper access controls with authorization checks on ID-based endpoints
- Monitor for anomalous request patterns, such as high-volume ID enumerations from a single IP

## Objectives

1. Confirm the predictable nature of ObjectIds in the target system
2. Estimate feasible brute-force ranges based on timestamp and counter
3. Prepare for enumeration of unauthorized resources

## Instructions

### Step 1: Extract and Inspect Own User ID

**Context**: Obtain a sample ObjectId from the application's API to analyze its components.

Use browser developer tools to inspect network requests in the Social Media Ads interface. Look for endpoints returning user data with ObjectIds.

No specific command, but example API call observation:

```http
GET /social-ads/users/current
Response: {"_id": "507f1f77bcf86cd799439011", "token": "..."}
```

> Parse the ID: Convert first 8 hex chars to decimal for timestamp (e.g., 507f1f77 hex = 1354924695 decimal ≈ 2012-12-05), identify counter in last 6 chars.

### Step 2: Break Down ID Components

**Context**: Manually or programmatically dissect the ID to understand predictability.

Use a hex-to-decimal converter or Python snippet:

```python
id_hex = "507f1f77bcf86cd799439011"
timestamp_hex = id_hex[:8]
timestamp = int(timestamp_hex, 16)
print(f"Timestamp: {timestamp} ({timestamp} seconds since epoch)")
random_part = id_hex[8:13]
counter = id_hex[13:]
print(f"Random: {random_part}, Counter: {counter}")
```

> Expected output shows timestamp in a narrow range (e.g., service uptime), counter incrementing, allowing prediction of adjacent IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mongodb]]
- [[id-analysis]]
