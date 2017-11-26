#using encoding = 'utf-8'
#the right way to loading your data
#eg:
setwd('D:/Project/Homework/机器学习与文本挖掘/zhbitNew文本挖掘')
zhbitNew <- read.table('2013-2017.txt', sep = '', 
                       header = F, encoding = 'UTF-8')
