mkdir -p ~/.streamlit/

echo "\
[server]\n\
poer=$PORT\n\
enableCORS=false\n\
headless=true\n\
\n\
"> ~/.streamlit/config.toml

