# The REAL Ghostbuster

The REAL Ghostbuster is a Python application designed to locate the code that is in use for Puppet Enterprise.

It was developed due to Ruby, Gem, and API issues related to the original Ghostbuster application. Those may have since been resolved.

## Features

- Retrieves a list of groups with classes in the UI classifer, nodes, and classes
- Recursively goes through the nodes to retrieve the classes applied
- Removes the 
- Simple command-line interface
- Uses a model, view, controller design for easy modifications
- Single threaded to ensure it doesn't cause issues with Puppet Enterprise

## Installation

Clone the repository and ensure you have Python 3.6+ installed.

```bash
git clone https://github.com/paul-riley/therealghostbuster.git
cd therealghostbuster
```

## Usage

Run the application from the command line:


```bash
./classfinder.py
```

or

```bash
python3 classfinder.py
```

## Output

The application prints a list of found group classes, known classes, used classes, and unused classes associated with the features above.

## License

This project is licensed under the GPLv2 license.

## Contributing

Pull requests are welcome! Please open issues for suggestions or bugs.

## Author

Paul Riley