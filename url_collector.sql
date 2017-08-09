drop table if exists urls;
create table urls(
	domain varchar(128) primary key,
	top varchar(32),
	second varchar(128),
	third varchar(128),
	sub_class_id integer(16)
);

drop table if exists class;
create table class(
	id integer(16) primary key,
	name varchar(64) not null,
	parent_class integer(4) not null
);

drop table if exists sub_class;
create table sub_class(
	id integer(16) primary key,
	name varchar(64) not null,
	parent_class integer(16) not null,
	description varchar(256)
);

insert into class ( id, name, parent_class ) values ( 3, '搜索', -1),
(4, '门户', -1),
(5, '时政', -1),
(6, '财经', -1),
(7, '工具', -1),
(8, '社交' , -1),
(9, '招聘' , -1),
(10, '生活' , -1),
(11, '电商' , -1),
(12, '休闲' , -1),
(13, '教育' , -1),
(14, '数码' , -1),
(15, '汽车' , -1),
(16, '专业' , -1),
(17, '公益' , -1),
(18, '其他' , -1);

insert into sub_class ( id, name, parent_class, description) values (120, 'Undefined', 18, 'Undefined'),
(128, '搜索引擎', 3, '专业提供搜索服务的网站'),
(129, '导航门户', 4, '大型门户导航综合性网站'),
(130, '新闻', 5, '侧重时政要闻的大型媒体网站'),
(131, '军事', 5, '军事题材的各类网站及相关论坛'),
(132, '政府机关', 5, '军事题材的各类网站及相关论坛'),
(133, '银行', 6, '银行及其主管部门创立的网站'),
(134, '理财', 6, '各类理财公司创立的网站'),
(135, '保险', 6, '保险及其主管部门创立的网站'),
(136, '股票', 6, '证券机构及其主管部门创立的网站'),
(137, '基金', 6, '基金及其主管部门创立的网站'),
(138, '网页邮箱', 7, '各类电子邮箱提供商的网站'),
(139, '下载站点', 7, '提供各类软件、文档下载的相关网站'),
(140, '病毒查杀', 7, '各类杀毒软件相关网站'),
(141, '设计素材', 7, '提供设计类各种素材的相关网站'),
(142, '博客论坛', 8, '提供博客、论坛为主的相关网站'),
(143, '交友聊天', 8, '即时消息会话软件与交友软件相关的网站'),
(144, '人才招聘', 9, '包括各种涉及求职和招聘相关信息及专业人才信息的网站'),
(145, '生活休闲', 10, '提供生活周边服务信息搜索及发布的相关网站'),
(146, '交通旅游', 10, '旅游类交通网站'),
(147, '房地产', 10, '房屋类交易、买卖、租赁、装修及中介服务信息发布的平台相关网站'),
(148, '医疗保健', 10, '医疗保健相关企业或个人创立的网站或服务信息及相关论坛网站'),
(149, '网购', 11, '主流网购平台网站'),
(150, '商贸', 11, '各类商贸企业或以宣传自产产品为主的专业网站'),
(151, '物流', 11, '互联网线上消费后线下运送货物的各类企业网站'),
(152, '支付', 11, '满足电子商务支付目的的第三方服务相关网站'),
(153, '文化体育', 12, '传统文化、运动健身类体育活动的专业网站及论坛网站'),
(154, '音乐', 12, '音乐在线或下载服务的相关网站'),
(155, '游戏', 12, '各类游戏专业网站及相关论坛网站'),
(156, '视频', 12, '各类直播或点播视频提供者的相关网站'),
(157, '小说', 12, '以在线、下载等方式提供文字或语音小说阅读的网站'),
(158, '娱乐', 12, '各类娱乐八卦相关网站'),
(159, '翻译', 13, '提供多种语言之间互译功能的相关网站'),
(160, '学习考试', 13, '各类互联网线上学习、在线考试或报名的专业网站'),
(161, '公共关系', 13, '提供公共关系学习、传播的各类相关网站'),
(162, '科普', 13, '面向大众普及科学知识的相关网站'),
(163, '艺术', 13, '包括与艺术、艺术品相关的各类资讯的相关网站'),
(164, '手机', 14, '主流手机终端、操作系统相关论坛及网站'),
(165, '摄影', 14, '摄影器材、技术等论坛及相关网站'),
(166, '数码资讯', 14, '潮流数码产品或操作系统论坛及相关网站'),
(167, '汽车资讯', 15, '汽车品牌自创企业网站及汽车类相关商品及价格的资讯网站'),
(168, '医药学', 16, '医药类生产销售等相关企业网站及相关论坛'),
(169, '气候学', 16, '气候学专业网站'),
(170, '计算机科学', 16, '计算机科学与技术的专业论坛及网站'),
(171, '商业', 16, '大宗商品贸易信息及主管机构相关网站'),
(172, '农业', 16, '大宗农产信息发布及农产品生产技术交流相关网站'),
(173, '工业', 16, '建筑、金属、机械、制造等行业专业论坛及网站'),
(174, '法律', 16, '法律机构及法律知识相关论坛及网站'),
(175, '营销管理', 16, '市场营销类相关论坛及网站'),
(176, '园艺学', 16, '园艺类专业网站'),
(177, '彩票', 17, '各类彩票机构自有网站'),
(178, '公益', 17, '公益类组织及媒体信息发布相关网站'),
(179, '广告', 18, '提供广告图片或相关内容的网站，或者以营销为目的的相关网站'),
(180, '成人', 18, '限制及或色情相关网站'),
(181, '赌博', 18, '赌博相关网站'),
(182, '恶意网站', 18, '对用户计算机、移动设备有危害的恶意网站'),
(183, '暴力反动', 18, '包含法律禁止的暴力反动内容的违法网站'),
(184, '其他', 18, '其他网站');