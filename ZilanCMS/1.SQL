/*********/
/*       */
/* 1.SQL */
/*       */
/*********/

/* Disable Foreign Keys */
pragma foreign_keys = off;
/* Begin Transaction */
begin transaction;

/* Drop table [main].[auth_group] */
drop table if exists [main].[auth_group];

/* Table structure [main].[auth_group] */
CREATE TABLE [main].[auth_group] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [name] varchar(150) NOT NULL UNIQUE);

/* Data [main].[auth_group] */


/* Drop table [main].[django_content_type] */
drop table if exists [main].[django_content_type];

/* Table structure [main].[django_content_type] */
CREATE TABLE [main].[django_content_type] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [app_label] varchar(100) NOT NULL, 
  [model] varchar(100) NOT NULL);
CREATE UNIQUE INDEX [main].[django_content_type_app_label_model_76bd3d3b_uniq] ON [django_content_type] ([app_label], [model]);

/* Data [main].[django_content_type] */
insert into [main].[django_content_type] values(1, 'admin', 'logentry');
insert into [main].[django_content_type] values(2, 'auth', 'permission');
insert into [main].[django_content_type] values(3, 'auth', 'group');
insert into [main].[django_content_type] values(4, 'contenttypes', 'contenttype');
insert into [main].[django_content_type] values(5, 'sessions', 'session');
insert into [main].[django_content_type] values(6, 'ZilanCMS', 'filetype');
insert into [main].[django_content_type] values(7, 'ZilanCMS', 'alluser');
insert into [main].[django_content_type] values(8, 'ZilanCMS', 'uploadwork');
insert into [main].[django_content_type] values(9, 'CarnivalApoint', 'activity');
insert into [main].[django_content_type] values(10, 'CarnivalApoint', 'apointmess');


/* Drop table [main].[auth_permission] */
drop table if exists [main].[auth_permission];

/* Table structure [main].[auth_permission] */
CREATE TABLE [main].[auth_permission] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [content_type_id] integer NOT NULL REFERENCES [django_content_type]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [codename] varchar(100) NOT NULL, 
  [name] varchar(255) NOT NULL);
CREATE INDEX [main].[auth_permission_content_type_id_2f476e4b] ON [auth_permission] ([content_type_id]);
CREATE UNIQUE INDEX [main].[auth_permission_content_type_id_codename_01ab375a_uniq] ON [auth_permission] ([content_type_id], [codename]);

/* Data [main].[auth_permission] */
insert into [main].[auth_permission] values(1, 1, 'add_logentry', 'Can add log entry');
insert into [main].[auth_permission] values(2, 1, 'change_logentry', 'Can change log entry');
insert into [main].[auth_permission] values(3, 1, 'delete_logentry', 'Can delete log entry');
insert into [main].[auth_permission] values(4, 1, 'view_logentry', 'Can view log entry');
insert into [main].[auth_permission] values(5, 2, 'add_permission', 'Can add permission');
insert into [main].[auth_permission] values(6, 2, 'change_permission', 'Can change permission');
insert into [main].[auth_permission] values(7, 2, 'delete_permission', 'Can delete permission');
insert into [main].[auth_permission] values(8, 2, 'view_permission', 'Can view permission');
insert into [main].[auth_permission] values(9, 3, 'add_group', 'Can add group');
insert into [main].[auth_permission] values(10, 3, 'change_group', 'Can change group');
insert into [main].[auth_permission] values(11, 3, 'delete_group', 'Can delete group');
insert into [main].[auth_permission] values(12, 3, 'view_group', 'Can view group');
insert into [main].[auth_permission] values(13, 4, 'add_contenttype', 'Can add content type');
insert into [main].[auth_permission] values(14, 4, 'change_contenttype', 'Can change content type');
insert into [main].[auth_permission] values(15, 4, 'delete_contenttype', 'Can delete content type');
insert into [main].[auth_permission] values(16, 4, 'view_contenttype', 'Can view content type');
insert into [main].[auth_permission] values(17, 5, 'add_session', 'Can add session');
insert into [main].[auth_permission] values(18, 5, 'change_session', 'Can change session');
insert into [main].[auth_permission] values(19, 5, 'delete_session', 'Can delete session');
insert into [main].[auth_permission] values(20, 5, 'view_session', 'Can view session');
insert into [main].[auth_permission] values(21, 6, 'add_filetype', 'Can add file type');
insert into [main].[auth_permission] values(22, 6, 'change_filetype', 'Can change file type');
insert into [main].[auth_permission] values(23, 6, 'delete_filetype', 'Can delete file type');
insert into [main].[auth_permission] values(24, 6, 'view_filetype', 'Can view file type');
insert into [main].[auth_permission] values(25, 7, 'add_alluser', 'Can add all user');
insert into [main].[auth_permission] values(26, 7, 'change_alluser', 'Can change all user');
insert into [main].[auth_permission] values(27, 7, 'delete_alluser', 'Can delete all user');
insert into [main].[auth_permission] values(28, 7, 'view_alluser', 'Can view all user');
insert into [main].[auth_permission] values(29, 8, 'add_uploadwork', 'Can add upload work');
insert into [main].[auth_permission] values(30, 8, 'change_uploadwork', 'Can change upload work');
insert into [main].[auth_permission] values(31, 8, 'delete_uploadwork', 'Can delete upload work');
insert into [main].[auth_permission] values(32, 8, 'view_uploadwork', 'Can view upload work');
insert into [main].[auth_permission] values(33, 9, 'add_activity', 'Can add activity');
insert into [main].[auth_permission] values(34, 9, 'change_activity', 'Can change activity');
insert into [main].[auth_permission] values(35, 9, 'delete_activity', 'Can delete activity');
insert into [main].[auth_permission] values(36, 9, 'view_activity', 'Can view activity');
insert into [main].[auth_permission] values(37, 10, 'add_apointmess', 'Can add apoint mess');
insert into [main].[auth_permission] values(38, 10, 'change_apointmess', 'Can change apoint mess');
insert into [main].[auth_permission] values(39, 10, 'delete_apointmess', 'Can delete apoint mess');
insert into [main].[auth_permission] values(40, 10, 'view_apointmess', 'Can view apoint mess');


