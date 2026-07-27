# 🦆 Platypus
![GitHub License](https://img.shields.io/github/license/foiovituh/platypus)
![GitHub Release](https://img.shields.io/github/v/release/foiovituh/platypus)

> 🛡️ A lightweight information gathering tool featuring DNS subdomain bruteforce and TCP port scanning.

<!-- Add a terminal screenshot or GIF here -->
<!-- ![Image](https://...) -->

## 📦 Installation

```bash
git clone https://github.com/foiovituh/platypus.git
cd platypus

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e .
```

### Development environment

Install development dependencies:

```bash
pip install -e ".[dev]"
```

## 🚀 Usage

### Help

```bash
platypus --help
```

### DNS Subdomain Bruteforce

```bash
platypus --sb <host> <wordlist>
```

Example:

```bash
platypus --sb example.com word_lists/tiny-10.txt
```

### TCP Port Scan

```bash
platypus --ps <host>
```

Example:

```bash
platypus --ps 192.168.1.1
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

## 📁 Project Structure

```text
.
├── src/
│   └── platypus/
├── tests/
├── word_lists/
├── pyproject.toml
└── README.md
```

## 🗺️ Roadmap

- [x] DNS subdomain bruteforce
- [x] TCP port scanner
- [ ] Custom timeout
- [ ] UDP port scan
- [ ] Banner grabbing
- [ ] DNS record enumeration
- [ ] Reverse DNS lookup
- [ ] IPv6 support
- [ ] Subcommands (`platypus dns`, `platypus port`)
- [ ] Parallel execution
- [ ] Service detection

## ⭐ Support the Project

If you like this project or find it useful, please give it a star! It helps increase its visibility and supports future development.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.