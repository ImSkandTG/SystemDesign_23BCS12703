from nselib import capital_market
from nselib import derivatives
import streamlit as st
from datetime import datetime, timedelta

st.header("Indian Stock Financial Dashboard")

instrument = st.sidebar.selectbox("Instrument Type", options=("NSE Equity Market", "NSE Derivatives Market"))

data = None

if instrument == "NSE Equity Market":
    data_info = st.sidebar.selectbox("Data to extract", options=('bhav_copy_equities','bhav_copy_with_delivery','equity_list', 'fno_equity_list',
                                                                'market_watch_all_indices', 'nifty50_equity_list','block_deals_data', 'bulk_deal_data',
                                                                'india_vix_data','short_selling_data','deliverable_position_data',
                                                                'index_data','price_volume_and_deliverable_position_data','price_volume_data'))
    try:
        if (data_info == 'equity_list') or (data_info == 'fno_equity_list') or (data_info == 'market_watch_all_indices') or (data_info == 'nifty50_equity_list'):
            data = getattr(capital_market, data_info)()
        elif (data_info == 'bhav_copy_equities') or (data_info == 'bhav_copy_with_delivery'):
            date = st.sidebar.text_input('Date (DD-MM-YYYY)','20-04-2026')
            data = getattr(capital_market,data_info)(date)
        elif (data_info == 'block_deals_data') or (data_info == 'bulk_deal_data') or (data_info == 'india_vix_data') or (data_info == 'short_selling_data'):
            period_ = st.sidebar.text_input('Period' ,'1M')
            data = getattr(capital_market, data_info)(period = period_)
        elif (data_info == 'deliverable_position_data') or (data_info == 'index_data') or (data_info == 'price_volume_and_deliverable_position_data') or (data_info == 'price_volume_data'):
            data = getattr(capital_market, data_info)()
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        st.info("Try changing the date to a recent trading day (DD-MM-YYYY format)")

elif instrument == "NSE Derivatives Market":
    st.info("Derivatives market functionality coming soon!")

if data is not None:
    st.write(data)
elif instrument == "NSE Equity Market":
    st.warning("No data to display. Please select an option or check the error above.")  