from api_handler import generate_reply_api, APIError

def generate_reply(email, tone, intent):
    try:
        reply = generate_reply_api(email, tone, intent)
        return reply, None
    except APIError as e:
        return None, str(e)
