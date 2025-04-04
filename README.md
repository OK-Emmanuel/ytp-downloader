# YouTube Playlist Downloader

## Description

I created this project (YouTube Playlist Downloader) tool to manage my internet distractions while learning on Youtube. It is intended for educational purposes only. It is designed to help users download entire YouTube playlists for offline learning, thereby avoiding internet distractions. Please note that this tool should not be redistributed.

## Features

- **Download Entire Playlists**: Input a YouTube playlist URL and download all videos in the playlist.
- **Format and Quality Options**: Choose the video format and quality for downloads.
- **User-Friendly Interface**: A simple and intuitive user interface built with HTML and CSS.

## Technologies Used

I'm running the project on Django. The repository is predominantly composed of Python (75.2%), with some HTML (14.6%) and CSS (10.2%). The backend system utilizes Python for core functionality, such as handling video downloads and processing playlists, while HTML and CSS are used for the frontend interface. Key features include the ability to input a URL for single video and YouTube playlist URL and download the videos in that playlist, with options for video quality or format. I made use of libraries such as `pytube` or `youtube-dl` for handling the downloading process. 

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/OK-Emmanuel/ytp-downloader.git
    ```
2. Navigate into the project directory:
    ```sh
    cd ytp-downloader
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```
2. Open your web browser and navigate to `http://localhost:5000`.
3. Enter the URL of the YouTube playlist you wish to download.
4. Select your preferred video format and quality, then start the download.

## Disclaimer

This tool is intended for educational purposes only. Please respect YouTube's Terms of Service and do not redistribute this software.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

## License

This project is licensed under the MIT License.
