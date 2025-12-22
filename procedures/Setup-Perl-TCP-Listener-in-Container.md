---
tags:
  - listener
  - perl
  - tcp
type: procedure
tools:
  - '[[tools/Perl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/perl-tcp-listener-port80]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:08:55.254Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: dbdac351-630a-430c-aa7e-aaaac09a2550
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Setup Perl TCP Listener in Container

## Summary

Deploy a simple TCP listener using Perl inside the Bitwarden icons Docker container to capture and log SSRF requests to localhost:80.

## Description

The listener confirms the SSRF by receiving the redirected HTTP GET request, which bypasses checks and hits internal port 80. Uses IO::Socket::INET for basic socket handling.

## Requirements

1. Perl installed in container (default in many images)
2. Exec access to Docker container
3. Port 80 free internally

## Defense

Defensive measures and detection strategies:

- Block unauthorized listeners in containers
- Use network policies to restrict internal port access
- Monitor for unexpected TCP binds on port 80

## Objectives

1. Intercept internal requests for verification
2. Log request details including path and headers
3. Prove SSRF success without full RCE

## Instructions

### Step 1: Access Container

**Context**: Enter the icons service container.

```bash
docker exec -it bitwarden_icons_1 /bin/bash
```

> Expected: Shell inside container.

### Step 2: Run Listener

**Context**: Bind to port 80 and echo incoming data.

Execute [[commands/perl-tcp-listener-port80]]:

```bash
perl -MIO::Socket::INET -ne 'BEGIN{$l=IO::Socket::INET->new( LocalPort=>80,Proto=>"tcp",Listen=>5,ReuseAddr=>1); my $l=$l->accept(); while(<$l>){ print $_; }; close($l);}'
```

> Expected: "Listening on port 80" or similar; waits for connections.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Discovery

### Sub-Techniques


## Commands Used

- [[commands/perl-tcp-listener-port80]]

## Tools Used

- [[tools/Perl]]

## Tags

- listener
- perl
- tcp
