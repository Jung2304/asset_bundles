from pyspark import pipelines as dp

@dp.table(name = "transformation")
def transformation():
    return spark.range(10)