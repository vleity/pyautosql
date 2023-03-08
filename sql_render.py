##########################################################################
# @ Main  : sql_render.py
# @ Date  : 2023
# @ Author: vleity
# @ Desc  : 渲染模板生成sql脚本生成器类定义
# 1. xxxx
# 2. xxxx
##########################################################################


import os, jinja2


class SqlRender:
    """
    生成器类
    """
    def __init__(self, template, context, tpl_path="./templates"):
        self.tpl_path = os.path.abspath(tpl_path)
        self.template = template
        self.context = context
        
    def render(self):
        """通过jinja2渲染"""
        TemplateLoader = jinja2.FileSystemLoader(self.tpl_path)
        TemplateEnv = jinja2.Environment(loader=TemplateLoader)
        template = TemplateEnv.get_template(self.template)
        return template.render(**self.context)
