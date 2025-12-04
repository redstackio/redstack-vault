---
id: <% tp.system.uuid() %>
name: <% tp.file.title %>
type: tag
usage_count: 0
created_at: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>Z
updated_at: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>Z
---

# <% tp.file.title %>

## Description

Brief description of what this tag represents and when it should be applied to content.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tags, this.file.link)
SORT name ASC
LIMIT 20
```

## Related Techniques

```dataview
TABLE name as "Technique", mitre_id as "MITRE ID"
FROM "techniques"
WHERE contains(tags, this.file.link)
SORT name ASC
LIMIT 10
```

## Usage Guidelines

When to apply this tag:

- Criterion 1
- Criterion 2

## Related Tags

- [[Related Tag 1]]
- [[Related Tag 2]]
