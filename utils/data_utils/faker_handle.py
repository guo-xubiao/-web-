# 封装的faker包的一些方法
import faker

# 创建一个Faker实例
fake = faker.Faker()

# 生成随机字符串
def generate_random_string(length=10):
    return fake.pystr(min_chars=length, max_chars=length)

# 生成随机邮箱
def generate_random_email():
    return fake.email()

# 生成随机手机号
def generate_random_phone_number():
    return fake.phone_number()

# 生成随机地址
def generate_random_address():
    return fake.address()

# 生成随机名字
def generate_random_name():
    return fake.name()

# 生成随机公司名
def generate_random_company_name():
    return fake.company()

# 生成随机职位
def generate_random_job():
    return fake.job()

# 生成随机日期
def generate_random_date():
    return fake.date()

# 生成随机时间
def generate_random_time():
    return fake.time()

# 生成随机日期和时间
def generate_random_datetime():
    return fake.date_time()

# 生成随机IP地址
def generate_random_ip_address():
    return fake.ipv4_private()

# 生成随机URL
def generate_random_url():
    return fake.uri()

#其他方法