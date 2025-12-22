---
id: proc-weblate-data-exfiltration
tags:
  - information-disclosure
  - exfiltration
  - tracking
type: procedure
tools:
  - '[[tools/Request-Tracker]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:25:12.631Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Capture-Exfiltrated-Admin-Data-via-Image-Requests

## Summary

This procedure sets up monitoring on an attacker-controlled server to capture HTTP requests triggered by the injected img tag when Weblate admins view the poisoned support ticket, disclosing internal IP addresses and User-Agent details.

## Description

Once the HTML payload executes in the RT support panel or email notifications (if the client loads external images), the browser fetches the img src from the attacker's server. This request includes the viewer's real IP (potentially internal, e.g., 10.x.x.x or VPN IPs like 137.9.65.65) and User-Agent (e.g., mobile or desktop browsers used by staff). The attack relies on RT's rendering of unsanitized content and targets admin workflows. Outcomes include logs of sensitive network reconnaissance data for further targeting.

## Requirements

1. A publicly accessible server with logging capabilities (e.g., Nginx or simple Python HTTP server)
2. The injected payload from the prior procedure active in a ticket
3. Patience for admin response time (hours to days)

## Defense

Defensive measures and detection strategies:

- Configure RT to strip or escape HTML in ticket views and emails
- Use email clients with external content blocking (e.g., Outlook's image download toggle)
- Monitor outbound traffic from internal networks for unexpected image fetches to unknown domains
- Log and alert on anomalous support ticket content

## Objectives

1. Receive and log exfiltration requests from admin views
2. Extract IPs and User-Agents for reconnaissance
3. Identify potential internal network details for escalation

## Instructions

### Step 1: Set Up Tracking Endpoint

**Context**: Deploy a server to host the fake image and log requests.

Use a tool like Nginx or Python's http.server. Configure to log full request headers and source IP for /track.gif.

Example Nginx config snippet:
```nginx
server {
    listen 80;
    server_name your-server.com;
    location /track.gif {
        access_log /var/log/nginx/track.log combined;
        return 200 "";  # Empty response to mimic image
    }
}
```

> Restart server; endpoint now logs all hits.

### Step 2: Monitor for Requests

**Context**: Wait for admins to access the ticket, triggering the img load.

Tail the access log: `tail -f /var/log/nginx/track.log`.

> Requests appear as GET /track.gif with headers including User-Agent and remote IP.

### Step 3: Analyze Captured Data

**Context**: Parse logs for sensitive info.

Review logs for entries like: `137.9.65.65 - - [date] "GET /track.gif HTTP/1.1" 200 ... "User-Agent: Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X)"`.

> Extract IPs (internal/external) and UAs to map admin environment.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Request-Tracker]]

## Tags

- [[information-disclosure]]
- [[Exfiltration]]
