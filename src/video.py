import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        if Video.print_info(self)['items'] == []:
            try:
                self.name: str = Video.print_info(self)['items'][0]['snippet']['title']
                self.url: str = f"https://www.youtube.com/watch?v={video_id}"
                self.views: int = Video.print_info(self)['items'][0]['statistics']['viewCount']
                self.likes: int = Video.print_info(self)['items'][0]['statistics']['likeCount']
            except IndexError:
                self.name = None
                self.url = None
                self.views = None
                self.likes = None

    def __repr__(self) -> str:
        return f'id - {self.video_id}'

    def __str__(self) -> str:
        return f"{Video.print_info(self)['items'][0]['snippet']['title']}"

    def print_info(self) -> dict:
        video_id = self.video_id
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
        return video_response


class PLVideo(Video):
    def __init__(self, video_id: str, plvideo_id: str) -> None:
        super().__init__(video_id)
        self.plvideo_id = plvideo_id

