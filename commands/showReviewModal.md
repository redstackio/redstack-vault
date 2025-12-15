---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
data: showReviewModal();
tags:
  - xss-escalation
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:06.247Z'
verified: false
validated: true
submitted: true
---
# showReviewModal

## Command

```javascript
showReviewModal();
```

## Description

This JavaScript function, executed in the browser console of the support portal, triggers the display of a review modal to prompt user rating, which escalates self-XSS by forcing agent review of injected content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; function call only | Yes |

## Examples

### Basic Usage

```javascript
showReviewModal();
```

### Advanced Usage

Not applicable; direct call.

## Expected Output

The review modal UI opens, allowing rating submission (e.g., 1-star) that notifies the support agent to review chat logs, executing any injected XSS payloads.

## Related

- [[procedures/Exfiltrate-Internal-URL-via-Agent-Review]]
