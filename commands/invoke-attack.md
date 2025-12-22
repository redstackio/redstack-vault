---
id: 123e4567-e89b-12d3-a456-426614174008
name: invoke-attack
type: command
executor: javascript
data: attack();
output: 'Execution of the attack logic, potentially triggering the alert.'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.685Z'
platforms:
  - Web
tags:
  - xss
  - trigger
verified: false
validated: true
submitted: true
---

# invoke-attack

## Command

```javascript
attack();
```

## Description

Calls the predefined attack function to initiate the XSS sequence, including window opening, payload sending, and execution.

## Parameters

None.

## Examples

### Basic Usage

```javascript
attack();
```

### Advanced Usage

```javascript
// In HTML: <a href="javascript:attack()">Trigger</a>
```

## Expected Output

Starts the exploit: window opens, messages sent, alert on success.

## Related

- [[Related Procedure|procedures/Trigger-XSS-by-Visiting-and-Clicking-Link]]
