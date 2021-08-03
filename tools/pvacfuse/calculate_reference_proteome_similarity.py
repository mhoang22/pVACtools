import sys
from lib.calculate_reference_proteome_similarity import *

def define_parser():
    return CalculateReferenceProteomeSimilarity.parser('pvacfuse')

def main(args_input = sys.argv[1:]):
    parser = define_parser()
    args = parser.parse_args(args_input)

    CalculateReferenceProteomeSimilarity(
    	args.input_file,
    	args.input_fasta,
    	args.output_file,
    	args.match_length,
    	args.species,
    	'pVACfuse',
    	args.blastp_path,
    	args.blastp_db
	).execute()

if __name__ == "__main__":
    main()