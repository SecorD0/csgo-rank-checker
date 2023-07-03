<h1><p align="center">csgo-rank-checker</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [DISCLAIMER](#DISCLAIMER)
- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker (image)](#Docker-image)
    - [Docker (building)](#Docker-building)
    - [Source code](#Source-code)
- [Updating](#Updating)
  - [Windows](#Windows-1)
  - [GitHub image](#GitHub-image)
  - [Self-built image](#Self-built-image)
  - [Source code](#Source-code-1)
- [Useful commands](#Useful-commands)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">DISCLAIMER</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program has no injections — you can make the code review to make sure. Any cases of third parties gaining access to your accounts aren't the fault of the developer, but of you or another person. Keep your sensitive data in a safe place.

⠀By using this program you have agreed to the above and have no and won't have claims against its developer.



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to check CS:GO ranks on your accounts.



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[csgo-rank-checker](https://github.com/SecorD0/csgo-rank-checker)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `maFiles` — a directory with maFiles from accounts;
  - `accounts.db` — a temporary database to save the state;
  - `accounts.xlsx` — an import and export spreadsheet;
  - `errors.log` — a log file with errors that occurred during the work;
  - `proxies.txt` — a text file with proxies that will be used randomly for logins and requests.
- `csgo-rank-checker.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/csgo-rank-checker/releases).
2. Create a folder and put the EXE file in it.
3. Run the program the first time to create necessary files.
4. Open, fill in the spreadsheet called `accounts.xlsx` with logins and passwords and close it.
5. Copy maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
6. Insert HTTP IPv4 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
7. Run the program again, wait for it to finish and close it.
8. Open the `accounts.xlsx` spreadsheet to view the results. You can see the following account statuses:
   - `new` — an account that, for whatever reason, wasn't checked;
   - `wrong credentials` — a wrong login or password;
   - `email guard` — the account is enabled to receive Steam Guard codes to the email, and the program doesn't support this type of authentication;
   - `checked` — the account was successfully checked.
9. If for some reason there are unchecked accounts left, you can go back to step `7`.


<h2><p align="center">Docker (image)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/csgo-rank-checker/files:/program/files --name csgo-rank-checker ghcr.io/secord0/csgo-rank-checker:main
```
3. Open, fill in the spreadsheet called `accounts.xlsx` with logins and passwords and close it.
4. Copy maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
5. Insert HTTP IPv4 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
6. Run the program again, wait for it to finish and close it:
```sh
docker run -it --rm -v $HOME/csgo-rank-checker/files:/program/files --name csgo-rank-checker ghcr.io/secord0/csgo-rank-checker:main
```
7. Open the `accounts.xlsx` spreadsheet to view the results. You can see the following account statuses:
   - `new` — an account that, for whatever reason, wasn't checked;
   - `wrong credentials` — a wrong login or password;
   - `email guard` — the account is enabled to receive Steam Guard codes to the email, and the program doesn't support this type of authentication;
   - `checked` — the account was successfully checked.
8. If for some reason there are unchecked accounts left, you can go back to step `6`.


<h2><p align="center">Docker (building)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/csgo-rank-checker
```
3. Go to the repository:
```sh
cd csgo-rank-checker
```
4. Build an image:
```sh
docker build -t csgo-rank-checker .
```
5. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/csgo-rank-checker/:/program --name csgo-rank-checker csgo-rank-checker
```
6. Open, fill in the spreadsheet called `accounts.xlsx` with logins and passwords and close it.
7. Copy maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
8. Insert HTTP IPv4 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
9. Run the program again, wait for it to finish and close it:
```sh
docker run -it --rm -v $HOME/csgo-rank-checker/:/program --name csgo-rank-checker csgo-rank-checker
```
10. Open the `accounts.xlsx` spreadsheet to view the results. You can see the following account statuses:
    - `new` — an account that, for whatever reason, wasn't checked;
    - `wrong credentials` — a wrong login or password;
    - `email guard` — the account is enabled to receive Steam Guard codes to the email, and the program doesn't support this type of authentication;
    - `checked` — the account was successfully checked.
11. If for some reason there are unchecked accounts left, you can go back to step `9`.


<h2><p align="center">Source code</p></h2>

1. Install [Python 3.8](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/csgo-rank-checker
```
3. Go to the repository:
```sh
cd csgo-rank-checker
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py` the first time to create necessary files.
7. Open, fill in the spreadsheet called `accounts.xlsx` with logins and passwords and close it.
8. Copy maFiles to the `maFiles` directory, among which the program will search for those that belong to the specified ones.
9. Insert HTTP IPv4 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
10. Run the `app.py` again, wait for it to finish and close it.
11. Open the `accounts.xlsx` spreadsheet to view the results. You can see the following account statuses:
    - `new` — an account that, for whatever reason, wasn't checked;
    - `wrong credentials` — a wrong login or password;
    - `email guard` — the account is enabled to receive Steam Guard codes to the email, and the program doesn't support this type of authentication;
    - `checked` — the account was successfully checked.
12. If for some reason there are unchecked accounts left, you can go back to step `10`.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn csgo-rank-checker -i images/icons/app.ico --add-binary "images/icons;images/icons"
```



<h1><p align="center">Updating</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file of the new version from the [releases page](https://github.com/SecorD0/csgo-rank-checker/releases) and replace the old one with it.


<h2><p align="center">GitHub image</p></h2>

1. Stop the container:
```sh
docker stop csgo-rank-checker
```
2. Remove the container:
```sh
docker rm csgo-rank-checker
```
3. Update the image:
```sh
docker pull ghcr.io/secord0/csgo-rank-checker:main
```


<h2><p align="center">Self-built image</p></h2>

1. Stop the container:
```sh
docker stop csgo-rank-checker
```
2. Remove the container:
```sh
docker rm csgo-rank-checker
```
3. Go to the repository:
```sh
cd csgo-rank-checker
```
4. Update the local files:
```sh
git pull
```
5. Rebuild the image:
```sh
docker build -t csgo-rank-checker .
```


<h2><p align="center">Source code</p></h2>

1. Go to the repository:
```sh
cd csgo-rank-checker
```
2. Update the local files:
```sh
git pull
```



<h1><p align="center">Useful commands</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀To run the program (GitHub image):
```sh
docker run -it --rm -v $HOME/csgo-rank-checker/files:/program/files --name csgo-rank-checker ghcr.io/secord0/csgo-rank-checker:main
```

⠀To run the program (self-built image):
```sh
docker run -it --rm -v $HOME/csgo-rank-checker/:/program --name csgo-rank-checker csgo-rank-checker
```

⠀To remove the container:
```sh
docker stop csgo-rank-checker; docker rm csgo-rank-checker
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/csgo-rank-checker/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Address of EVM networks (Ethereum, Polygon, BSC, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