/* Drop table [main].[auth_group_permissions] */
drop table if exists [main].[auth_group_permissions];

/* Table structure [main].[auth_group_permissions] */
CREATE TABLE [main].[auth_group_permissions] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [group_id] integer NOT NULL REFERENCES [auth_group]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [permission_id] integer NOT NULL REFERENCES [auth_permission]([id]) DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX [main].[auth_group_permissions_group_id_b120cbf9] ON [auth_group_permissions] ([group_id]);
CREATE UNIQUE INDEX [main].[auth_group_permissions_group_id_permission_id_0cd325b0_uniq] ON [auth_group_permissions] ([group_id], [permission_id]);
CREATE INDEX [main].[auth_group_permissions_permission_id_84c5c92e] ON [auth_group_permissions] ([permission_id]);

/* Data [main].[auth_group_permissions] */


/* Drop table [main].[CarnivalApoint_activity] */
drop table if exists [main].[CarnivalApoint_activity];

/* Table structure [main].[CarnivalApoint_activity] */
CREATE TABLE [main].[CarnivalApoint_activity] (
  [aid] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [name] varchar(100) NOT NULL, 
  [address] varchar(200) NOT NULL, 
  [max_user] [smallint unsigned] NOT NULL, 
  [start_time] datetime, 
  [end_time] datetime, 
  CHECK("max_user" >= 0));

/* Data [main].[CarnivalApoint_activity] */


/* Drop table [main].[CarnivalApoint_apointmess] */
drop table if exists [main].[CarnivalApoint_apointmess];

/* Table structure [main].[CarnivalApoint_apointmess] */
CREATE TABLE [main].[CarnivalApoint_apointmess] (
  [uid] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [name] varchar(11) NOT NULL, 
  [age] [smallint unsigned] NOT NULL, 
  [id_no] varchar(20) NOT NULL, 
  [is_female] bool NOT NULL, 
  [phone] varchar(11) NOT NULL, 
  [is_child] bool NOT NULL, 
  [create_time] datetime NOT NULL, 
  [activity_id] integer NOT NULL REFERENCES [CarnivalApoint_activity]([aid]) DEFERRABLE INITIALLY DEFERRED, 
  [parent_id_id] integer REFERENCES [CarnivalApoint_apointmess]([uid]) DEFERRABLE INITIALLY DEFERRED, 
  CHECK("age" >= 0));
CREATE INDEX [main].[CarnivalApoint_apointmess_activity_id_e9d8cfc2] ON [CarnivalApoint_apointmess] ([activity_id]);
CREATE INDEX [main].[CarnivalApoint_apointmess_parent_id_id_16f15b49] ON [CarnivalApoint_apointmess] ([parent_id_id]);

