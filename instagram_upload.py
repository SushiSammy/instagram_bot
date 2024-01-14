import requests, json, constants, time

def get_creds():
    """ Get creds required for use in the applications

    Returns:
        dictonary: credentials needed globally
    """
    creds = {
        'access_token': constants.INSTAGRAM_ACCESS_TOKEN,
        'graph_domain': 'https://graph.facebook.com/',
        'graph_version': 'v18.0',
        'endpoint_base': 'https://graph.facebook.com/v18.0/',
        'instagram_account_id': constants.INSTAGRAM_USER_ID,
    }

    return creds

def make_api_call(url, endpointParams, type) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""

	if type == 'POST' : # post request
		data = requests.post(url, endpointParams)
	else : # get request
		data = requests.get(url, endpointParams)

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps(endpointParams, indent = 4) # pretty print for cli
	response['json_data'] = json.loads(data.content) # response data from the api
	response['json_data_pretty'] = json.dumps(response['json_data'], indent = 4) # pretty print for cli

	return response # get and return content

def create_media_object(params) :
	""" Create media object

	Args:
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-user-id}/media?image_url={image-url}&caption={caption}&access_token={access-token}
		https://graph.facebook.com/v5.0/{ig-user-id}/media?video_url={video-url}&caption={caption}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + params['instagram_account_id'] + '/media' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['caption'] = params['caption']  # caption for the post
	endpointParams['access_token'] = params['access_token'] # access token

	if params['media_type'] == 'IMAGE': # posting image
		endpointParams['image_url'] = params['media_url']  # url to the asset
	else : # posting video
		endpointParams['media_type'] = params['media_type']  # specify media type
		endpointParams['video_url'] = params['media_url']  # url to the asset
	
	return make_api_call(url, endpointParams, 'POST') # make the api call

def get_media_object_status(mediaObjectId, params) :
	""" Check the status of a media object

	Args:
		mediaObjectId: id of the media object
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-container-id}?fields=status_code

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + '/' + mediaObjectId # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'status_code' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return make_api_call(url, endpointParams, 'GET') # make the api call

def publish_media(mediaObjectId, params) :
	""" Publish content

	Args:
		mediaObjectId: id of the media object
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-user-id}/media_publish?creation_id={creation-id}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + params['instagram_account_id'] + '/media_publish' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['creation_id'] = mediaObjectId # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return make_api_call(url, endpointParams, 'POST') # make the api call

def upload_to_instagram(url):
    params = get_creds() # get creds from defines

    params['media_type'] = 'REELS' # type of asset
    params['media_url'] = url # url on public server for the post
    params['caption'] = 'this is a test description'
    params['caption'] += "\n"
    params['caption'] += "\n"
    params['caption'] += "\n#funny #meme" # caption for the post

    imageMediaObjectResponse = create_media_object(params) # create a media object through the api
    print(imageMediaObjectResponse['json_data'])
    imageMediaObjectId = imageMediaObjectResponse['json_data']['id'] # id of the media object that was created
    imageMediaStatusCode = 'IN_PROGRESS'

    print("\n---- IMAGE MEDIA OBJECT -----\n") # title
    print("\tID:") # label
    print("\t" + imageMediaObjectId) # id of the object

    while imageMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
        imageMediaObjectStatusResponse = get_media_object_status(imageMediaObjectId, params) # check the status on the object
        imageMediaStatusCode = imageMediaObjectStatusResponse['json_data']['status_code'] # update status code

        print("\n---- IMAGE MEDIA OBJECT STATUS -----\n") # display status response
        print("\tStatus Code:") # label
        print("\t" + imageMediaStatusCode) # status code of the object

        time.sleep( 5 ) # wait 5 seconds if the media object is still being processed

    publish_media(imageMediaObjectId, params) # publish the post to instagram