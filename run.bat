docker rm -f fastapi-container
@REM docker run -it --name fastapi-container -p 8000:8000 fastapi-server # For Debugging/Testing/Development
docker run -d --name fastapi-container -p 8000:8000 fastapi-server