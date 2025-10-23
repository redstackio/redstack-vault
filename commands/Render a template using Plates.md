---
id: ef82b492-fa77-4d42-a3a9-9ffbc14ce803
name: Render a template using Plates
type: command
executor: bash
data: '// Create new Plates instance

  $templates = new League\Plates\Engine(''/path/to/templates'');


  // Render a template

  echo $templates->render(''profile'', [''name'' => ''Jonathan'']);'
output: null
created_at: '2023-04-06T03:56:40.469114+00:00'
updated_at: '2023-04-10T20:23:37.836976+00:00'
---

# Render a template using Plates

```bash
// Create new Plates instance
$templates = new League\Plates\Engine('/path/to/templates');

// Render a template
echo $templates->render('profile', ['name' => 'Jonathan']);
```


