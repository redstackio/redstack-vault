---
title: <% tp.file.title %>
type: platform
platform: <% tp.file.title %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %> Platform

Overview of attack techniques, procedures, and tools specific to the <% tp.file.title %> platform.

## Overview

A comprehensive description of this platform from a security perspective, including common attack surfaces, default configurations, and security considerations.

## By MITRE Tactic

### Initial Access

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(platforms, this.platform) AND contains(tactics, [[Initial Access]])
SORT name ASC
LIMIT 10
```

### Execution

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(platforms, this.platform) AND contains(tactics, [[Execution]])
SORT name ASC
LIMIT 10
```

### Persistence

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(platforms, this.platform) AND contains(tactics, [[Persistence]])
SORT name ASC
LIMIT 10
```

### Privilege Escalation

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(platforms, this.platform) AND contains(tactics, [[Privilege Escalation]])
SORT name ASC
LIMIT 10
```

## Key Tools

```dataview
TABLE name as "Tool", verified as "Verified"
FROM "tools"
WHERE contains(platforms, this.platform)
SORT name ASC
LIMIT 20
```

## Common Attack Paths

1. **Path 1**: Initial Access → Execution → Privilege Escalation → Objective
2. **Path 2**: Initial Access → Persistence → Lateral Movement → Objective

## Platform-Specific Considerations

### Security Features

- Security feature 1
- Security feature 2

### Common Misconfigurations

- Misconfiguration 1
- Misconfiguration 2

## Related Resources

### Internal Links

- [[Related Platform]]
- [[Related Cheatsheet]]

### External Resources

- Resource 1
- Resource 2

---

*Last updated: <% tp.date.now("YYYY-MM-DD") %>*
