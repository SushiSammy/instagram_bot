from publitio_upload import *
from instagram_upload import upload_to_instagram

def main():
    # Generate video


    # Upload video to publitio
    publitio_response = upload_to_publitio('/Users/samuelxing/instagram_bot/test_vid.mp4')

    # Upload video to instagram
    video_url = publitio_response['url_short']
    upload_to_instagram(video_url)
    # test url: "https://media.publit.io/file/test-vid-3.mp4"

    # Delete video from publitio
    video_id = publitio_response['id']
    delete_from_publitio(video_id)



if __name__ == "__main__":
    main()