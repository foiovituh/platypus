# 🦆 Platypus
![GitHub License](https://img.shields.io/github/license/foiovituh/platypus)
![GitHub Release](https://img.shields.io/github/v/release/foiovituh/platypus)

> A command-line reconnaissance tool for DNS enumeration and TCP port scanning.

![Image](https://github.com/user-attachments/assets/9984e089-5945-40ef-a754-98d3c2e76d30)

## 📦 Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/foiovituh/platypus.git
cd platypus

python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

`python -m pip` ensures that pip is executed using the currently active Python interpreter. You can also use `pip` directly if your environment is correctly configured.

To use Platypus in a new terminal session, activate the virtual environment again:

```bash
source .venv/bin/activate
```

### Development environment

Install development dependencies:

```bash
python -m pip install -e ".[dev]"
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