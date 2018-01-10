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