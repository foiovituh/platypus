# 🦆 Platypus
![GitHub License](https://img.shields.io/github/license/foiovituh/platypus)
![GitHub Release](https://img.shields.io/github/v/release/foiovituh/platypus)

> A personal command-line tool for security enumeration.

![Image](https://github.com/user-attachments/assets/eeae4a7b-4eae-4576-b80d-04b8cdb96396)

## 📦 Installation

### From GitHub

Clone the repository and install Platypus:

```bash
git clone https://github.com/foiovituh/platypus.git
cd platypus

python3 -m pip install .
```

### Development environment

Create a virtual environment and install development dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install -e ".[dev]"
```

## 🚀 Usage

### Help

```bash
platypus --help
```

### DNS Subdomain Bruteforce

```bash
platypus subdomains <host> <wordlist>
```

Example:

```bash
platypus subdomains example.com word_lists/tiny-10.txt
```

Show all results, including non-existent subdomains:

```bash
platypus subdomains example.com word_lists/tiny-10.txt --verbose
```

### TCP Port Scan

Scan common ports:

```bash
platypus ports <host>
```

Example:

```bash
platypus ports 192.168.1.1
```

Scan specific ports:

```bash
platypus ports <host> --ports 22,80,443
```

Scan all TCP ports:

```bash
platypus ports <host> --all
```

Set the connection timeout:

```bash
platypus ports <host> --timeout 0.5
```

Show closed ports:

```bash
platypus ports <host> --verbose
```

### HTML Email Finder

```bash
platypus emails <target>
```

Example:

```bash
platypus emails example.com
```

A target with an HTTP or HTTPS scheme can also be provided:

```bash
platypus emails https://example.com
```

## 🧪 Development

Run the test suite:

```bash
pytest
```

Generate a coverage report:

```bash
pytest --cov=platypus --cov-report=term-missing
```

Run Ruff:

```bash
ruff check . --fix
ruff format .
```

## ⭐ Support the Project

If you like this project or find it useful, please give it a star! It helps increase its visibility and supports future development.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
