### platypus 🦆

generic information gathering scanner

### done/planned
- [x] subdomain bruteforce<br>
- [x] port scanning<br>
- [ ] DNS zone transfer (AXFR)

### requirements 
- python3
- pip3

### setup
- pip3 install -r requirements.txt

### usage
```
python3 platypus.py [module type] [optional flags...]

MODULES:
  --sb (DNS subdomain bruteforce)
  --ps (Port scan) [--all, 65536 ports, optional] [--v, verbose, optional]
    DEFAULT_PORTS_TO_BE_SCANNED:
      21, 22, 23, 25, 26, 53, 80, 110, 143,
      443, 587, 993, 995, 2082, 2083, 3306, 8080
EXAMPLES:
  python3 platypus.py --sb
  host name: google.com
  word list path: word_lists/example-10.txt

  python3 platypus.py --ps --all
  host name: bancocn.com
  timeout: 0.05
```
