import argparse
from pathlib import Path
import random
import tempfile
import shutil
import os

def download(input_file: Path, output_file: Path, fail_ratio: float, seed: int) -> None:
    """
    Simulates a download of data from the UK Biobank
    
    :param input_file: text file listing patient name, scan type 
    :param output_file: text file recording the entries that failed to be downloaded
    :param fail_ratio: average number of failures 
    :param seed: random seed
    """
    random.seed(seed)
    fout = open(output_file, 'w')
    for line in open(input_file).readlines():
        # randomly fail
        if random.random() < fail_ratio:
            print(f'Warning: {line} failed!')
            fout.write(line)
            
def download_until_success(input_file: Path='', output_file: Path='', 
                           fail_ratio: float=0.3, seed: int=123) -> None:
    
    
    # perform the download in a temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)
        
        tmp_input_file = 'input.txt'
        tmp_output_file = 'output.txt'
        
        # initially input and output files are the same
        shutil.copyfile(input_file, tmp_input_file)
        shutil.copyfile(input_file, tmp_output_file)
        
        # iterate until the output file is empty (ie all files have been successfully downloaded)
        iteration = 0
        while os.path.getsize(tmp_output_file) > 0:
            
            print(f'iteration: {iteration}')
            download(tmp_input_file, tmp_output_file, fail_ratio=fail_ratio, seed=seed+iteration)
            
            # the output file becomes the input file
            shutil.copyfile(tmp_output_file, tmp_input_file)
            
            iteration += 1
        
        # copy the output back
        shutil.copyfile(tmp_output_file, output_file)
    
            
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='', 
                        help='Specify the absolute path to the input file')
    parser.add_argument('-o', '--output', default='', 
                        help='Specify the absolute path to the output file')
    parser.add_argument('-f', '--fail', default=0.3, type=float,
                        help='Specify the ratio of failures')
    parser.add_argument('-s', '--seed', default=123, type=int,
                        help='Specify the random seed')
    args = parser.parse_args()

    download_until_success(args.input, args.output, args.fail, args.seed)
    
    return 0
    
if __name__ == '__main__':
    main()
    

