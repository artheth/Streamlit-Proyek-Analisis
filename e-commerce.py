import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

st.write("""
# PROYEK ANALISIS DATA
Menentukan Tujuan Bisnis
1. Menghitung nilai order pada tiap kota yang terbesar bedasarkan order status
2. Mencari jumlah pengiriman pemesanan yang terbesar di tiap kota berdasarkan pemesanan
3. Mencari persentase pembatalan pemesanan terbesar dari customer tiap kota""")

st.write("""
# 1. Menghitung nilai order pada tiap kota yang terbesar bedasarkan order status""")

# Mengambil dataset 
sum_order_city = pd.read_csv("https://raw.githubusercontent.com/artheth/Proyek-Analisis/main/order_terbesar.csv")


# Menampilkan dataset
st.text("Tabel Order Status By City")
st.table(sum_order_city)

# Grafik order tiap terbesar
fig, ax = plt.subplots(figsize=(10, 5))

colors = ["#D3D3D3", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]

sns.barplot(
    x="order_status",
    y="count_city_order",
    data=sum_order_city,
    palette=colors,
    ax=ax
)
plt.title("Order Status By City", loc="left", fontsize=15)
plt.ylabel("Count")
plt.xlabel("Order")
plt.tick_params(axis='x', labelsize=10)
st.pyplot(fig)

st.caption('Nilai order yang terbesar yaitu order status delivered sebesar 96487, sedangkan order status terkecil yaitu approved sebanyak 2')

st.write("""
# 2. Mencari jumlah pengiriman pemesanan yang terbesar di tiap kota berdasarkan pemesanan""")

# Mengambil dataset 
city_orders_delivered_top10 = pd.read_csv("https://raw.githubusercontent.com/artheth/Proyek-Analisis/main/order_delivered%20_tp10.csv")


# Menampilkan dataset
st.text("Tabel Order delivered By City")
st.table(city_orders_delivered_top10)

# Grafik order tiap terbesar
fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x="count_delivered",
    y="customer_city",
    data=city_orders_delivered_top10
)
plt.title("Order Status Delivered By City", loc="left", fontsize=15)
plt.ylabel("City Order Delivered")
plt.xlabel("Count Delivered")
plt.tick_params(axis='x', labelsize=8)
st.pyplot(fig)

st.caption('Dapat disimpulkan bahwa 5 kota dengan order status delivered terbesar adalah sao paulo, rio de janeiro, belo horizonter, brasilia dan curitiba')

st.write("""
# 3. Mencari persentase pembatalan pemesanan terbesar dari customer tiap kota""")

# Mengambil dataset 
city_orders_canceled_top10 = pd.read_csv("https://raw.githubusercontent.com/artheth/Proyek-Analisis/main/order_canceled_top10.csv")


# Menampilkan dataset
st.text("Tabel Order canceled By City")
st.table(city_orders_canceled_top10)

# Grafik order tiap terbesar
fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x="percent_orders_canceled",
    y="customer_city",
    data=city_orders_canceled_top10

)
plt.title("Order Status Canceled By City", loc="left", fontsize=15)
plt.grid()
plt.ylabel("City Order Canceled")
plt.xlabel("Count Canceled")
plt.tick_params(axis='x', labelsize=8)
st.pyplot(fig)

st.caption('Dapat disimpulkan bahwa 5 kota dengan order status canceled terbesar yaitu sao paulo sebesar 22,40%, rio de janeiro sebesar 7,68%, belo horizonte sebesar 2,72%, guarulhos sebesar 2,08% dan campinas sebesar 1,60%')