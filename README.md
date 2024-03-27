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
This will install module `ukb` and its dependencies. Option `-e` means "editable", code changes will be reflected in the installed software without the need to re-install the software (good for development).

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
This can be run on a laptop.

## How things work

The workflow executes a single step, calling `ukbmanage`. This command will pretend to download files, iteratively until all files have been successfully downloaded. An empty file `success.txt` is produced at the end of the step to let the workflow manager know that the step was successful. 

## Future work

The `download` step in the src/ukb/ukb.py step would need to be replaced with the actual ukbfetch call. This call would need to be executed via a Slurm job. Another function would need to be written to detect which files have not been successfully downloaded. The function would return an input file (argument to the -b option of ukbfetch), allowing ukbfetch to be invoked until all files are available.

Module [submitit](https://github.com/facebookincubator/submitit) could be used to submit a script from Python.

The Snakefile file could be enhanced to support multiple concurrent file downloads.
