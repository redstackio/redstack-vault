---
id: proc-uuid-placeholder-1
tags:
  - prototype-pollution
  - gitlab
  - mermaid
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:49.514Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-GitLab-Issue-with-Mermaid-Payload

## Summary

This procedure demonstrates how to create a GitLab issue containing a Mermaid diagram with a prototype pollution payload, leading to client-side DoS by overwriting the Object prototype in the browser's JavaScript environment.

## Description

In GitLab, Mermaid diagrams are rendered client-side using the Mermaid library, which processes unsanitized JSON in init directives (%%{init: {JSON}}%%). By injecting '__proto__' as a key in this JSON, attackers can pollute the global Object prototype, causing exceptions on property access across the application. This breaks interactivity like commenting or editing on the issue page for any visitor. The procedure requires only standard user access to a repository and targets web-based GitLab instances.

## Requirements

1. Authenticated GitLab account with issue creation permissions in a target repository.
2. Web browser for accessing the GitLab UI.
3. No additional tools; uses GitLab's built-in Markdown editor.

## Defense

Defensive measures and detection strategies:

- Sanitize Mermaid init directives to block '__proto__', 'constructor', and similar keys.
- Implement Content Security Policy (CSP) to restrict inline script execution and external loads.
- Monitor for anomalous JavaScript errors in client logs, such as prototype access failures.
- Use server-side rendering or validation for user-generated diagrams.

## Objectives

1. Persist a prototype pollution payload in a stored GitLab issue.
2. Cause DoS by breaking client-side JavaScript functionality.
3. Set up for potential escalation to code execution.

## Instructions

### Step 1: Access Issue Creation

**Context**: Log in to GitLab and navigate to a repository to start a new issue, providing a vector for stored content.

No command execution; use the GitLab web interface to click "New Issue".

> This opens the Markdown editor where Mermaid code can be inserted.

### Step 2: Insert Pollution Payload

**Context**: Add the malicious Mermaid init directive to pollute the prototype upon rendering.

Insert the following in the issue description:

```markdown
%%{init: { '__proto__': {'polluted': 'asdf'}} }%% sequenceDiagram Alice->>Bob: Hi Bob Bob->>Alice: Hi Alice
```

> Preview the Markdown to ensure the diagram renders. The pollution occurs on full page load for viewers.

### Step 3: Submit and Verify

**Context**: Save the issue to trigger rendering for others.

Click "Create Issue" to submit.

> View the issue in an incognito window; check browser console for errors like "TypeError: Cannot read property 'polluted' of undefined" indicating successful pollution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[prototype-pollution]]
- [[gitlab]]
- [[dos]]
