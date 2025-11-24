# Project

## Install

Installing is easy with [pixi](https://pixi.sh/latest/). Once installed use the following commands:

```sh
pixi install
pixi global install pre-commit
pre-commit install
```

You can get the `python.exe` file by:
```sh
pixi r which python
```


## Testing

pytests will run with pre-commit, to run manually use:
```sh
pixi run tests
```

## Enabling packages to be externally referenced

If you need to be able to use your packages as dependencies from another
project, you must add `project.dependencies` to each package. For this example
monorepo, you would add to both `packages/pixi_py/pyproject.toml` and
`packages/pixi_py_copy/pyproject.toml`:

```toml
[project]
...
dependencies = ["rich"]
```

Then you can reference your packages from outside of this repo as:

```toml
pixi_py = { git = "…", subdirectory = "packages/pixi_py", branch = "main" }
pixi_py_copy = { git = "…", subdirectory = "packages/pixi_py_copy", branch = "main" }
```

The downside of this strategy is the duplication of the dependency list; now
your package `pyproject.toml`s can get out of sync with the top-level config.
