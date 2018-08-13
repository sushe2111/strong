CREATE DATABASE IF NOT EXISTS `starmmo_wjs` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; 

CREATE TABLE IF NOT EXISTS `starmmo_wjs`.`tbl_account` (
  `uid` bigint(20) unsigned NOT NULL COMMENT '账号id',
  `uname` varchar(200) COLLATE utf8_bin NOT NULL COMMENT '账号名',
  `createTime` int(10) unsigned NOT NULL COMMENT '账号创建时间',
  `channel` varchar(200) COLLATE utf8_bin NOT NULL COMMENT '渠道',
  `dev` varchar(200) COLLATE utf8_bin NOT NULL COMMENT '设备id',
  `openId` varchar(200) COLLATE utf8_bin NOT NULL COMMENT 'openid',
  `cbtFbState` int(10) NOT NULL DEFAULT '0' COMMENT '0:尚未初始化(还不知道是不是fb账号) 1:Fb账号尚未初始化 2:Fb账号处理完成 3:处理失败 4:非fb账号',
  `fbuid_2017` varchar(20) COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '2017年测试时,本账号的uid',
  `fbuid_cbt` varchar(20) COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT 'cbt测试时,本账号的facebook uid'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
