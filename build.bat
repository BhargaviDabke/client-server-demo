cd server
docker build -t fastapi-server -f server.Dockerfile .
cd ../ui
docker build -t streamlit-client -f client.Dockerfile .
cd ..
