# Todo List
Todo List Simple API With python 3.x

## Boilerplate skeleton with pena rest engine
[pena-rest-engine](https://github.com/penaagp-dev/pena-rest-engine)

## Getting Started
### Environtment Setup
```
mv env.example .env
```

### Virtualenv
```
virtualenv -p python3 env
```

### Install And Running Service
#### Developer Mode
auto reload is active
```
pip install -e .
```

#### Production Mode
```
pip install .
```

### Running
```
pena http serve
```

help
```
# pena -h
---------------------------------------------------------------------------------------------------
Usage:
  pena <command> [<args>...]

Options:
  -h, --help                             Display this help and exit
  -v, --version                          Print version information and quit

Commands:
  http                                 Starting http serve
  migrate                              Migrating apps
  deploy                                Setup apps

Run 'pena COMMAND --help' for more information on a command.
```



