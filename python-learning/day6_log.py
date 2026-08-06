import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log"
)

logging.info("AI系统启动")

name=input("请输入用户名：")

logging.info(
    f"用户输入:{name}"
)