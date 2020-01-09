![PyJaipurLogo](https://github.com/PyJaipur/pyjaipur.github.io/blob/master/images/logo-white.png?raw=True) 

 
## Official website for [PyJaipur](https://pyjaipur.github.io) - Python Jaipur User Group.

## Build instructions

1. Please fork https://github.com/PyJaipur/pyjaipur.github.io to your own account
2. ```bash
   git clone https://github.com/<MyFork>/pyjaipur.github.io
   cd pyjaipur.github.io
   pipenv install --dev --deploy
   pipenv run python -m website build
   ```
3. Site will be built to `docs/` folder. You can open the `index.html` file to see.


## Misc commands

Please use `pipenv run python -m website --help` to get latest help.
