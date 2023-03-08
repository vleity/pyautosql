--------------------------------------------------------------------------
--------------------------------------------------------------------------
-- @ Main  : {{table_name}}.hql
-- @ Date  : {{create_date}}
-- @ Author: {{author}}
-- @ Desc  : 
-- 1. 创建 {{schema}}.{{table_name}} 表
--------------------------------------------------------------------------


-- 设置执行引擎 mr tez spark
set hive.execution.engine={{ engine | default("mr") }};

-- 切换数据库
use {{ schema }};


-- 创建表，LOCATION 'hdfs://usr/warehouse/hive/schema/<table_name>/<partition_name>'
CREATE TABLE IF NOT EXISTS {{schema}}.{{ table_name }}(
    {%- for col in columns %}
    {%- if loop.last %}
    {{col.column_name}} {{col.column_type}} COMMENT '{{col.column_comment}}'
    {%- else %}
    {{col.column_name}} {{col.column_type}} COMMENT '{{col.column_comment}}',
    {%- endif %}
    {%- endfor %}
)
COMMENT '{{ table_comment | default("") }}'
{%- if partitions %}
PARTITIONED BY (
    {%- for col in partitions.columns %}
    {%- if loop.last %}
    {{col.partition_column}} {{col.partition_column_type}} COMMENT '{{col.partition_column_comment}}'
    {%- else %}
    {{col.partition_column}} {{col.partition_column_type}} COMMENT '{{col.partition_column_comment}}',
    {%- endif %}
    {%- endfor %}
)
{%- endif %}
ROW FORMAT DELIMITED FIELDS TERMINATED BY '{{delimited_fields | default("\001")}}'
{%- if null_defined or null_defined == "" %}
NULL DEFINED AS '{{null_defined}}'
{%- endif %}
STORED AS {{ store_type | default("TEXTFILE") }}
LOCATION '{{schema_location}}/{{ table_name }}'
;


-- 删除表
--DROP TABLE IF EXISTS {{schema}}.{{ table_name }};

{% if partitions.partition_values %}
-- 添加分区
{%- for item in partitions.partition_values %}
ALTER TABLE {{schema}}.{{ table_name }} ADD IF NOT EXISTS PARTITION ({%- for col in partitions.columns %}
    {%- if loop.last -%}
    {{col.partition_column}} = '{{item[loop.index0]}}'
    {%- else -%}
    {{col.partition_column}} = '{{item[loop.index0]}}',
    {%- endif %}
    {%- endfor %})
LOCATION '{{schema_location}}/{{ table_name }}/{{item | join("/")}}';
{% endfor %}

--删除分区
{%- for item in partitions.partition_values %}
--ALTER TABLE {{schema}}.{{ table_name }} DROP IF EXISTS PARTITION ({%- for col in partitions.columns %}
    {%- if loop.last -%}
    {{col.partition_column}} = '{{item[loop.index0]}}'
    {%- else -%}
    {{col.partition_column}} = '{{item[loop.index0]}}',
    {%- endif %}
    {%- endfor %});
{% endfor %}

{%- endif %}
