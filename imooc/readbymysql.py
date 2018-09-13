import pymysql.cursors

# 获取链接
connection = pymysql.connect(host='118.89.242.225',user='root',password='789456',db='wikiurl',charset='utf8mb4')

try:
    #获取会话指针
    with connection.cursor() as cursor:
        #查询语句
        sql= "select  urlname , urlhref from urls  "
        # 查询条数
        count = cursor.execute(sql);
        #查询具体数据
        result = cursor.fetchall();
        #设置具体查询条数
        # result = cursor.fetchmany(size=3)
        print(result)


finally:
    connection.close()