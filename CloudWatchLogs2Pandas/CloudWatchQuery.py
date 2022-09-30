# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_CloudWatchQuery.ipynb.

# %% auto 0
__all__ = ['CloudWatchQuery', 'foo']

# %% ../nbs/00_CloudWatchQuery.ipynb 13
import awswrangler as wr
import pandas as pd
import boto3

class CloudWatchQuery:
    "Configure a  CloudWatch query"
    def __init__(self, query, log_group): 
        self.query = query 
        self.log_group = log_group
        
    def get_df(self):
        "Execute the query"
        df = wr.cloudwatch.read_logs(
            log_group_names=[self.log_group],
            query=self.query,
            boto3_session = boto3.Session(region_name="us-west-2")
        )
        return df

# %% ../nbs/00_CloudWatchQuery.ipynb 16
def foo(): pass
