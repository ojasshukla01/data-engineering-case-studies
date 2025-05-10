def lambda_handler(event, context=None):
    transformed = {
        "id": event["user_id"],
        "action": event["event_type"],
        "event_time": event["timestamp"]
    }
    return transformed
