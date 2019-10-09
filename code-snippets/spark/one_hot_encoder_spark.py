# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:38:45 2019

@author: amitabh.gunjan
"""

from __future__ import print_function

# $example on$
from pyspark.ml.feature import OneHotEncoder
# $example off$
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("OneHotEncoderExample").getOrCreate()

    # Note: categorical features are usually first encoded with StringIndexer
    # $example on$

from pyspark.ml.feature import OneHotEncoderEstimator

#spark.createDataFrame
df = spark.createDataFrame([(0.0, 1.0),(1.0, 0.0),(2.0, 1.0),(0.0, 2.0),(0.0, 1.0),(2.0, 0.0)], ["categoryIndex1", "categoryIndex2"])

encoder = OneHotEncoderEstimator(inputCols=["categoryIndex1", "categoryIndex2"],
                                 outputCols=["categoryVec1", "categoryVec2"])
model = encoder.fit(df)
encoded = model.transform(df)
encoded.show()
encoded.columns
encoded.approxQuantile('categoryVec1', probabilities=(0.9,), relativeError = 0.0)
