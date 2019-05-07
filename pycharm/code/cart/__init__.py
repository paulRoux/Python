from flask import Blueprint

# 创建蓝图 如果模板在小范围没找到，则会往顶层去寻找，而且顶层的优先级高于底层
app_cart = Blueprint("app_cart", __name__, template_folder="templates", static_folder="static")


# 在__init__.py被执行的时候，把视图加载进来，让蓝图与应用程序知道视图的存在
from .views import get
