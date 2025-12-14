---
tags:
  - csrf
  - timing
  - web
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:12.425Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 250b665c-75d5-4e53-a5cc-966a1216a9b2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Wait-for-Secret-Answer-Propagation

## Summary

This procedure introduces a delay in the CSRF attack chain to ensure backend propagation of the updated secret answer before attempting the password change, avoiding failures due to replication lag.

## Description

In distributed systems like Okta-integrated apps, updates may not be immediately visible across services. This step uses client-side JavaScript timing to pause execution, tested empirically to match server latency (typically 1-5 seconds). It is embedded in the same HTML PoC as the prior and subsequent steps for seamless chaining.

## Requirements

1. JavaScript-enabled browser (standard)
2. Empirical testing of delay duration via manual requests
3. Integration into the multistage HTML PoC

## Defense

Defensive measures and detection strategies:

- Implement idempotent updates with immediate consistency guarantees
- Rate-limit rapid successive requests from the same session
- Log and alert on chained state changes within short time windows

## Objectives

1. Ensure reliability of chained exploits
2. Prevent timing-based failures in account takeover
3. Maintain attack flow without manual intervention

## Instructions

### Step 1: Add Timeout to HTML Script

**Context**: Insert a setTimeout after the first form submission to delay the second.

Edit the HTML file:

```html
<script>
document.getElementById('csrf1').submit();
setTimeout(function() {
  document.getElementById('csrf2').submit();
}, 3000); // Adjust based on testing, e.g., 3 seconds
</script>
```

> This pauses execution, allowing server sync; test by observing if password change fails without delay.

### Step 2: Validate Delay

**Context**: Test the full PoC to confirm propagation.

Load the HTML in a test browser session, monitor network tab for timings, and verify second request succeeds.

> Expected: No errors in second response; successful password update.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- timing
- propagation