/* Data [main].[CarnivalApoint_apointmess] */


/* Drop table [main].[Dis_alluser] */
drop table if exists [main].[Dis_alluser];

/* Table structure [main].[Dis_alluser] */
CREATE TABLE [main].[Dis_alluser] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [password] varchar(128) NOT NULL, 
  [last_login] datetime, 
  [is_superuser] bool NOT NULL, 
  [username] varchar(150) NOT NULL UNIQUE, 
  [first_name] varchar(30) NOT NULL, 
  [last_name] varchar(150) NOT NULL, 
  [email] varchar(254) NOT NULL, 
  [is_staff] bool NOT NULL, 
  [is_active] bool NOT NULL, 
  [date_joined] datetime NOT NULL, 
  [phone] varchar(11) UNIQUE, 
  [nickname] varchar(20), 
  [shot] varchar(300), 
  [is_expand] bool NOT NULL, 
  [is_pay] bool NOT NULL, 
  [is_disuser] bool NOT NULL);

/* Data [main].[Dis_alluser] */
insert into [main].[Dis_alluser] values(1, 'pbkdf2_sha256$180000$JVR2AizHZIyV$pvzR/53SmtAVBTXoiR7yCKH6YLgqWb7lByBPiibbJK4=', '2020-02-25 00:07:01.773', 0, 'admin', '', '', 'admin1@admin.com', 0, 1, '2020-02-13 17:51:51.937', null, null, null, 0, 0, 0);
insert into [main].[Dis_alluser] values(2, 'pbkdf2_sha256$180000$YmpPJ1THAz6t$CdbzL/e/W6p/kOgdRj7PEN0frbKUJ9nWfu1zZrZDnoY=', '2020-02-13 17:55:16.655', 0, 'admin5', '', '', 'admin1@admin.com', 0, 1, '2020-02-13 17:55:16.428', '1231182818', '3344', null, 0, 0, 0);
insert into [main].[Dis_alluser] values(3, 'sharif0115', null, 0, 'admin2', '', '', '', 0, 1, '2020-02-24 15:47:22.684', '12312312312', '2', null, 0, 0, 1);
insert into [main].[Dis_alluser] values(4, 'pbkdf2_sha256$180000$RurRF3hKau4W$CgJEhfSnjR/Ct5yAHFbaO5ppG3bNBZQb362eob0WWGs=', '2020-02-24 21:40:19.140', 0, 'guest', '', '', 'guest@guest.com', 0, 1, '2020-02-24 21:35:06.579', '13654328765', null, null, 0, 0, 1);
insert into [main].[Dis_alluser] values(7, 'pbkdf2_sha256$180000$ckSi1CgVQLpX$/FdrlKNNZCIBIaz1ii4tS1szmylkMtCy3i5jN4F+RRM=', '2020-02-24 23:35:33.353', 0, 'guest1', '', '', '', 0, 1, '2020-02-24 23:35:21.076', null, 'guest', null, 0, 0, 1);


/* Drop table [main].[Dis_alluser_groups] */
drop table if exists [main].[Dis_alluser_groups];

/* Table structure [main].[Dis_alluser_groups] */
CREATE TABLE [main].[Dis_alluser_groups] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [alluser_id] integer NOT NULL REFERENCES [Dis_alluser]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [group_id] integer NOT NULL REFERENCES [auth_group]([id]) DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX [main].[Dis_alluser_groups_alluser_id_8c4d4825] ON [Dis_alluser_groups] ([alluser_id]);
CREATE UNIQUE INDEX [main].[Dis_alluser_groups_alluser_id_group_id_198cb3e2_uniq] ON [Dis_alluser_groups] ([alluser_id], [group_id]);
CREATE INDEX [main].[Dis_alluser_groups_group_id_c6a5f964] ON [Dis_alluser_groups] ([group_id]);

/* Data [main].[Dis_alluser_groups] */


/* Drop table [main].[Dis_alluser_user_permissions] */
drop table if exists [main].[Dis_alluser_user_permissions];

/* Table structure [main].[Dis_alluser_user_permissions] */
CREATE TABLE [main].[Dis_alluser_user_permissions] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [alluser_id] integer NOT NULL REFERENCES [Dis_alluser]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [permission_id] integer NOT NULL REFERENCES [auth_permission]([id]) DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX [main].[Dis_alluser_user_permissions_alluser_id_627df990] ON [Dis_alluser_user_permissions] ([alluser_id]);
CREATE UNIQUE INDEX [main].[Dis_alluser_user_permissions_alluser_id_permission_id_ec621e8c_uniq] ON [Dis_alluser_user_permissions] ([alluser_id], [permission_id]);
CREATE INDEX [main].[Dis_alluser_user_permissions_permission_id_72ed7f80] ON [Dis_alluser_user_permissions] ([permission_id]);

