#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    newdf = df.groupby("Publisher")["WoC"].sum()
    max = newdf.idxmax()
    mask = df["Publisher"] == max
    return df[mask]

def main():
    best_record_company()
    

if __name__ == "__main__":
    main()
