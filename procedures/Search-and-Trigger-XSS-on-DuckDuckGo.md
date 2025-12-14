---
tags:
  - xss
  - search-engine
  - duckduckgo
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
updated_at: '2025-12-13T23:52:55.428Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: cf39b79d-32c6-4e84-836c-74443c3a2e9a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Search-and-Trigger-XSS-on-DuckDuckGo

## Summary

This procedure triggers the stored XSS by searching for the tainted video on DuckDuckGo, causing the platform to fetch and reflect the unsanitized Rutube user tag in the video detail page.

## Description

The attacker uses DuckDuckGo's video search to query the Rutube video URL, encoding the payload if needed. DuckDuckGo embeds the external metadata, including the malicious tag, into the `c-detail__user` class without proper escaping, leading to execution. Target environment is DuckDuckGo's web interface. Prerequisites: The malicious tag must already be injected on Rutube. Outcomes include the payload being rendered and potentially executed on the detail page.

## Requirements

1. Web browser with JavaScript enabled
2. Access to DuckDuckGo.com
3. URL of the tainted Rutube video

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in all fetched external content
- Use sandboxed iframes for third-party embeds
- Log and scan for XSS payloads in search queries and results

## Objectives

1. Fetch tainted video metadata
2. Reflect payload in search results
3. Load detail page to trigger execution

## Instructions

### Step 1: Construct Search Query

**Context**: Build a search URL that includes the Rutube video to pull in the metadata.

Use the format: https://duckduckgo.com/?q=VIDEO_QUERY&t=hk&iar=videos&iax=videos&ia=videos&iai=https://rutube.ru/video/83a4775f020b3fd68efd3dc9a73031e8/. Encode the payload if directly in query: %22%2F%3E%22%2F%3E%3Cimg+src%3Dxss+onerror%3Dalert(2)%3E.

### Step 2: Perform Search and Navigate to Details

**Context**: Execute the search and click into the video detail to render the vulnerable element.

Enter the query in DuckDuckGo's video search tab and select the result. The detail page should load the `c-detail__user` div with the reflected tag.

> Reflection occurs due to lack of sanitization in fetched Rutube data.

### Step 3: Inspect Rendered Page

**Context**: Verify the payload is present in the DOM before execution.

Use browser dev tools (F12) to inspect the `c-detail__user` class and confirm the img tag is injected.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- reflection
- web-search
