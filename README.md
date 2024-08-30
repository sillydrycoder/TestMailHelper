# TMClient

TMClient is a Python package for interacting with the Testmail API. It allows you to retrieve email lists and specific emails using the Testmail API.

## Features

- Retrieve a list of emails with detailed information.
- Fetch a specific email by its ID.

## Installation

You can install `tmclient` using pip. To install it locally from the source code, navigate to the root directory containing `setup.py` and run:

```bash
pip install .
```

Alternatively, if you want to install it from PyPI (once published), use:

```bash
pip install tmclient
```

## Usage

Here's a basic example of how to use the `TMClient` class:

```python
from tmclient import TMClient

def main():
    client = TMClient(
        api_key='your_api_key',
        namespace='your_namespace'
    )
    
    # Get list of emails
    emails = client.get_emails_list()
    print("Email List:")
    for email in emails:
        print(email)
    
    # Get a specific email by ID
    email_id = 'some_email_id'
    email = client.get_email_by_id(email_id)
    if email:
        print("Email Details:")
        print(email)
    else:
        print(f"No email found with ID: {email_id}")

if __name__ == "__main__":
    main()
```

## API Reference

### `TMClient`

#### `__init__(api_key, namespace)`

Initialize the TMClient with your API key and namespace.

- `api_key` (str): Your API key for the Testmail API.
- `namespace` (str): The namespace for the Testmail API.

#### `get_emails_list()`

Retrieve a list of emails from the Testmail API.

- Returns: A list of dictionaries, each representing an email with keys: `'from'`, `'subject'`, `'tag'`, `'timestamp'`, `'id'`.
- Raises: `requests.exceptions.HTTPError` if the request fails.

#### `get_email_by_id(email_id)`

Retrieve a specific email by its ID.

- `email_id` (str): The ID of the email to retrieve.
- Returns: A dictionary representing the email, or `None` if not found.
- Raises: `requests.exceptions.HTTPError` if the request fails.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [Muhammad Ali](mailto:muhammad_alil@workmail.com.com).