import argparse
import os
import pandas as pd 

def run_parking_vioaltion_data_pipleine(input_file:str,output_loc:str,run_id:str) -> None:
    df=pd.read_csv(input_file)
    df.to_parquet(
        os.path.join(output_loc ,run_id),partition_cols=["Registration State"]
    )

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument(
        "--input-file",
        type=str,
        help="The input file",
    )    
    parser.add_argument(
        "--output-loc",
        type=str,
        help="the output folder",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        help="The day of run,in yyyymmdd format",
    )

    opts = parser.parse_args()
    run_parking_vioaltion_data_pipleine(
        input_file=opts.input_file, output_loc=output_loc, run_id=ops.run_id
    )
    