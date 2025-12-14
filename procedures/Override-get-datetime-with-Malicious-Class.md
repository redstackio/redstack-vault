---
id: proc-uuid-003
tags:
  - python-override
  - xss-payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/define-malicious-get-datetime-class]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.609Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Override-get-datetime-with-Malicious-Class

## Summary

Define a Python class named get_datetime in the algorithm code to override the built-in function, returning an XSS payload from the strftime method when the watched expression is evaluated.

## Description

Quantopian's backend evaluates Python expressions from watched variables during debugging. By defining a class that shadows get_datetime(), the strftime call in the hardcoded expression can be hijacked to output arbitrary strings, such as an HTML img tag with onerror JS. This injects the payload into the unsanitized frontend display without altering the expression itself.

## Requirements

1. Access to edit algorithm code
2. Knowledge of the target expression string
3. Python syntax for class definition

## Defense

Defensive measures and detection strategies:

- Namespace isolation for built-in functions in evaluation sandbox
- Scan algorithm code for class overrides on builtins
- Whitelist allowed expression patterns

## Objectives

1. Hijack the datetime display mechanism
2. Inject persistent XSS payload
3. Enable execution on backtest trigger

## Instructions

### Step 1: Insert Class Definition

**Context**: Add the override to the algorithm body, preferably obfuscated.

Execute [[commands/define-malicious-get-datetime-class]] at the top of the code:

```python
class get_datetime():
    def __init__(self):
        self.img ='<img src=x'+' one'+'rror=alert(1)>'
    def strftime(self, x=None):
        return self.img
```

> This concatenates the payload to evade basic filters; expected output is the full img tag when strftime is called.

### Step 2: Verify Expression Compatibility

**Context**: Ensure the watched expression invokes the override.

Test locally by evaluating get_datetime().strftime("%Y-%m-%d %H:%M:%S") in a Python REPL.

**Expected Output**: Returns the XSS string instead of formatted time.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/define-malicious-get-datetime-class]]

## Tools Used


## Tags

- python-override
- xss-payload
