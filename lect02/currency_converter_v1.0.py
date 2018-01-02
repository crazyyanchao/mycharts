"""
@FILE_NAME: currency_converter_v1.0.py
@Description: TODO(Describe the role of this Python file)
@author YanchaoMa yanchaoma@foxmail.com
@date  2017/12/6 23:51
 
"""
# RATE
USD_VS_RMB = 6.77

# RMB INPUT
rmb_str_value = input('请输入人民币(CNY)金额:')

# STRING CONVERTER NUMBER
rmb_value = eval(rmb_str_value)

# RATE CALSULATE
usd_value = rmb_value / USD_VS_RMB

# OUTPUT
print('美元(USD)金额是：', usd_value)