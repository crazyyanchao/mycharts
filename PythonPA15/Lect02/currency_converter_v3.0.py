"""
@Description: TODO(新增功能：程序一直执行直到用户选择退出)
@author YanchaoMa yanchaoma@foxmail.com
@date  2018/01/02
"""
# RATE
USD_VS_RMB = 6.77

# 带单位的货币输入
curency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）:')

i = 0

while curency_str_value != 'Q':
    i = i + 1
    print('循环次数',i)
    # 获取货币单位
    unit = curency_str_value[-3:]

    if unit == 'CNY':
        # 输入的是人民币
        rmb_str_value = curency_str_value[:-3]
        # STRING CONVERTER NUMBER
        rmb_value = eval(rmb_str_value)

        # RATE CALSULATE100
        usd_value = rmb_value / USD_VS_RMB

        # OUTPUT
        print('美元(USD)金额是：', usd_value)

    elif unit == 'USD':
        # 输入的是美元
        usd_str_value = curency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value * USD_VS_RMB

        print('人民币（CNY）金额是：', rmb_value);

    else:
        # 其他情况
        print('目前版本尚不支持该币种！')

    # 带单位的货币输入
    print('***************************************')
    curency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）:')

print('程序已退出！')