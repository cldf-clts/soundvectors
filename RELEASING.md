
# Releasing soundvectors

- Make sure to initiate and update the submodule in tests:
  ```shell
  git submodule init
  git submodule update
  ```

- Do platform test via tox:
  ```shell
  tox -r
  ```

- Run all CLTS sound tests:
  ```shell
  pytest --all
  ```

- Make sure flake8 passes:
  ```shell
  flake8 src
  ```

- Update the version number, by removing the trailing `.dev0` in:
  - `setup.cfg`
  - `src/soundvectors.py`

- Create the release commit:
  ```shell
  git commit -a -m "release <VERSION>"
  ```

- Create a release tag:
  ```
  git tag -a v<VERSION> -m"<VERSION> release"
  ```

- Release to PyPI:
  ```shell
  rm dist/*
  python -m build -n
  twine upload dist/*
  ```

- Push to github:
  ```shell
  git push origin
  git push --tags
  ```

- Change version for the next release cycle, i.e. incrementing and adding .dev0

  - `setup.py`
  - `src/soundvectors.py`

- Commit/push the version change:
  ```shell
  git commit -a -m "bump version for development"
  git push origin
  ```
