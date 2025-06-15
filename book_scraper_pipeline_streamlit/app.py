import streamlit as st
from scraper.scrape_site import smart_scrape
from etl.load import transform_and_save
import pandas as pd

st.set_page_config(page_title="Smart Web Scraper", layout="wide")
st.title("🌐 Smart Web Scraper with CrewAI Agents")

url = st.text_input("Enter the website URL to scrape", "http://books.toscrape.com")

if st.button("Scrape and Preview"):
    with st.spinner("Scraping data..."):
        try:
            data = smart_scrape(url)
            if not data:
                st.warning("No data found.")
            else:
                df = pd.DataFrame(data)
                st.success(f"Scraped {len(df)} records successfully!")
                st.dataframe(df)

                transform_and_save(data, url)
                csv_filename = f"scraped_{url.replace('http://', '').replace('https://', '').replace('/', '_')[:50]}.csv"
                st.download_button(
                    label="📥 Download CSV",
                    data=df.to_csv(index=False),
                    file_name=csv_filename,
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Error: {e}")
