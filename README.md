# The REAL Ghostbuster

The REAL Ghostbuster is a Python application designed to locate the code that is in use for Puppet Enterprise.

It was developed due to Ruby, Gem, and API issues related to the original Ghostbuster application. Those may have since been resolved since the original application release.

## Features

- Retrieves a list of groups with classes in the UI classifer, nodes, and classes
- Recursively goes through the nodes to retrieve the classes applied
- Creates a list of classes for the UI groups, all system classes, used classes, and unused classes
- Simple command-line interface
- Uses a model, view, controller design for easy modifications
- Single threaded to ensure it doesn't cause issues with Puppet Enterprise

## Limitations

- Output is written to the directory where the application exists
- Output is long, lacks pretty formatting, and is a CSV
- Output is meant to be interpreted by a third-party tool (vim, Microsoft Excel, Google Sheets, etc.)

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

This project is licensed under the MIT license.

## Contributes and Derivatives

Derivatives (copying the API models or controllers) are welcome; please attempt to reference this project in your project or application in those scenarios.

Pull requests are encouraged! Please open issues for suggestions or bugs.

## Author

Paul Riley