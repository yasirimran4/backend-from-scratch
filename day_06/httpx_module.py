import httpx
import asyncio


            
async def fetch_data(url):

    try:
        with httpx.Client() as client:
            response = client.get(url)
        return response.json()
    except Exception as e:
        print(f"Error occurs {str(e)}")


async def main():
    try:
        with httpx.Client() as client:
            response = client.get("https://tiktok.com",timeout=10.0)
            print(response.status_code)
            response = client.get("https://facebook.com",timeout=10.0)
            print(response.status_code)
            response = client.get("https://youtube.com",timeout=10.0)
            print(response.status_code)
        url = 'https://api.example.com/users'
        data = await fetch_data(url)    
        print(data)   
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e.response.status_code}")
    except httpx.TimeoutException:
        print("Request timed out")
    except httpx.RequestError as e:
        print(f"Request failed: {e}")


if __name__ == '__main__':
    asyncio.run(main())
  
