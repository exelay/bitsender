# bitsender
A script for sending bitcoins to multiple addresses.

## Installation
### Clone This Repository
```shell
git clone https://github.com/exelay/bitsender.git
cd bitsender
```
### Make Virtual Environment
```shell
python3 -m venv venv
source venv/bin/activate
```
### Install Requirements
```shell
pip install -r requirements.txt
```
### Create Configuration File
```shell
cp configurations/example.config.yaml configurations/config.yaml
```
## Usage
### Update Configuration
Open the `config.yaml` file with any text editor and fill in all the fields with
your information. And save changes.

For example:
```shell
vim config.yaml
```
```yaml
# List of recipients.
# In square brackets: bitcoin wallet address, amount of money and currency. (usd or btc)
# All the money is sent in bitcoins, if you specify e.g. 10 usd,
# they will be automatically converted into bitcoins according to the current exchange rate.
recipients:
  - [mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB, 10, usd]
  - [tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt, 0.0015, btc]

# Fee for one byte
# You can leave this field blank, then fee will be calculated automatically.
fee: 70

# Wallet private key
key: cPmJ6LdYHeX46pJGvi5hbbmHjDGQQ1goCbBZEyNk5b2UG7GX6FkS
```

### Run Script
```shell
python bitsender.py run
```
With this run, the script will take all the data from the `config.yaml` file.
### Support for different configurations
If you want to create several different configuration files, 
store them and use them for different purpose situations, you can do this. 
Simply copy the `config.yaml` file and rename it.
For example:
```shell
cp config.yaml custom-config.yaml
```
Then run the script with this command:
```shell
python bitsender.py run path/to/the/custom-config.yaml
```
Where `path/to/the/custom-config.yaml` is path to your custom configuration file.
