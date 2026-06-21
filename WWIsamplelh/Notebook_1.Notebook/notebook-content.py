# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7ecbadfc-7af3-4ff7-a490-07fc5c9b6852",
# META       "default_lakehouse_name": "wwisamplelh",
# META       "default_lakehouse_workspace_id": "66154246-634f-4485-88d1-1634ff4cf0af",
# META       "known_lakehouses": [
# META         {
# META           "id": "7ecbadfc-7af3-4ff7-a490-07fc5c9b6852"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM wwisamplelh.dbo.dimension_city LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
