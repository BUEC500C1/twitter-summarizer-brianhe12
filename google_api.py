def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    import pandas as pd
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'SA_Token.json'
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Image Labels:')

    df = pd.DataFrame(columns=['description', 'score', 'topicality'])

    for label in labels:
        df = df.append(
            dict(
                description=label.description,
                score=label.score,
                topicality=label.topicality
            ), ignore_index=True)
            
    print(df)
    print('\n')

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
