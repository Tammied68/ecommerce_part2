def upload_media(image_path):
    """
    Uploads an image to X (Twitter) using Tweepy.

    This helper function uploads an image file and returns the
    media ID, which can be attached to a tweet via post_tweet.

    Parameters:
        image_path (str): The file path to the image being uploaded.

    Returns:
        str or None: The media ID string if upload succeeds,
                     or None if the upload fails.
    """
    try:
        media = api.media_upload(image_path)
        return media.media_id_string
    except Exception as e:
        print("Error uploading media:", e)
        return None
