# VeracityMeasures
The mapper of Spam Index is calculateDiffusionIndexMapper.py.


hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -D mapred.reduce.tasks=3
-D mapreduce.map.memory.mb=6144 -D mapreduce.reduce.memory.mb=8192
-D stream.num.map.output.key.fields=1 
-files /home/paryani/DGSVeracityIndices/tweetCount,/home/paryani/VeracityAnalysis/topic1,/home/paryani/VeracityAnalysis/topic2,/home/paryani/VeracityAnalysis/topic3
-file /home/paryani/DGSVeracityIndices/calculateGeographicIndexMapper.py 
-file /home/paryani/DGSVeracityIndices/calculateGeographicIndexReducer.py 
-mapper calculateGeographicIndexMapper.py 
-reducer calculateGeographicIndexReducer.py 
-input /TwitterData/FLU/Flu_01 
-output /paryani/geographicIndexNewPart1



tweetCount file has just the count of tweets. Say for above command the tweetcount for Flu_01 is 7027167
