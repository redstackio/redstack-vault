---
tags:
  - reconnaissance
  - api-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-vimeo-oembed-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:01.480Z'
sub_techniques: []
id: 3afaa5ac-8d53-462b-9393-1eec1cc91d35
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Vimeo-Legacy-OEmbed-API-Endpoint

## Summary

This procedure identifies Vimeo's legacy oEmbed API endpoint, which accepts video URLs and returns embedding metadata in JSON format, setting the stage for privacy testing.

## Description

In the context of Vimeo's platform, the legacy API at /api/oembed.json is designed for embedding videos but fails to consistently enforce privacy controls. This step involves reviewing API documentation or testing common oEmbed patterns to confirm the endpoint's existence and parameters. No authentication is required, making it accessible for reconnaissance.

## Requirements

1. Internet access to Vimeo's domain
2. Basic knowledge of HTTP requests (e.g., via browser or curl)
3. Access to Vimeo video URLs for testing

## Defense

Defensive measures and detection strategies:

- Monitor API endpoint access logs for unusual query patterns
- Deprecate and redirect legacy endpoints to secure versions
- Implement rate limiting on API calls

## Objectives

1. Locate and validate the vulnerable API endpoint
2. Understand parameter handling for video URLs
3. Prepare for privacy enforcement testing

## Instructions

### Step 1: Review Vimeo API Documentation

**Context**: Search for oEmbed support in Vimeo's developer resources to identify the legacy endpoint.

**Command** ([[commands/curl-vimeo-oembed-test]]):
```bash
curl "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/12345"
```

> This tests a public video to confirm the endpoint returns JSON with type, title, and embed details.

### Step 2: Validate Parameter Acceptance

**Context**: Ensure the endpoint processes the 'url' parameter correctly.

**Command** ([[commands/curl-vimeo-oembed-test]]):
```bash
curl -v "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/[PUBLIC_VIDEO_ID]"
```

> Expected verbose output shows HTTP 200 with JSON response, confirming functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-vimeo-oembed-test]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[api-discovery]]
