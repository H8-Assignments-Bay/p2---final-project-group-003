[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8070902&assignment_repo_type=AssignmentRepo)

## Environment Setup
### Conda
`conda env create -p ./env -f ./environment.yml`

Run
`conda activate ./env`

## Init Rasa (OPTIONAL)
`rasa init`

## Run the latest rasa model
1. Start action endpoint. This is where we store our actions (class and functions)
`rasa run actions`

2. On a different terminal / command prompt / anaconda prompt
`rasa shell`

3. Profit
