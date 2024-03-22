import defopt
from pathlib import Path
from ukbfetch.api import fetch, check


def main(cmd: str, *, input_file: Path, output_file: Path):
    
    if cmd == 'fetch':
        fetch(input_file=input_file, output_file=output_file)
    elif cmd == 'check':
        check(input_file=input_file, output_file=output_file)
    
if __name__ == '__main__':
    defopt.run(main)
