from pathlib import Path
import random
import difflib


def fetch(input_file: Path, output_file: Path,
    ratio_fail: float=0.1, seed=None):
    """Fetch data   

    Args:
        input_file (Path): Input file listing patient and scan_type
        output_file (Path): Output file containing list of downloaded files
        ratio_fail (float): Ratio of failure
        seed (float): random seed
    """

    random.seed(seed)

    with open(input_file, 'r') as fi:
        
        with open(output_file, 'w') as fo:

            for line in fi.readlines():
                patient, scan_type = line.split(' ')

                # randomly fail
                if random.random() > ratio_fail:
                    # success, write to the output file
                    fo.write(f'{patient} {scan_type}\n')
                else:
                    print(f'ERROR: failed to fetch data for patient {patient} and scan type {scan_type}')
            

def check(input_file: Path, output_file: Path) -> int:
    """Check if the fetch operation succeeded 

    Args:
        input_file (Path): Input file listing patient and scan_type
        output_file (Path): Output file containing list of downloaded files
        
    Returns: 0 if no error
            >0 if error
    """

    with open(input_file) as f:
        input_lines = f.readlines()
        
    with open(output_file) as f:
        output_lines = f.readlines()
      
      
    cmp = difflib.Differ().compare(input_lines, output_lines)
    
    ier = 0  
    # count the differences
    for line in cmp:
        if line[0] == '-':
            # present in input and absent in output
            print(f'Warning: missing {line}')
            ier += 1
                                
    return ier
