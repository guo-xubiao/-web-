#-一个小作业项目，持续完善中
#-各个文件的作用
Web_Test_boxuegu
├────allure-results/ allure测试报告
├────outputs/  测试报告，日志，图片保存的目录
│    ├────image/
│    ├────log/
│    │    └────test.log
|
├────test_case/ 测试用例目录
│    ├────__init__.py
│    ├────conftest.py   pytest框架中一个特殊且重要的组件，它允许你定义和重用测试fixture
│    ├────test_login.py   登录测试用例
│    ├────test_page_redirect.py   页面转换测试用例
|
utils/  工具类
|
data_utils/  数据处理
├────__init__.py
└────faker_handle.py  封装的faker包的一些方法
|
database_utils/  数据库处理
├────__init__.py
└────mysql_handle.py  封装的pymysql的一些操作方法
|
files_utils/  文件处理
├────__init__.py
├────files_handle.py 封装文件操作相关的一些方法
└────yaml_handle.py  读写yaml文件
|
logger_utils/ 日志处理
├────__init__.py
└────loguru_log.py  封装的loguru日志处理
|
report_utils/ 报告处理
├────__init__.py
├────allure_handle.py 封装的allure的一些操作
├────get_results_handle.py  从测试报告中获取测试结果
|
ui_utils/  UI工具类
├────__init__.py
├────base_page.py   封装的selenium的一些基础浏览器操作方法
└────get_driver.py  通过webdriver自动获取浏览器驱动，避免手动下载
|
├────config/  配置文件目录
├────conftest.py   pytest框架中一个特殊且重要的组件，它允许你定义和重用测试fixture
├────pytest.ini    pytest的配置文件
├────README.md
├────requirements.txt 项目包管理
├────run.py   框架主入口文件
