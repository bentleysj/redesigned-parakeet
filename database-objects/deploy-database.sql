create schema task_catalog;

create  table TASK_CATALOG.TASKS
(
    ID BIGINT IDENTITY(1, 1),
    CLASSIFYING_ID VARCHAR(255),
    name varchar(255) not null,
    description text,
    created_at datetime default CURRENT_TIMESTAMP,
    lastupdated_at datetime, 
    type varchar(255) not null,

    repeate_type VARCHAR(255),
    dayofmonth integer,
    dayofweek integer,
    timeofday time,
    numberofperiods integer,

    amount decimal,
    account VARCHAR(255),

    weekdays_only TINYINT DEFAULT 0,
    max_concurrent integer DEFAULT 1,
    PERSISTED TINYINT DEFAULT 0
)
;

CREATE UNIQUE INDEX task_catalog_tasks_id_uindex ON task_catalog.tasks (ID);

CREATE TABLE task_catalog.TASK_INSTANCES
(
    ID BIGINT IDENTITY(1, 1),
    TASK_ID BIGINT,
    STATUS VARCHAR(255),
    CREATED DATETIME default CURRENT_TIMESTAMP, 
    FINISHED_AT DATETIME,
    LAST_UPDATED_AT DATETIME,

);

CREATE UNIQUE INDEX task_catalog_task_instances_id_uindex ON task_catalog.task_instances (ID);
;

ALTER TABLE task_catalog.TASK_INSTANCES
ADD CONSTRAINT FK_TASKS_TASTKCATALOG FOREIGN KEY (TASK_ID)
REFERENCES task_catalog.TASKS (ID);

;

CREATE TABLE task_catalog.CURRENT_TASKS
(
    ID BIGINT IDENTITY(1, 1),
    TASK_ID BIGINT,
    TASK_INSTANCE_ID BIGINT,
    STATUS VARCHAR(255),
    CREATED DATETIME default CURRENT_TIMESTAMP, 
    FINISHED_AT DATETIME,
    LAST_UPDATED_AT DATETIME,
    CONSTRAINT FK_CURRENTTASKS_TASTKCATALOG FOREIGN KEY (TASK_ID)
    REFERENCES task_catalog.TASKS (ID),
    CONSTRAINT FK_CURRENTTASK_TASKINSTANCE FOREIGN KEY (TASK_INSTANCE_ID)
    REFERENCES task_catalog.TASK_INSTANCES (ID)
);

create schema task_users; 
create table task_users.USERS
(
    ID BIGINT IDENTITY(1, 1),
    USERNAME VARCHAR(255) NOT NULL,
    PASSWORD VARCHAR(255) NOT NULL,
    EMAIL VARCHAR(255), 
    CREATED_AT DATETIME default CURRENT_TIMESTAMP,
    LAST_UPDATED_AT DATETIME
);

alter table task_catalog.TASKS
add column USER_ID BIGINT;
;

alter table task_catalog.task_instances
add column USER_ID BIGINT;

alter table task_catalog.CURRENT_TASKS
add column USER_ID BIGINT;