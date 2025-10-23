---
id: ea3cb554-4b16-4a68-b973-9c38f4583708
name: Convert JSON to XML
type: command
executor: bash
data: 'const json = {name: ''John'', age: 30};

  const options = {compact: true, ignoreComment: true, spaces: 4};

  const xml = xmljs.js2xml(json, options);'
output: null
created_at: '2023-04-06T03:56:44.656701+00:00'
updated_at: '2023-04-10T20:24:43.080287+00:00'
---

# Convert JSON to XML

```bash
const json = {name: 'John', age: 30};
const options = {compact: true, ignoreComment: true, spaces: 4};
const xml = xmljs.js2xml(json, options);
```


