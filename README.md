# voice-checklist

This script is used to assist with Google Voice's numbers retention checks, 
to help with manual operations, 
and to prompt for basic information about the accounts to be viewed.

## Preparation

Enter the information about the accounts in the JSON file according to the following format:

```json
{
    "Login Device Name": {
        "Email": "Number"
    }
}
```

Example: See [example.json](. /example.json).

## Usage

Start checklist:

```
python main.py -f "JSON file path"
```

Search for information on a given email or number:

```
python main.py -f "JSON file path" -s "example1@gmail.com"
```
