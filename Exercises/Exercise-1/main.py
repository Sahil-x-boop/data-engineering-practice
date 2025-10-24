import requests
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  
]


def download_file(url):
    """Downloads a file from the given URL and saves it locally."""
    filename = url.split("/")[-1]  # extract file name
    try:
        print(f"Downloading: {filename}")
        response = requests.get(url, stream=True, timeout=20)
        response.raise_for_status()  # raise error if not 200 OK

        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Saved: {filename}\n")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}\n")
    

def main():
    print("Everything is running inside Docker successfully\n")
    os.makedirs("data", exist_ok=True)
    os.chdir("data")  

    for url in download_uris:
        download_file(url)

    print("All downloads complete")


if __name__ == "__main__":
    main()
