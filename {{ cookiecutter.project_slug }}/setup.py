# %%
import duckdb
import os

con = duckdb.connect("files.duckdb")

# %%
folders = ["hosp"]

for folder in folders:
    con.sql(f"CREATE SCHEMA if not exists {folder}")
    files = os.listdir(f"./data_source/{folder}/")
    for file in files:
        table_name = file.split(".")[0]
        print(table_name)
        if table_name == "":  # for file name .DS_Store
            continue
        con.sql(f"DROP TABLE if exists {folder}.{table_name}")
        con.sql(
            f"CREATE TABLE {folder}.{table_name} AS FROM read_csv_auto('./data_source/{folder}/{table_name}.csv.gz', HEADER=true, sample_size=-1)"
        )

con.close()
