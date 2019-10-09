# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:19:30 2019

@author: amitabh.gunjan
"""

import pandas as pd
import _pickle as cPickle
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
#spark = SparkSession.builder.appName("read-file-fit-model").getOrCreate()
#spark = SparkSession.builder.appName("read-file-fit-model").getOrCreate()
#spark = SparkSession.Builder.master("local[4]").appName("read-file-fit-model").getOrCreate()
#spark = SparkSession.builder.master("local[4]").appName("read-file-fit-model").getOrCreate()

#spark = SparkSession.Builder()
#spark.master("local[4]").appName("read-file-fit-model").getOrCreate()
spark = SparkSession.builder.appName("read-file-fit-model").getOrCreate()
#spark.stop()
spark.read.text('D:/work/recommendation-system/ml-based/supplier-connect-data.txt')

textRDD2 = spark.read.text('D:/work/recommendation-system/ml-based/supplier-connect-data.txt')
textRDD2.columns
textRDD2.printSchema()

data_path = 'D:/work/recommendation-system/ml-based/supplier-connect-data.dat'
with open(data_path, 'rb') as f:
    data_txt = cPickle.load(f)

data_pd_df = pd.DataFrame(data_txt)
data_pd_df.info()

data_path = 'D:/work/recommendation-system/ml-based/supplier-connect-data.dat'
with open(data_path, 'rb') as f:
    data_txt = cPickle.load(f)

def remove_nested_dicts_from_data(input_data):
    """Augment data with the userId so that userid could be used as an independent variable. Also remove the empty dictionaries from the container"""
    input_data_new = []
    for data in input_data:
#        data['userId'] = str(user)
        data = {i:j for i, j in data.items() if isinstance(j, dict) != True}
        input_data_new.append(data)
    # input_data_new = input_data_new[:20]
    return input_data_new

data_txt_new = remove_nested_dicts_from_data(data_txt)

from pyspark.sql import Row
spark_df_array_row = spark.createDataFrame(Row(**x) for x in data_txt_new).show(truncate=False)

data_pd_df = pd.DataFrame(data_txt_new)
data_pd_df.info()

data_pd_df_sliced = data_pd_df.iloc[:,0:6]
spark_df = spark.createDataFrame(data_pd_df_sliced)
spark_df.printSchema()
spark_df.count()
spark_df.take(5)
Y_col = spark_df.columns[0]
X_col = spark_df.columns[1:]
train_Y = spark_df.select(Y_col)
train_X = spark_df.select(X_col)

#################################################################
### Repartition the data - coalesce them - decrease the partition
#################################################################

# Does not work if you don't change the bindings.
train_X.rdd.getNumPartitions()
train_X.repartition(1)
train_X.rdd.getNumPartitions()
train_X.coalesce(1)
train_X.rdd.getNumPartitions() == 8

# Change the varible name
train_X_repartitioned = train_X.rdd.coalesce(1)
train_X_repartitioned_new = train_X.rdd.repartition(1)
train_X_repartitioned_new.getNumPartitions()



#################################################################
from pyspark.ml.feature import VectorAssembler
assembler = VectorAssembler(inputCols=X_col, outputCol=Y_col)
from pyspark.ml.feature import OneHotEncoder, StringIndexer
encoder = OneHotEncoder(inputCol="indexed", outputCol="features")

df = spark.createDataFrame([
    (0, "a"),
    (1, "b"),
    (2, "c"),
    (3, "a"),
    (4, "a"),
    (5, "c")
], ["id", "category"])

stringIndexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
model = stringIndexer.fit(df)
indexed = model.transform(df)
indexed.printSchema()
indexed.take(1)
indexed.take(5)


train_Y.printSchema()
train_X.printSchema()
train_X.schema.json()
train_X.columns
spark_df.columns
import json
data_schema = json.loads(train_X.schema.json())
isinstance(data_schema, dict)
StringIndexer(inputCol='x1', outputCol='indexed_x1')
ac = spark_df.select('assetclass')
ac.printSchema()
ac.take(4)
vecAssembler = VectorAssembler(inputCols=spark_df.columns, outputCol="features")
vecAssembler.transform(spark_df)

def string_index(spark_df):
    """Create an index for each of the categorical column of the data set."""
    for i in spark_df.columns:
        inp_col = str(i)
        out_col = str(i) + "_indexed"
        fit_on = spark_df.select(str(i))
        df_i_indexed = StringIndexer(inputCol = inp_col, outputCol = out_col).fit(fit_on).transform(fit_on)
        indexed_col = df_i_indexed.select(out_col)
        print(i)
        indexed_col.printSchema()
        out_col_ohe = str(i) + "_encoded"
        try:
            df_i_encoded = OneHotEncoder(inputCol = out_col, outputCol = out_col_ohe).transform(df_i_indexed).show()
            df_i_encoded.select(out_col_ohe)
            vecAssembler = VectorAssembler(inputCols = out_col_ohe, outputCol="features")
            vecAssembler.transform(spark_df)
        except:
            pass
    return None
string_index(spark_df)
spark_df.columns

#########################################
### Pyspark implementation
#########################################
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
categoricalColumns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'poutcome']
stages = []
categoricalColumns = spark_df.columns

for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol = categoricalCol, outputCol = categoricalCol + 'Index')
#    encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
    encoder = OneHotEncoder(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
    stages += [stringIndexer, encoder]
    
label_stringIdx = StringIndexer(inputCol = 'deposit', outputCol = 'label')
stages += [label_stringIdx]
numericCols = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous']
assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler]

from pyspark.ml import Pipeline
pipeline = Pipeline(stages = stages)
pipelineModel = pipeline.fit(df)
df = pipelineModel.transform(df)
selectedCols = ['label', 'features'] + cols
df = df.select(selectedCols)
df.printSchema()

train, test = df.randomSplit([0.7, 0.3], seed = 2018)
print("Training Dataset Count: " + str(train.count()))
print("Test Dataset Count: " + str(test.count()))
from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=10)
lrModel = lr.fit(train)


######################################################################
def transform_data_for_spark(spark_df):
    """Create pipeline for transforming the data to spark data frame."""
    from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
#    categoricalColumns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'poutcome']
    stages = []
#    categoricalColumns = spark_df.columns
    categoricalColumns = ['allocatedQty', 'assetclass', 'calledOffQty', 'contractRefNo']
    for categoricalCol in categoricalColumns:
        stringIndexer = StringIndexer(inputCol = categoricalCol, outputCol = categoricalCol + 'Index')
        encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
#        encoder = OneHotEncoder(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
        stages += [stringIndexer, encoder]
    label_stringIdx = StringIndexer(inputCol = 'calledOffQty', outputCol = 'label')
    stages += [label_stringIdx]
    assemblerInputs = [c + "classVec" for c in categoricalColumns]
    assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
    stages += [assembler]
    from pyspark.ml import Pipeline
    pipeline = Pipeline(stages = stages)
    try:
        pipelineModel = pipeline.fit(spark_df)
        spark_df = pipelineModel.transform(spark_df)
    except:
        pass
    selectedCols = ['label', 'features'] + categoricalColumns
#    selectedCols = ['label', 'features']
    spark_df = spark_df.select(selectedCols)
    spark_df.printSchema()
    return spark_df
spark_df_transformed = transform_data_for_spark(spark_df)

from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=10)
lrModel = lr.fit(spark_df_transformed)
lrModel.coefficientMatrix


#####################################
### Save and load model using PySpark
#####################################
lrModel.save('D:/lr-spark.dat')
from pyspark.ml.classification import LogisticRegressionModel
lr_loded = LogisticRegressionModel.load('D:/lr-spark.dat')

###############
### Serializers
###############
from pyspark.serializers import PickleSerializer
PickleSerializer.dumps(lrModel, 'D:/lr-spark-pickle.dat')
#######################################
### Column names in the spark DataFrame
#######################################
spark_df_transformed.columns
spark_df_transformed.printSchema()

#################################
### Schema of the spark DataFrame
#################################
spark_df_transformed.printSchema()
spark_df_transformed.stat
feat_vec = spark_df_transformed.select('features')
feat_vec.printSchema()
feat_vec.take(1)

####################################
### Count number of rows in the data
####################################
feat_vec.count()

##############################
### Take five rows of the data
##############################
spark_df_transformed.take(5)

###############################################
### Get the number of partitions of the dataset
###############################################
spark_df.rdd.getNumPartitions()

#############
### Fit model
#############
from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=10)
lrModel = lr.fit(spark_df_transformed)

#################################################################################################
### Need to partition the spark dataframe by the columns for having the dependent and independent 
### variables in the same dataframe and make as many partitions for as the number of fields in data.
### Fit the model on each partition of the data in parallel so that the separate models can be 
### trained fast enough.
###################################################################################################
#df.coalesce(1).rdd.getNumPartitions()


repartitioned_df = spark_df.repartition(8, ['allocatedQty', 'assetclass'])
repartitioned_df.printSchema()
repartitioned_df.take(3)
spark_df.rdd.glom().collect()
print("Partitions structure: {}".format(spark_df.rdd.glom().collect()))


import pyspark
pyspark.__version__






