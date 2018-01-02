"""
@FILE_NAME: currency_converter_v2.0.py
@Description: TODO(Describe the role of this Python file)
@author YanchaoMa yanchaoma@foxmail.com
@date  2018/01/02
新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
 
"""
# RATE
USD_VS_RMB = 6.77

# 带单位的货币输入
curency_str_value = input('请输入带单位的货币金额:')

# 获取货币单位
unit    =   curency_str_value[-3:]

if unit == 'CNY':
    # 输入的是人民币
    rmb_str_value = curency_str_value[:-3]
    # STRING CONVERTER NUMBER
    rmb_value = eval(rmb_str_value)

    # RATE CALSULATE
    usd_value = rmb_value / USD_VS_RMB

    # OUTPUT
    print('美元(USD)金额是：', usd_value)

elif unit == 'USD':
    # 输入的是美元
    usd_str_value = curency_str_value[:-3]
    usd_value = eval(usd_str_value)
    rmb_value = usd_value*USD_VS_RMB

    print('人民币（CNY）金额是：', rmb_value);

else:
    # 其他情况
    print('目前版本尚不支持该币种！')