/* Data [main].[Dis_alluser_user_permissions] */


/* Drop table [main].[Dis_filetype] */
drop table if exists [main].[Dis_filetype];

/* Table structure [main].[Dis_filetype] */
CREATE TABLE [main].[Dis_filetype] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [typename] varchar(100) NOT NULL);

/* Data [main].[Dis_filetype] */
insert into [main].[Dis_filetype] values(1, 'Python');
insert into [main].[Dis_filetype] values(2, 'C+1');
insert into [main].[Dis_filetype] values(3, 'B');
insert into [main].[Dis_filetype] values(4, 'C++');


/* Drop table [main].[Dis_uploadwork] */
drop table if exists [main].[Dis_uploadwork];

/* Table structure [main].[Dis_uploadwork] */
CREATE TABLE [main].[Dis_uploadwork] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [filename] varchar(100) NOT NULL, 
  [file_illustrate] text NOT NULL, 
  [operate_illustrate] text NOT NULL, 
  [location] varchar(100) NOT NULL, 
  [thumbnail] varchar(100) NOT NULL, 
  [hittimes] integer NOT NULL, 
  [thumbup] integer NOT NULL, 
  [is_publish] bool NOT NULL, 
  [is_charge] bool NOT NULL, 
  [user_id] integer NOT NULL REFERENCES [Dis_alluser]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [type_id] integer REFERENCES [Dis_filetype]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [create_time] datetime NOT NULL, 
  [update_time] datetime NOT NULL, 
  [is_delated] bool NOT NULL);
CREATE INDEX [main].[Dis_uploadwork_type_id_cea519af] ON [Dis_uploadwork] ([type_id]);
CREATE INDEX [main].[Dis_uploadwork_user_id_b0675acc] ON [Dis_uploadwork] ([user_id]);

/* Data [main].[Dis_uploadwork] */
insert into [main].[Dis_uploadwork] values(8, '123', '', '11', '1/BlueDream_1080.jpg', '1/BlueDream_1080_GWondST.jpg', 0, 0, 0, 0, 1, null, '2020-02-23 22:41:46.532', '2020-02-23 22:41:46.532', 0);
insert into [main].[Dis_uploadwork] values(10, '123', '', '11', '1/BlueDream_4k_pQqUQH7.jpg', '1/oasis_4k.jpg', 0, 0, 0, 0, 1, null, '2020-02-23 22:42:31.318', '2020-02-23 22:42:31.318', 0);
insert into [main].[Dis_uploadwork] values(11, '123', '123123', '', '4/BlueDream_4k.jpg', '4/BlueDream_1080.jpg', 0, 0, 0, 0, 4, null, '2020-02-24 21:41:46.427', '2020-02-24 21:41:46.427', 0);
insert into [main].[Dis_uploadwork] values(13, '234', '', '234', '1/111322LW-5.jpg', '1/111322LW-5_o7piYSJ.jpg', 0, 0, 0, 0, 1, null, '2020-02-25 19:53:59.335', '2020-02-25 19:58:24.812', 0);


/* Drop table [main].[django_admin_log] */
drop table if exists [main].[django_admin_log];

/* Table structure [main].[django_admin_log] */
CREATE TABLE [main].[django_admin_log] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [action_time] datetime NOT NULL, 
  [object_id] text, 
  [object_repr] varchar(200) NOT NULL, 
  [change_message] text NOT NULL, 
  [content_type_id] integer REFERENCES [django_content_type]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [user_id] integer NOT NULL REFERENCES [Dis_alluser]([id]) DEFERRABLE INITIALLY DEFERRED, 
  [action_flag] [smallint unsigned] NOT NULL, 
  CHECK("action_flag" >= 0));
CREATE INDEX [main].[django_admin_log_content_type_id_c4bce8eb] ON [django_admin_log] ([content_type_id]);
CREATE INDEX [main].[django_admin_log_user_id_c564eba6] ON [django_admin_log] ([user_id]);

/* Data [main].[django_admin_log] */


/* Drop table [main].[django_migrations] */
drop table if exists [main].[django_migrations];

