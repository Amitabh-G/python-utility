# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:10:52 2019

@author: amitabh.gunjan
"""
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("app-name-of-your-choice").setMaster("local[*]").set("spark.sql.execution.arrow.enabled", "true")
try:
    sc = SparkContext(conf=conf)
except ValueError:
    pass

rdd = sc.parallelize([10,20,30,40,50,10,20,35]).map(lambda x : (float(x)/10, float(x)/10))
elements = rdd.partitionBy(2,lambda x: int(x > 3)).map(lambda x: x[0]).glom().collect()
elements
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("train-model").getOrCreate()
spark.createDataFrame(elements)
import pyarrow
spark.sparkContext._conf.getAll()