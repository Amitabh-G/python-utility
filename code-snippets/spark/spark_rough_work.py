# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:02:44 2019

@author: amitabh.gunjan
"""
import pyspark
pyspark.find_spark_home.os.curdir
pyspark.__version__
spark = SparkSession.builder.master("local").appName("Word Count").config("spark.some.config.option", "some-value").getOrCreate()

pyspark.SparkConf().getAll()
conf = pyspark.SparkConf()
conf.getAll()
conf.setAppName("My App")
context = pyspark.SparkContext()

from pyspark import SparkConf, SparkContext
from pyspark import SparkSession
conf = SparkConf().setAppName("PySpark App").setMaster("spark://master:7077")
sc = SparkContext.getOrCreate(conf = conf)
