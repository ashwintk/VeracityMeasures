# OTC MOODEL
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -D mapred.reduce.tasks=3
 -D mapreduce.map.memory.mb=6144 -D mapreduce.reduce.memory.mb=8192 -D stream.num.map.output.key.fields=1
 -files /home/paryani/VeracityAnalysis/topic1,/home/paryani/VeracityAnalysis/topic2,/home/paryani/VeracityAnalysis/topic3
 -file /home/paryani/OTCAnalysis/calculateObjectivityMapper.py
 -file /home/paryani/VeracityAnalysis/otcReducer.py -mapper calculateObjectivityMapper.py -reducer otcReducer.py
 -input /TwitterData/FluTweetsText/TweetsJPPreProcess1 -output /paryani/objectivityPart1