/* Table structure [main].[django_migrations] */
CREATE TABLE [main].[django_migrations] (
  [id] integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  [app] varchar(255) NOT NULL, 
  [name] varchar(255) NOT NULL, 
  [applied] datetime NOT NULL);

/* Data [main].[django_migrations] */
insert into [main].[django_migrations] values(1, 'CarnivalApoint', '0001_initial', '2020-02-23 17:36:10.534');
insert into [main].[django_migrations] values(2, 'contenttypes', '0001_initial', '2020-02-23 17:36:10.553');
insert into [main].[django_migrations] values(3, 'contenttypes', '0002_remove_content_type_name', '2020-02-23 17:36:10.569');
insert into [main].[django_migrations] values(4, 'auth', '0001_initial', '2020-02-23 17:36:10.586');
insert into [main].[django_migrations] values(5, 'auth', '0002_alter_permission_name_max_length', '2020-02-23 17:36:10.599');
insert into [main].[django_migrations] values(6, 'auth', '0003_alter_user_email_max_length', '2020-02-23 17:36:10.610');
insert into [main].[django_migrations] values(7, 'auth', '0004_alter_user_username_opts', '2020-02-23 17:36:10.620');
insert into [main].[django_migrations] values(8, 'auth', '0005_alter_user_last_login_null', '2020-02-23 17:36:10.630');
insert into [main].[django_migrations] values(9, 'auth', '0006_require_contenttypes_0002', '2020-02-23 17:36:10.637');
insert into [main].[django_migrations] values(10, 'auth', '0007_alter_validators_add_error_messages', '2020-02-23 17:36:10.648');
insert into [main].[django_migrations] values(11, 'auth', '0008_alter_user_username_max_length', '2020-02-23 17:36:10.659');
insert into [main].[django_migrations] values(12, 'auth', '0009_alter_user_last_name_max_length', '2020-02-23 17:36:10.670');
insert into [main].[django_migrations] values(13, 'auth', '0010_alter_group_name_max_length', '2020-02-23 17:36:10.683');
insert into [main].[django_migrations] values(14, 'auth', '0011_update_proxy_permissions', '2020-02-23 17:36:10.695');
insert into [main].[django_migrations] values(15, 'ZilanCMS', '0001_initial', '2020-02-23 17:36:10.716');
insert into [main].[django_migrations] values(16, 'admin', '0001_initial', '2020-02-23 17:36:10.733');
insert into [main].[django_migrations] values(17, 'admin', '0002_logentry_remove_auto_add', '2020-02-23 17:36:10.751');
insert into [main].[django_migrations] values(18, 'admin', '0003_logentry_add_action_flag_choices', '2020-02-23 17:36:10.769');
insert into [main].[django_migrations] values(19, 'sessions', '0001_initial', '2020-02-23 17:36:10.778');
insert into [main].[django_migrations] values(20, 'ZilanCMS', '0002_remove_uploadwork_type', '2020-02-23 17:37:00.306');
insert into [main].[django_migrations] values(21, 'ZilanCMS', '0003_uploadwork_type', '2020-02-23 17:38:02.312');
insert into [main].[django_migrations] values(22, 'ZilanCMS', '0004_auto_20200223_2226', '2020-02-23 22:26:24.578');
insert into [main].[django_migrations] values(23, 'ZilanCMS', '0005_uploadwork_is_delated', '2020-02-24 14:26:05.894');


/* Drop table [main].[django_session] */
drop table if exists [main].[django_session];

/* Table structure [main].[django_session] */
CREATE TABLE [main].[django_session] (
  [session_key] varchar(40) NOT NULL, 
  [session_data] text NOT NULL, 
  [expire_date] datetime NOT NULL, 
  CONSTRAINT [sqlite_autoindex_django_session_1] PRIMARY KEY ([session_key]));
CREATE INDEX [main].[django_session_expire_date_a5c62663] ON [django_session] ([expire_date]);

/* Data [main].[django_session] */
insert into [main].[django_session] values('n1aqx02wdrukvbhrzu0cx7m1cs09t4j3', 'Yjc1ZmRmNWY2MDM1OTY5Y2NkMWIyNmQzYjg0NjQ5YjcwM2EwYTM4ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NTlkZjAwNzVmYjFkZjRlNDYxY2NmY2ZmYjIzNjE5NWQ1NWRhZjllIn0=', '2020-03-10 00:07:01.779');


/* Commit Transaction */
commit transaction;

/* Enable Foreign Keys */
pragma foreign_keys = on;
