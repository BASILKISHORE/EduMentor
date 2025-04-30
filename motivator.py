def main(req):
    content = req.params.get('content')
    return {'motivation': f"Great job with {content}! Keep going!"}