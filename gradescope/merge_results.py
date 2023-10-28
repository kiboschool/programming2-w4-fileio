'''
This utility program takes multiple results.json files that were generated
by Gradescope's JSONTestRunner and combines them into a single file
with the results aggregated into the appropriate JSON structure for consumption
by GradeScope.  This is useful when there are multiple projects, each with 
their own test runs, in a single submission.

This utility program is run with command line

python3 merge_results.py dir1/results.json dir2/results.json ...

The merged results.json will be written to the current directory.
'''
import json
from sys import argv

def usage():
    print("Usage: python merge_results.py [input file name] [input file name] ... ")
    print("Merged result.json is written to the current directory")
    
def main():
    ''' program starts here '''
    
    input_file_name = 'report.json'
    output_file_name = 'results.json'
   
    num_params = len(argv) - 1
    if num_params == 1:
        usage()
        return

    result_files = argv[1:]

    combined_data = None
    for file in result_files:
        with open(file, 'r') as f:
            data = json.load(f)
        if combined_data is None:
            combined_data = data
        else:
            combined_data['tests'] += data['tests']
            combined_data['score'] = \
                float(combined_data['score']) + float(data['score'])
            combined_data['execution_time'] = \
                float(combined_data['execution_time']) + float(data['execution_time'])

    with open("results.json", 'w') as f:
        json.dump(combined_data, f, indent=4)

    
if __name__ == "__main__":
    main()