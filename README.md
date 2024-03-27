# ukbfetch_workflow
Example of a workflow for the resilient download of data

## Set up your virtual environemnt

Start by creating a Python virtual environment
```
python -m venv venv
```

## Install the software and its dependencies

The workflow require Snakemake and a command, ukbmanage, to run the download step in resilient way. 
```
pip install -e .[dev]
```

## Check that the ukbmanage command is working

```
ukbmanage -h
```

## Run the workflow

```
cd workflow
rm ../results/*
snakemake -p --cores=1
```


