# 数据库
SQLALCHEMY_DATABASE_URI = "mysql://root:Feng1997@localhost:3306/superset_database_localdev"

# 启用中文界面
BABEL_DEFAULT_LOCALE = 'zh'

# 支持的语言列表（可选）
LANGUAGES = {
    'zh': {'flag': 'cn', 'name': '简体中文'},
    'en': {'flag': 'us', 'name': 'English'},
    'ja': {'flag': 'jp', 'name': '日本語'},
    # 可添加更多语言
}