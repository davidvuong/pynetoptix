# pynetoptix

**Welcome to pynetoptix!**

This is an unofficial, zero-dependency, Python 3 wrapper over the NetworkOptix' HTTP API. You can view their API documentation [here](http://www.networkoptix.com/sdk-api/).

## Installation & usage

```bash
pip install pynetoptix
```

```python
import pynetoptix

nx_username = 'demo'
nx_password = 'nxwitness'

nx_client = pynetoptix.create_client(nx_username, nx_password)
print(nx_client.system.get_cameras_ex())
```

## Development

```bash
# Clone the repository from GitHub
git clone git@github.com:davidvuong/pynetoptix.git

# Create a Python virtual environment (using Python 3)
mkvirtualenv pynetoptix -p python3

# Install development dependencies
pip install -r requirements.txt

# Run unit tests
python -m pytest tests/
```

## Deployment

PyPi deployments are manual for now. I'll need to configure CI to auto deploy on git branches. However until then, the process is as follows:

1. Bump the version number `pynetoptix.__version__`

    ```python
    __version_info__ = (0, 0, 1)
    __version__ = '.'.join([str(i) for i in __version_info__])
    ```

1. Commit, tag, and push your version bump:

    ```bash
    git add .
    git commit -m "chore(pkg): bump 0.0.1"
    git tag -a "v0.0.1" -m "chore(pkg): bump 0.0.1"
    git push && git push --tags
    ```

1. Build a new distribution and upload to PyPi:

    ```bash
    pip install twine
    python setup.py sdist
    twine upload dist/pynetoptix-0.0.1.tar.gz
    ```

**NOTE:** You might get warnings around having a misconfigured `~/.pypirc` file. Create one if you haven't and make sure it contains:

```
[pypi]
username = <username>
password = <password>
```

Ask another developer for the `username` and `password`.
