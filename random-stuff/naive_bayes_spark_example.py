# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:58:59 2019

@author: amitabh.gunjan
"""

from pyspark.sql import Row
from pyspark.ml.linalg import Vectors
import pyspark as spark


spark= spark.SparkSession.builder.getOrCreate()

df = spark.SQLContext.createDataFrame(data=[Row(label=0.0, weight=0.1, features=Vectors.dense([0.0, 0.0]))
    ,Row(label=0.0, weight=0.5, features=Vectors.dense([0.0, 1.0]))
    ,Row(label=1.0, weight=1.0, features=Vectors.dense([1.0, 0.0]))])
nb = spark.ml.classification.NaiveBayes(smoothing=1.0, modelType="multinomial", weightCol="weight")
model = nb.fit(df)
model.pi
model.theta
test0 = sc.parallelize([Row(features=Vectors.dense([1.0, 0.0]))]).toDF()
result = model.transform(test0).head()
result.prediction
result.probability
result.rawPrediction
test1 = sc.parallelize([Row(features=Vectors.sparse(2, [0], [1.0]))]).toDF()
model.transform(test1).head().prediction
nb_path = temp_path + "/nb"
nb.save(nb_path)
nb2 = NaiveBayes.load(nb_path)
nb2.getSmoothing()
model_path = temp_path + "/nb_model"
model.save(model_path)
model2 = NaiveBayesModel.load(model_path)
model.pi == model2.pi
model.theta == model2.theta
nb = nb.setThresholds([0.01, 10.00])
model3 = nb.fit(df)
result = model3.transform(test0).head()
result.prediction