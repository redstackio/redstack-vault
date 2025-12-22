---
data: 'view-source:https://www.lyst.com/LAVFKS53DG.css'
tags:
  - web
  - inspection
type: command
executor: bash
platforms:
  - Web
id: 765de503-0d9e-44ba-858a-d6098e161ecb
created_at: '2025-12-13T09:00:34.388Z'
updated_at: '2025-12-13T09:00:34.388Z'
verified: false
validated: true
submitted: true
---
# View Source of Cached URL

## Command

```bash
view-source:https://www.lyst.com/LAVFKS53DG.css
```

## Description

This command is used by the attacker to inspect the source code of the cached URL after poisoning, revealing sensitive user information such as username, slug, id, and email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The crafted .css URL containing cached data | Yes |

## Examples

### Basic Usage

```bash
view-source:https://www.lyst.com/LAVFKS53DG.css
```

### Advanced Usage

Use in a browser's address bar to view source directly.

## Expected Output

Page source containing username, slug, id, email, etc.

## Related

- [[procedures/Access-Cached-Content-as-Unauthenticated-User]]
