# Sample flask hierarchy with blueprint

blueprints are for saparating app into more parts, which have different tasks

if template is not in blueprints, it searches global templates

```
flaskblueprint-tutorial
├── /application
│   ├── __init__.py
│   ├── /admin
│   │   ├── __init__.py
│   │   ├── admin_routes.py
│   │   ├── assets.py
│   │   └── /templates
│   ├── /main
│   │   ├── __init__.py
│   │   ├── assets.py
│   │   ├── main_routes.py
│   │   └── /templates
│   ├── /static
│   └── /templates
│       ├── layout.html
│       ├── meta.html
│       ├── navigation-default.html
│       ├── navigation-loggedin.html
│       └── scripts.html
├── config.py
├── requirements.txt
├── start.sh
└── wsgi.py
```