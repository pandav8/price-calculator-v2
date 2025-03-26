import streamlit as st
import pandas as pd

st.set_page_config(page_title="跨境定价计算器", layout="wide")

st.title("跨境定价计算器")
st.markdown("""
这个计算器可以帮助您计算跨境商品的最终售价，考虑各种成本和费用。
""")

# 创建两列布局
col1, col2 = st.columns(2)

with col1:
    st.subheader("基础信息")
    # 基础成本输入
    purchase_price = st.number_input("采购价格 (CNY)", min_value=0.0)
    exchange_rate = st.number_input("汇率 (CNY/USD)", min_value=0.0, value=7.2)
    
    # 物流费用
    shipping_cost = st.number_input("物流费用 (CNY)", min_value=0.0)
    customs_duty = st.number_input("关税税率 (%)", min_value=0.0, max_value=100.0, value=0.0)
    
    # 平台费用
    platform_fee = st.number_input("平台费用 (%)", min_value=0.0, max_value=100.0, value=15.0)
    
    # 利润率
    profit_margin = st.number_input("目标利润率 (%)", min_value=0.0, max_value=100.0, value=30.0)

with col2:
    st.subheader("计算结果")
    
    # 计算过程
    if st.button("计算售价"):
        # 计算总成本
        total_cost = purchase_price + shipping_cost
        
        # 计算关税
        duty_amount = total_cost * (customs_duty / 100)
        
        # 计算平台费用
        platform_amount = total_cost * (platform_fee / 100)
        
        # 计算目标利润
        target_profit = total_cost * (profit_margin / 100)
        
        # 计算最终售价（人民币）
        final_price_cny = total_cost + duty_amount + platform_amount + target_profit
        
        # 转换为美元
        final_price_usd = final_price_cny / exchange_rate
        
        # 显示结果
        st.markdown("### 计算结果")
        st.write(f"总成本: ¥{total_cost:.2f}")
        st.write(f"关税: ¥{duty_amount:.2f}")
        st.write(f"平台费用: ¥{platform_amount:.2f}")
        st.write(f"目标利润: ¥{target_profit:.2f}")
        st.write(f"最终售价 (CNY): ¥{final_price_cny:.2f}")
        st.write(f"最终售价 (USD): ${final_price_usd:.2f}")
        
        # 计算利润率
        actual_profit = final_price_cny - total_cost - duty_amount - platform_amount
        actual_profit_margin = (actual_profit / total_cost) * 100
        
        st.write(f"实际利润率: {actual_profit_margin:.2f}%")

# 添加使用说明
st.markdown("""
### 使用说明
1. 输入商品采购价格（人民币）
2. 设置当前汇率（CNY/USD）
3. 输入物流费用（人民币）
4. 设置关税税率（百分比）
5. 设置平台费用（百分比）
6. 设置目标利润率（百分比）
7. 点击"计算售价"按钮查看结果

计算结果将显示：
- 总成本
- 关税金额
- 平台费用
- 目标利润
- 最终售价（人民币和美元）
- 实际利润率
""") 