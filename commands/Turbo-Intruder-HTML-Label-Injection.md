---
id: cmd-turbo-intruder-label
data: |-
  def handleResponse(req, interesting):
      req.label = '<html><img src="http://responder-ip"/></img>'
      table.add(req)
tags:
  - extension-test
  - mitigation-check
type: command
output: No unsolicited request due to mitigation; label updated without fetching.
executor: python
platforms:
  - Desktop
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.366Z'
verified: false
validated: true
submitted: true
---
# Turbo-Intruder-HTML-Label-Injection

## Command

```python
def handleResponse(req, interesting):
    req.label = '<html><img src="http://responder-ip"/></img>'
    table.add(req)
```

## Description

Python snippet for Burp's Turbo Intruder extension to inject HTML into request labels, testing if post-2021.2 mitigations prevent fetches during rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| req.label | HTML payload assigned to request label | Yes |
| responder-ip | Attacker IP for potential fetch | Yes |

## Examples

### Basic Usage

Paste into Turbo Intruder script; run against requests.

### Advanced Usage

Modify for different tags: req.label = '<link href="http://test">'

## Expected Output

Label updates in Burp without triggering img fetch, confirming mitigation.

## Related

- [[procedures/Trigger-HTML-Rendering-in-Burp-Suite]]
- [[tools/Burp-Suite]]
