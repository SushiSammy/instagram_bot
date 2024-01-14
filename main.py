from publitio_upload import *
from instagram_upload import upload_to_instagram

def main():
    # Generate video


    # Upload video to publitio
    response = upload_to_publitio('/Users/samuelxing/instagram_bot/test_vid.mp4')

    # Upload video to instagram
    video_url = response['url_short']
    # upload_to_instagram("https://media.publit.io/file/test-vid-3.mp4")

    # Delete video from publitio
    video_id = response['id']
    delete_from_publitio(video_id)



if __name__ == "__main__":
    main()