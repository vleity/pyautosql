##########################################################################
# @ Main  : sql_render.py
# @ Date  : 2023
# @ Author: vleity
# @ Desc  : 渲染模板生成sql脚本生成器类定义
# 1. xxxx
# 2. xxxx
##########################################################################

import sys
sys.path.append("..")
from sql_render import SqlRender
from datetime import datetime

# context

# 单分区
context1 = {
    "create_date": datetime.now().strftime("%Y-%m-%d"),
    "author": "vleity",
    "schema": "schema",
    "table_name": "dwd_d_xxx",
    "table_comment": "表注释",
    "delimited_fields": "\\001",
    "null_defined": "",
    "store_type": "TEXTFILE",
    "schema_location": "hdfs://usr/warehouse/hive/schema",
    "columns": [
        {
        "column_name": "xxx1",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx2",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx3",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx4",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx5",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx6",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx7",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx8",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx9",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        }
    ],
    "partitions": {
        "columns": [
            {
            "partition_column": "p_acct_month",
            "partition_column_type": "STRING",
            "partition_column_comment": "月份"
            }
        ],
        "partition_values": [
            ["${V_MONTH}"]
        ]
    }    
}

# 双分区
context2 = {
    "create_date": "2023-01-01",
    "author": "vleity",
    "schema": "schema",
    "table_name": "dwd_d_xxx",
    "table_comment": "表注释",
    "delimited_fields": "\\001",
    "null_defined": "",
    "store_type": "TEXTFILE",
    "schema_location": "hdfs://usr/warehouse/hive/schema",
    "columns": [
        {
        "column_name": "xxx1",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx2",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx3",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx4",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx5",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx6",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx7",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx8",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        },
        {
        "column_name": "xxx9",
        "column_type": "STRING",  # 大写
        "column_comment": "字段注释"
        }
    ],
    "partitions": {
        "columns": [
            {
            "partition_column": "p_acct_month",
            "partition_column_type": "STRING",
            "partition_column_comment": "月份"
            },
            {
            "partition_column": "p_city",
            "partition_column_type": "STRING",
            "partition_column_comment": "城市"
            }
        ],
        "partition_values": [
            ["${V_MONTH}","${V_CITY}"]
        ]
    }    
}

# 渲染
sqlrender = SqlRender(template = "hive_create_table.sql", context = context2, tpl_path = "../templates")
sql = sqlrender.render()

# 打印结果
print(sql)



