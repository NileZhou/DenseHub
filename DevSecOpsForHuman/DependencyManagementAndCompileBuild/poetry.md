# poetry

specific version:

poetry env use /usr/local/bin/python3.12


## use mirror

temporary:
```shell
POETRY_HTTP_BASIC_PYPI__URL=https://pypi.tuna.tsinghua.edu.cn/simple poetry install
```

global:
```shell
poetry config repositories.pypi-url https://pypi.tuna.tsinghua.edu.cn/simple
```

specific for current project.

update the pyproject.toml:
```toml
[[tool.poetry.source]]
name = "pypi"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = true
```
then poetry install
