点击率是在线广告系统中衡量广告效率的最重要指标之一。我们提供S公司部分用户在APP内11月份的卡片浏览记录，请根据用户历史浏览交互行为预测11月28，29,30日三天的赞，踩交互行为。
请点击下载本次比赛的所有数据，"高速下载"的密码为ste5。解压后会得到
1. page_view_data.tar.gz
该文件记录用户在11月份的浏览记录，解压后文件每行通过'\t'分隔，各列字段意义如下
dev_id —用户id
stat_date —日期yyyymmdd
stat_time —时间HHMMSS
post_id —卡片/帖子id
type — 1是S公司卡片数据，2是L社区数据
stat_view — APP内浏览的次数
stat_click — 点击查看详情的次数
每个用户对同一内容可能会有多次记录，表示用户的多次浏览/查看详情行为
2.post_data.txt
该文件提供11月卡片/帖子具体的内容，文件每行通过'\t'分隔，各列字段意义如下
id —帖子id
title —帖子title，可能为空
content --帖子内容
3.train.txt
该文件提供11月份前27天用户的交互记录，文件每行通过'\t'分隔，各列字段意义如下
dev_id —用户id
post_id —卡片/帖子id
praise —1表示赞，2表示踩
time —时间yyyymmddHHMMSS
根据page_view_data.tar.gz的浏览记录，请预测用户28,29,30日的赞踩行为。提交文件每行应该包含dev_id,post_id,praise三个字段，各个字段通过'\t'分隔。具体请参考sample_submission.txt
注：提交文件最多包含20万行，最大10M
记分规则：
提交数据的记分通过F1-Measure来打分
P 准确率
R 召回率
F1 = 2P*R/(P+R)
