def main(req):
    user_id = req.params.get('user_id')
    query = req.params.get('query')
    return {'plan': f"Study Plan for {user_id}: 1 hour on {query}"}