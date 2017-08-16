/*
Navicat MySQL Data Transfer

Source Server         : ly
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : taobao

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2017-08-16 22:24:07
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('1', 'pcConsole');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('1', '1', '37');
INSERT INTO `auth_group_permissions` VALUES ('2', '1', '38');
INSERT INTO `auth_group_permissions` VALUES ('3', '1', '39');

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add cart', '7', 'add_cart');
INSERT INTO `auth_permission` VALUES ('20', 'Can change cart', '7', 'change_cart');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete cart', '7', 'delete_cart');
INSERT INTO `auth_permission` VALUES ('22', 'Can add item', '8', 'add_item');
INSERT INTO `auth_permission` VALUES ('23', 'Can change item', '8', 'change_item');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete item', '8', 'delete_item');
INSERT INTO `auth_permission` VALUES ('25', 'Can add user', '9', 'add_user');
INSERT INTO `auth_permission` VALUES ('26', 'Can change user', '9', 'change_user');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete user', '9', 'delete_user');
INSERT INTO `auth_permission` VALUES ('28', 'Can add goods', '10', 'add_goods');
INSERT INTO `auth_permission` VALUES ('29', 'Can change goods', '10', 'change_goods');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete goods', '10', 'delete_goods');
INSERT INTO `auth_permission` VALUES ('31', 'Can add cart item', '11', 'add_cartitem');
INSERT INTO `auth_permission` VALUES ('32', 'Can change cart item', '11', 'change_cartitem');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete cart item', '11', 'delete_cartitem');
INSERT INTO `auth_permission` VALUES ('34', 'Can add user_cart', '12', 'add_user_cart');
INSERT INTO `auth_permission` VALUES ('35', 'Can change user_cart', '12', 'change_user_cart');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete user_cart', '12', 'delete_user_cart');
INSERT INTO `auth_permission` VALUES ('37', 'Can add pc list', '13', 'add_pclist');
INSERT INTO `auth_permission` VALUES ('38', 'Can change pc list', '13', 'change_pclist');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete pc list', '13', 'delete_pclist');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$ZWu4sUQ8OpD8$x0BsEnLXMy8/ndSD1wL2btxrRndUfEYVXvOAJlGZrB0=', '2017-08-12 12:04:41.798268', '1', 'root', '', '', '457868671@qq.com', '1', '1', '2017-07-21 11:45:12.104700');
INSERT INTO `auth_user` VALUES ('8', 'pbkdf2_sha256$36000$yA9CPFtXqNKb$0GK47KrdOaYPnci627H+DO5CQIByVshrS/IaUAluZkw=', '2017-08-09 08:00:40.618845', '0', '13638423531', '', '', '', '0', '1', '2017-08-03 16:22:54.146368');
INSERT INTO `auth_user` VALUES ('9', 'pbkdf2_sha256$36000$sqYnDn6YZ8eL$FMeQ8ZmsLYmgpfBjwggBLxcpc7GYgdmqH5+847J0DGw=', '2017-08-09 09:06:18.725522', '0', '18390206838', '', '', '', '0', '1', '2017-08-06 13:55:07.029328');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES ('1', '9', '1');

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for cart_cart
-- ----------------------------
DROP TABLE IF EXISTS `cart_cart`;
CREATE TABLE `cart_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creation_date` datetime(6) NOT NULL,
  `checked_out` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cart_cart
-- ----------------------------

-- ----------------------------
-- Table structure for cart_item
-- ----------------------------
DROP TABLE IF EXISTS `cart_item`;
CREATE TABLE `cart_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(10) unsigned NOT NULL,
  `unit_price` decimal(18,2) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  `cart_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_item_cart_id_157ecf5f_fk_cart_cart_id` (`cart_id`),
  KEY `cart_item_content_type_id_5737916f_fk_django_content_type_id` (`content_type_id`),
  CONSTRAINT `cart_item_cart_id_157ecf5f_fk_cart_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `cart_cart` (`id`),
  CONSTRAINT `cart_item_content_type_id_5737916f_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cart_item
-- ----------------------------

-- ----------------------------
-- Table structure for crawlerconsole_pclist
-- ----------------------------
DROP TABLE IF EXISTS `crawlerconsole_pclist`;
CREATE TABLE `crawlerconsole_pclist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `processName` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `host` varchar(20) NOT NULL,
  `path` varchar(255) NOT NULL,
  `logpath` varchar(256) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crawlerconsole_pclist
-- ----------------------------
INSERT INTO `crawlerconsole_pclist` VALUES ('1', 'suning', '苏宁', '127.0.0.1', '/static/sn/suning_BaseInfo.py', '/', '0');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('7', 'cart', 'cart');
INSERT INTO `django_content_type` VALUES ('8', 'cart', 'item');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('13', 'crawlerConsole', 'pclist');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('11', 'taobao', 'cartitem');
INSERT INTO `django_content_type` VALUES ('10', 'taobao', 'goods');
INSERT INTO `django_content_type` VALUES ('9', 'taobao', 'user');
INSERT INTO `django_content_type` VALUES ('12', 'taobao', 'user_cart');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-07-21 05:58:57.215456');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2017-07-21 05:59:25.353650');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2017-07-21 05:59:50.489704');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2017-07-21 05:59:50.572746');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2017-07-21 05:59:53.174635');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2017-07-21 05:59:54.699723');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2017-07-21 05:59:56.300874');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2017-07-21 05:59:56.396010');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2017-07-21 05:59:57.576874');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2017-07-21 05:59:57.639919');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2017-07-21 05:59:57.718988');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2017-07-21 05:59:59.478229');
INSERT INTO `django_migrations` VALUES ('13', 'cart', '0001_initial', '2017-07-21 06:00:08.068342');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2017-07-21 06:00:10.195856');
INSERT INTO `django_migrations` VALUES ('15', 'taobao', '0001_initial', '2017-07-21 06:00:17.637196');
INSERT INTO `django_migrations` VALUES ('16', 'taobao', '0002_goods', '2017-07-21 06:00:21.074636');
INSERT INTO `django_migrations` VALUES ('17', 'taobao', '0003_goods_goods_introduce', '2017-07-21 06:00:22.416597');
INSERT INTO `django_migrations` VALUES ('18', 'taobao', '0004_goods_goods_name', '2017-07-21 06:00:23.665509');
INSERT INTO `django_migrations` VALUES ('19', 'taobao', '0005_cartid_cartitem', '2017-07-21 06:00:25.072483');
INSERT INTO `django_migrations` VALUES ('20', 'taobao', '0006_auto_20170622_2153', '2017-07-21 06:00:27.794528');
INSERT INTO `django_migrations` VALUES ('21', 'taobao', '0007_auto_20170622_2156', '2017-07-21 06:00:29.896996');
INSERT INTO `django_migrations` VALUES ('22', 'taobao', '0008_delete_cartitem', '2017-07-21 06:00:30.260254');
INSERT INTO `django_migrations` VALUES ('23', 'taobao', '0009_cartitem', '2017-07-21 06:00:30.981769');
INSERT INTO `django_migrations` VALUES ('24', 'taobao', '0010_cartitem_sum', '2017-07-21 06:00:32.381764');
INSERT INTO `django_migrations` VALUES ('25', 'taobao', '0011_auto_20170623_1631', '2017-07-21 06:00:33.837801');
INSERT INTO `django_migrations` VALUES ('26', 'taobao', '0012_auto_20170721_2057', '2017-07-21 12:57:31.078965');
INSERT INTO `django_migrations` VALUES ('27', 'taobao', '0013_auto_20170728_1820', '2017-07-28 10:45:19.302058');
INSERT INTO `django_migrations` VALUES ('28', 'taobao', '0014_auto_20170728_1823', '2017-07-28 10:45:20.823693');
INSERT INTO `django_migrations` VALUES ('29', 'taobao', '0015_auto_20170728_1831', '2017-07-28 10:45:23.264384');
INSERT INTO `django_migrations` VALUES ('30', 'taobao', '0016_auto_20170728_1850', '2017-07-28 10:50:08.680585');
INSERT INTO `django_migrations` VALUES ('31', 'crawlerConsole', '0001_initial', '2017-08-06 13:46:00.448970');
INSERT INTO `django_migrations` VALUES ('32', 'crawlerConsole', '0002_auto_20170807_1413', '2017-08-07 06:14:00.830596');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0obwd2jkwssmkqg79vze0oxfk4g25ezg', 'YWNiZDhhNWVjYWI1ODBjY2JmZTc3NDBiMjY4NmYwYjM0ODEwOTZhODp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZWFiMjA1MmZjYjU4MjNlZDFiZmE4OGUyYWQwMjg0YTYzOWViMmRjIiwidXNlcm5hbWUiOiIxODM5MDIwNjgzOCJ9', '2017-08-20 16:30:31.914907');
INSERT INTO `django_session` VALUES ('3wa5zvy2ezu3rlywycy1b5t3n8nddav4', 'ZGE4NGI3MDAzNDAzYTgwZDA2NDNlZmM0YTZlNTE1NDRlZDM1MTg2OTp7InVzZXJuYW1lIjoiMTM2Mzg0MjM1MzEifQ==', '2017-08-04 09:44:41.371461');
INSERT INTO `django_session` VALUES ('7b0secynaukou0hbkvrl0oihux7x3tuc', 'ZWFiYWFkZjBhN2QxMzhjZmM4YzVkYzdmMGM4NjI1ODhmYjJhZmNmOTp7InVzZXJuYW1lIjoiMTgzOTAyMDY4MzgiLCJfYXV0aF91c2VyX2lkIjoiNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmU2YTgyODNlMzlhN2YyYzUzMjU0MGM3OTJlNzg5YTY1MGViYWE1MSJ9', '2017-08-07 11:40:16.057124');
INSERT INTO `django_session` VALUES ('9823dnm508md8qen814fwkl33eawco50', 'YWNiZDhhNWVjYWI1ODBjY2JmZTc3NDBiMjY4NmYwYjM0ODEwOTZhODp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZWFiMjA1MmZjYjU4MjNlZDFiZmE4OGUyYWQwMjg0YTYzOWViMmRjIiwidXNlcm5hbWUiOiIxODM5MDIwNjgzOCJ9', '2017-08-22 07:29:27.615043');
INSERT INTO `django_session` VALUES ('a3ori75btybaox1yzcl7zhcjsh3ptm6b', 'Yzk5OWUzNjlhZjZkMDgxYTA1NTVjNjViZjc1YmI0YzJiNzI0YzU2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NzI2MGQwZmZhNTczMDU3Y2IyNWNmZTQ5MTFiZTIxMzhjMTNkNmFkIn0=', '2017-08-26 12:04:42.067459');
INSERT INTO `django_session` VALUES ('diiolfx1n60oudiq6eevstuhcmbsipy5', 'OTllZjNiOGJiNDFmZmRmNWUwYmQwNDJhOWYyNTA2YjJiYzNmMGRhZjp7fQ==', '2017-08-17 12:54:56.972203');
INSERT INTO `django_session` VALUES ('eoy6xlnjahnncrqd36oeg2y0imt0l1mg', 'OTllZjNiOGJiNDFmZmRmNWUwYmQwNDJhOWYyNTA2YjJiYzNmMGRhZjp7fQ==', '2017-08-11 11:13:38.840389');
INSERT INTO `django_session` VALUES ('f4xyy4rb9mcceil8syzlnmi5bqwjb3ph', 'OTllZjNiOGJiNDFmZmRmNWUwYmQwNDJhOWYyNTA2YjJiYzNmMGRhZjp7fQ==', '2017-08-11 11:11:17.703158');
INSERT INTO `django_session` VALUES ('inxhna91kppipbitiws4p076d24gfnrg', 'YWNiZDhhNWVjYWI1ODBjY2JmZTc3NDBiMjY4NmYwYjM0ODEwOTZhODp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZWFiMjA1MmZjYjU4MjNlZDFiZmE4OGUyYWQwMjg0YTYzOWViMmRjIiwidXNlcm5hbWUiOiIxODM5MDIwNjgzOCJ9', '2017-08-22 03:46:29.806318');
INSERT INTO `django_session` VALUES ('n8v2871tmrf5nts2xwo4vdnl13iqdbdn', 'YWNiZDhhNWVjYWI1ODBjY2JmZTc3NDBiMjY4NmYwYjM0ODEwOTZhODp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZWFiMjA1MmZjYjU4MjNlZDFiZmE4OGUyYWQwMjg0YTYzOWViMmRjIiwidXNlcm5hbWUiOiIxODM5MDIwNjgzOCJ9', '2017-08-21 11:04:23.751700');
INSERT INTO `django_session` VALUES ('yxlkyeqo63o8eq7zg9da41ulnuvwaaj3', 'YWNiZDhhNWVjYWI1ODBjY2JmZTc3NDBiMjY4NmYwYjM0ODEwOTZhODp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZWFiMjA1MmZjYjU4MjNlZDFiZmE4OGUyYWQwMjg0YTYzOWViMmRjIiwidXNlcm5hbWUiOiIxODM5MDIwNjgzOCJ9', '2017-08-23 09:06:18.936047');
INSERT INTO `django_session` VALUES ('z61kkt0ijbjg2fwz1vf5pmc8qksbl4yy', 'NmY4NWViY2ViZjU2OWRlYWQyMjMyNGUwOTM4OWQ0OWZkZGIxYzNkMDp7Il9hdXRoX3VzZXJfaWQiOiI2IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NDk1ZWUxODgxYjRlNDc0OThlNDkzYjYxMTk2MmUzMzlmZTIwOTE5IiwidXNlcm5hbWUiOiIxMzYzODQyMzUzMSJ9', '2017-08-12 09:26:49.332552');
INSERT INTO `django_session` VALUES ('z8xc4kq0o82jbixgaqv5vo0pqr8tswu7', 'Yzk5OWUzNjlhZjZkMDgxYTA1NTVjNjViZjc1YmI0YzJiNzI0YzU2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NzI2MGQwZmZhNTczMDU3Y2IyNWNmZTQ5MTFiZTIxMzhjMTNkNmFkIn0=', '2017-08-09 14:22:42.345769');

-- ----------------------------
-- Table structure for taobao_cartitem
-- ----------------------------
DROP TABLE IF EXISTS `taobao_cartitem`;
CREATE TABLE `taobao_cartitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantuty` int(11) NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `username` varchar(50) NOT NULL,
  `sum` decimal(10,2) NOT NULL,
  `goods_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `taobao_cartitem_goods_id_054418b5_fk_taobao_goods_id` (`goods_id`),
  CONSTRAINT `taobao_cartitem_goods_id_054418b5_fk_taobao_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `taobao_goods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of taobao_cartitem
-- ----------------------------
INSERT INTO `taobao_cartitem` VALUES ('6', '1', '498.00', '13638423531', '498.00', '6');
INSERT INTO `taobao_cartitem` VALUES ('8', '1', '138.00', '18390206838', '138.00', '5');
INSERT INTO `taobao_cartitem` VALUES ('9', '1', '249.00', '13638423531', '249.00', '2');

-- ----------------------------
-- Table structure for taobao_goods
-- ----------------------------
DROP TABLE IF EXISTS `taobao_goods`;
CREATE TABLE `taobao_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` int(11) NOT NULL,
  `goods_id` varchar(10) NOT NULL,
  `goods_price` decimal(10,2) NOT NULL,
  `goods_Stock` int(11) NOT NULL DEFAULT '100',
  `sales_Volume` int(11) NOT NULL DEFAULT '0',
  `goods_introduce` varchar(250) NOT NULL,
  `goods_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of taobao_goods
-- ----------------------------
INSERT INTO `taobao_goods` VALUES ('1', '1', '33428', '45.00', '100', '0', ' 音乐和茶 伴你左右 ', ' 岷江音乐 三角调配茶包 8枚');
INSERT INTO `taobao_goods` VALUES ('2', '1', '33431', '249.00', '100', '0', ' 沙冰或沙拉 它都能搞定 ', ' 【预售】榨冰+沙拉一体机');
INSERT INTO `taobao_goods` VALUES ('3', '1', '32755', '299.00', '100', '0', ' 橄榄油奥斯卡得主 ', ' 特级初榨橄榄油 500ml 8色可选，2种口味，意大利纯手工制罐，古法压榨油');
INSERT INTO `taobao_goods` VALUES ('4', '1', '31226', '39.00', '100', '0', ' 美观实用合二为一 ', ' Ball Mason Jar 梅森罐 玻璃密封罐 蔬菜沙拉罐 12oz水晶杯 360ml');
INSERT INTO `taobao_goods` VALUES ('5', '1', '33411', '138.00', '100', '0', ' 手工上色 匠心之作 ', ' 土耳其手工玻璃贝壳盘 2件套');
INSERT INTO `taobao_goods` VALUES ('6', '1', '32998', '498.00', '100', '0', ' 营养果汁 随时打包 ', ' 梅森瓶蔬果榨汁机 含两个梅森瓶');
INSERT INTO `taobao_goods` VALUES ('7', '1', '33409', '169.00', '100', '0', ' 把海洋搬到餐桌上 ', ' 土耳其手工璃鱼盘 3件套');
INSERT INTO `taobao_goods` VALUES ('8', '1', '33416', '58.00', '100', '0', ' 每天都多一份小确幸 ', ' 小确幸调味花果茶 泡袋茶 9枚装');
INSERT INTO `taobao_goods` VALUES ('9', '1', '29735', '35.00', '100', '0', '', '朝夕家品 陶瓷杯碟套装');
INSERT INTO `taobao_goods` VALUES ('10', '1', '28858', '479.00', '100', '0', ' 告别单调厨房 ', ' DANSK Kobenstyle 珐琅搪瓷单柄汤锅 2.2L   ');
INSERT INTO `taobao_goods` VALUES ('11', '1', '33429', '218.00', '100', '0', ' 饮下斯里兰卡的风情 ', ' 斯里兰卡花果调配茶红茶礼盒');
INSERT INTO `taobao_goods` VALUES ('12', '1', '32853', '326.00', '100', '0', ' 新鲜果汁随身带 ', ' 便携原汁果汁机 600ml');
INSERT INTO `taobao_goods` VALUES ('13', '1', '31221', '69.00', '100', '0', ' 玻璃瓶中爱马仕 ', ' Ball Mason Jar 玻璃密封罐/梅森瓶 蓝色宽口elite 32oz 947ml ');
INSERT INTO `taobao_goods` VALUES ('14', '1', '22335', '139.00', '100', '0', ' 9s极细研磨 ', ' 电动咖啡磨豆机 干湿两用 粗细可调 ');
INSERT INTO `taobao_goods` VALUES ('15', '1', '23687', '199.00', '100', '0', ' 古朴自然 ', ' 不石之作咖啡杯2套装 杯+底碟+勺');
INSERT INTO `taobao_goods` VALUES ('16', '1', '26855', '29.00', '100', '0', ' 静享午后时光 ', ' cork 茶杯200ml');
INSERT INTO `taobao_goods` VALUES ('17', '1', '17029', '99.00', '100', '0', ' 餐桌上的自然界 ', ' MIA系列俏皮豆荚餐具4件套 手握更舒适');
INSERT INTO `taobao_goods` VALUES ('18', '1', '31224', '35.00', '100', '0', ' 玻璃罐中的爱马仕 ', ' Ball Mason Jar 梅森罐 玻璃密封罐 蔬菜沙拉罐  8oz水晶杯 240ml');
INSERT INTO `taobao_goods` VALUES ('19', '1', '27936', '198.00', '100', '0', ' 不插电的&quot;电饭锅&quot; ', ' 熊本熊不锈钢焖烧罐 700ml ');
INSERT INTO `taobao_goods` VALUES ('20', '1', '33415', '49.00', '100', '0', ' 口腔里的香气盛宴 ', ' 调配茶包袱礼盒 7袋装');
INSERT INTO `taobao_goods` VALUES ('41', '2', '33446', '295.00', '100', '0', ' 戒指项链你随便挂 ', ' 万宝鹿首饰架');
INSERT INTO `taobao_goods` VALUES ('42', '2', '33391', '219.00', '100', '0', ' 柔软舒适像朵云 ', ' 可爱系全棉精梳床笠四件套');
INSERT INTO `taobao_goods` VALUES ('43', '2', '33350', '168.00', '100', '0', ' 柔软凉爽 好舒服 ', ' 日式条纹水洗纱毛巾被150*200cm');
INSERT INTO `taobao_goods` VALUES ('44', '2', '33373', '138.00', '100', '0', ' 每天妆容 好看10倍 ', ' 对面 磁力补光化妆镜 准确化妆不尴尬 高清护肤无死角');
INSERT INTO `taobao_goods` VALUES ('45', '2', '33088', '298.00', '100', '0', ' 光随你动 夜晚不再害怕 ', ' MINI+ 旗舰版智能光瓶');
INSERT INTO `taobao_goods` VALUES ('46', '2', '33356', '319.00', '100', '0', ' 如丝爽滑 可直接机洗 ', ' 高支精梳全棉缎纹夏凉被	200×230cm');
INSERT INTO `taobao_goods` VALUES ('47', '2', '31979', '268.00', '100', '0', ' 舒适材质助睡眠 ', ' VanillaButterfly 淡淡青春系列精梳棉四件套 萌宠熊宝 200*230cm');
INSERT INTO `taobao_goods` VALUES ('48', '2', '33365', '428.00', '100', '0', ' 哄着你安稳入睡 ', ' 蜗牛睡眠智能助眠枕');
INSERT INTO `taobao_goods` VALUES ('49', '2', '33355', '129.00', '100', '0', ' 柔软亲肤 可直接机洗 ', ' 小格点 全棉舒柔夏凉被150×210cm');
INSERT INTO `taobao_goods` VALUES ('50', '2', '26593', '208.00', '100', '0', ' 北欧简约装点爱巢 ', ' 北欧风小树印花四件套');
INSERT INTO `taobao_goods` VALUES ('51', '2', '29476', '39.00', '100', '0', ' 家居不再单调 ', ' 范店 水彩绿色植物系列靠垫  ');
INSERT INTO `taobao_goods` VALUES ('52', '2', '33451', '829.00', '100', '0', ' 好运不断 喜事登门 ', ' 18k金镶登喜鹿摆件');
INSERT INTO `taobao_goods` VALUES ('53', '2', '25214', '158.00', '100', '0', ' 吸水又快又透气 ', ' 桃皮绒抹胸浴裙');
INSERT INTO `taobao_goods` VALUES ('54', '2', '33449', '365.00', '100', '0', ' 放慢节奏 一起深呼吸 ', ' 立马桃花开无火香薰');
INSERT INTO `taobao_goods` VALUES ('55', '2', '31890', '39.00', '100', '0', ' 让家充满朝气 ', ' 田园童话吸水门垫');
INSERT INTO `taobao_goods` VALUES ('56', '2', '26456', '189.00', '100', '0', ' 完美妆容神助攻 ', ' LED化妆镜 ');
INSERT INTO `taobao_goods` VALUES ('57', '2', '33522', '198.00', '100', '0', ' 夜晚给你安全感 ', ' MINI 经典版智能光瓶');
INSERT INTO `taobao_goods` VALUES ('58', '2', '25938', '39.00', '100', '0', ' 生活本应如此惊喜 ', ' 柔雅软木底花瓶');
INSERT INTO `taobao_goods` VALUES ('59', '2', '33060', '128.00', '100', '0', ' 萌到不忍心撒手 ', ' 森林室友系列弹力抱枕');
INSERT INTO `taobao_goods` VALUES ('60', '2', '23986', '298.00', '100', '0', ' 记录孩子成长 ', ' 儿童成长记录时光机');

-- ----------------------------
-- Table structure for taobao_user_cart
-- ----------------------------
DROP TABLE IF EXISTS `taobao_user_cart`;
CREATE TABLE `taobao_user_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `total` int(11) NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of taobao_user_cart
-- ----------------------------
INSERT INTO `taobao_user_cart` VALUES ('1', '13638423531', '747', '2');
INSERT INTO `taobao_user_cart` VALUES ('2', '18390206838', '138', '1');
